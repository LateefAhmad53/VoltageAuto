from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Review, Inquiry
from .serializers import (
    CategorySerializer, ProductListSerializer, ProductDetailSerializer,
    ReviewSerializer, InquirySerializer, ProductImageSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve product categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for products
    List, Create, Retrieve, Update, Delete products
    """
    queryset = Product.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'condition', 'fuel_type', 'transmission', 'featured']
    search_fields = ['name', 'description', 'color']
    ordering_fields = ['price', 'year', 'created_at']
    ordering = ['-created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('images', 'reviews')
        if self.request.user.is_staff:
            return queryset
        return queryset.exclude(status='sold')

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured products"""
        products = self.get_queryset().filter(featured=True)[:8]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get latest products"""
        products = self.get_queryset()[:12]
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def related(self, request, slug=None):
        """Get related products"""
        product = self.get_object()
        related = self.get_queryset().filter(
            category=product.category
        ).exclude(id=product.id)[:6]
        serializer = ProductListSerializer(related, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def add_image(self, request, slug=None):
        """Add image to product"""
        product = self.get_object()
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def add_review(self, request, slug=None):
        """Add review to product"""
        product = self.get_object()
        data = request.data.copy()
        data['product'] = product.id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Manage product reviews
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_slug = self.request.query_params.get('product', None)
        if product_slug:
            return Review.objects.filter(product__slug=product_slug)
        return Review.objects.all()


class InquiryViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for customer inquiries
    """
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        return Inquiry.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def pending(self, request):
        """Get pending inquiries (staff only)"""
        if not request.user.is_staff:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        inquiries = Inquiry.objects.filter(status='pending')
        serializer = InquirySerializer(inquiries, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        """Update inquiry status (staff only)"""
        if not request.user.is_staff:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        inquiry = self.get_object()
        inquiry.status = request.data.get('status', inquiry.status)
        inquiry.save()
        serializer = InquirySerializer(inquiry)
        return Response(serializer.data)
