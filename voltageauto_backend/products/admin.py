from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Review, Inquiry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def product_count(self, obj):
        count = obj.products.count()
        return format_html('<strong style="color: #0066cc;">{}</strong> products', count)
    product_count.short_description = 'Products'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text', 'is_main', 'order']
    ordering = ['order']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_display', 'year', 'condition_badge', 'status_badge', 'featured_badge', 'created_at']
    list_filter = ['status', 'condition', 'fuel_type', 'transmission', 'featured', 'created_at']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['id', 'created_at', 'updated_at', 'main_image_display']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'name', 'slug', 'category', 'description')
        }),
        ('Pricing & Status', {
            'fields': ('price', 'status', 'featured')
        }),
        ('Vehicle Details', {
            'fields': ('year', 'condition', 'mileage', 'transmission', 'fuel_type', 'color')
        }),
        ('Features', {
            'fields': ('has_ac', 'has_power_steering', 'has_abs', 'has_airbags', 'has_alloy_wheels'),
            'classes': ('collapse',)
        }),
        ('Main Image', {
            'fields': ('main_image_display',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['make_available', 'mark_as_sold', 'toggle_featured']

    def price_display(self, obj):
        formatted_price = f'₦{obj.price:,.2f}'
        return format_html('{}', formatted_price)
    price_display.short_description = 'Price'

    def condition_badge(self, obj):
        colors = {
            'brand_new': '#28a745',
            'tokunbo': '#ffc107',
            'nigerian_used': '#fd7e14',
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.condition, '#999'),
            obj.get_condition_display()
        )
    condition_badge.short_description = 'Condition'

    def status_badge(self, obj):
        colors = {
            'available': '#28a745',
            'sold': '#dc3545',
            'reserved': '#ffc107',
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, '#999'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def featured_badge(self, obj):
        if obj.featured:
            return format_html(
                '<span style="background-color: #ff6b6b; color: white; padding: 5px 10px; border-radius: 3px;">⭐ Featured</span>'
            )
        return '—'
    featured_badge.short_description = 'Featured'

    def main_image_display(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="max-width: 300px; height: auto;" />',
                obj.main_image.image.url
            )
        return 'No image'
    main_image_display.short_description = 'Main Image'

    def make_available(self, request, queryset):
        updated = queryset.update(status='available')
        self.message_user(request, f'{updated} products marked as available.')
    make_available.short_description = 'Mark selected products as Available'

    def mark_as_sold(self, request, queryset):
        updated = queryset.update(status='sold')
        self.message_user(request, f'{updated} products marked as Sold.')
    mark_as_sold.short_description = 'Mark selected products as Sold'

    def toggle_featured(self, request, queryset):
        for product in queryset:
            product.featured = not product.featured
            product.save()
        self.message_user(request, f'{queryset.count()} products featured status toggled.')
    toggle_featured.short_description = 'Toggle Featured Status'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_preview', 'is_main', 'order', 'created_at']
    list_filter = ['product', 'is_main', 'created_at']
    search_fields = ['product__name', 'alt_text']
    readonly_fields = ['id', 'created_at', 'image_preview']
    ordering = ['product', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 100px; height: auto;" />',
                obj.image.url
            )
        return 'No image'
    image_preview.short_description = 'Preview'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'rating_stars', 'verified_purchase_badge', 'created_at']
    list_filter = ['rating', 'verified_purchase', 'created_at']
    search_fields = ['name', 'email', 'product__name']
    readonly_fields = ['id', 'created_at']

    def rating_stars(self, obj):
        stars = '⭐' * obj.rating + '☆' * (5 - obj.rating)
        return format_html(
            '<span style="font-size: 16px;">{}</span>',
            stars
        )
    rating_stars.short_description = 'Rating'

    def verified_purchase_badge(self, obj):
        if obj.verified_purchase:
            return format_html('<span style="color: #28a745;">✓ Verified</span>')
        return '—'
    verified_purchase_badge.short_description = 'Verified'


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'status_badge', 'email', 'phone', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'phone', 'product__name', 'message']
    readonly_fields = ['id', 'created_at', 'updated_at']
    actions = ['mark_as_contacted', 'mark_as_resolved', 'mark_as_closed']

    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('product', 'message', 'status')
        }),
        ('Timestamps', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def status_badge(self, obj):
        colors = {
            'pending': '#ffc107',
            'contacted': '#0099ff',
            'resolved': '#28a745',
            'closed': '#6c757d',
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, '#999'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def mark_as_contacted(self, request, queryset):
        updated = queryset.update(status='contacted')
        self.message_user(request, f'{updated} inquiries marked as contacted.')
    mark_as_contacted.short_description = 'Mark as Contacted'

    def mark_as_resolved(self, request, queryset):
        updated = queryset.update(status='resolved')
        self.message_user(request, f'{updated} inquiries marked as resolved.')
    mark_as_resolved.short_description = 'Mark as Resolved'

    def mark_as_closed(self, request, queryset):
        updated = queryset.update(status='closed')
        self.message_user(request, f'{updated} inquiries marked as closed.')
    mark_as_closed.short_description = 'Mark as Closed'
