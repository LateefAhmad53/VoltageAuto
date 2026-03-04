from django.urls import path
from .views_templates import HomeView, ProductListView, ProductDetailView, ContactView, ServicesView, AffiliateView

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
        path('services/', ServicesView.as_view(), name='services'),
        path('affiliate/', AffiliateView.as_view(), name='affiliate'),
]

