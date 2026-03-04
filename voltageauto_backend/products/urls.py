from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, InquiryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'inquiries', InquiryViewSet, basename='inquiry')

urlpatterns = [
    path('', include(router.urls)),
]
