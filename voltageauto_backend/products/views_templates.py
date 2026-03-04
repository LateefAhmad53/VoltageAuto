from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import Product, Inquiry


class HomeView(TemplateView):
    template_name = 'products/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(featured=True)[:3]
        context['latest_products'] = Product.objects.exclude(status='sold')[:6]
        return context


class ProductListView(TemplateView):
    template_name = 'products/products.html'


class ProductDetailView(TemplateView):
    template_name = 'products/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['product'] = Product.objects.prefetch_related('images', 'reviews').get(slug=kwargs['slug'])
        except Product.DoesNotExist:
            context['product'] = None
        # Provide WhatsApp number to template for Buy Now action
        context['whatsapp_number'] = getattr(settings, 'WHATSAPP_NUMBER', '2349150729116')
        return context


@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class ContactView(View):
    """Handle contact form submissions"""
    
    def get(self, request):
        """Display contact page"""
        return render(request, 'products/contact.html')
    
    def post(self, request):
        """Handle contact form submission"""
        try:
            if request.content_type and 'application/json' in request.content_type:
                data = json.loads(request.body or '{}')
            else:
                data = request.POST.dict()
            
            # Validate required fields
            required_fields = ['name', 'email', 'phone', 'subject', 'message']
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse(
                        {'success': False, 'message': f'{field.capitalize()} is required'},
                        status=400
                    )
            
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            phone = data.get('phone', '').strip()
            subject = data.get('subject', '').strip()
            message = data.get('message', '').strip()
            
            # Save inquiry to database
            inquiry = Inquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=f"Subject: {subject}\n\n{message}",
                status='pending'
            )
            
            # Send email to admin
            try:
                subject_email = f"New Contact Form Submission - {subject}"
                message_body = f"""
                Name: {name}
                Email: {email}
                Phone: {phone}
                Subject: {subject}
                
                Message:
                {message}
                
                Inquiry ID: {inquiry.id}
                """
                
                send_mail(
                    subject_email,
                    message_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you! Your message has been received. We will contact you soon.',
                'inquiry_id': str(inquiry.id)
            })
        
        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'message': 'Invalid request format'},
                status=400
            )
        except Exception as e:
            print(f"Contact form error: {e}")
            return JsonResponse(
                {'success': False, 'message': 'An error occurred. Please try again.'},
                status=500
            )


class ServicesView(TemplateView):
    """Display services page"""
    template_name = 'products/services.html'


class AffiliateView(TemplateView):
    """Display affiliate program page"""
    template_name = 'products/affiliate.html'

