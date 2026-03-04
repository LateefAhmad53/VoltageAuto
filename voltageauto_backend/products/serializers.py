from rest_framework import serializers
from .models import Category, Product, ProductImage, Review, Inquiry


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_main', 'order']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    main_image = serializers.SerializerMethodField()
    price = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'price', 'condition', 'year', 'main_image', 'featured', 'status']

    def get_main_image(self, obj):
        main_image = obj.main_image
        if main_image:
            return ProductImageSerializer(main_image).data
        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()
    price = serializers.CharField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description', 'price',
            'condition', 'year', 'mileage', 'transmission', 'fuel_type',
            'color', 'status', 'has_ac', 'has_power_steering', 'has_abs',
            'has_airbags', 'has_alloy_wheels', 'featured', 'images',
            'reviews', 'created_at', 'updated_at'
        ]

    def get_reviews(self, obj):
        reviews = obj.reviews.all()[:5]
        return ReviewSerializer(reviews, many=True).data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'rating', 'comment', 'verified_purchase', 'created_at']


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'product', 'name', 'email', 'phone', 'message', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
