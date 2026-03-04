from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
import uuid


class Category(models.Model):
    """Car category/model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Car product model"""
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
    ]

    CONDITION_CHOICES = [
        ('brand_new', 'Brand New'),
        ('tokunbo', 'Tokunbo (Foreign Used)'),
        ('nigerian_used', 'Nigerian Used'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='tokunbo')
    year = models.IntegerField(validators=[MinValueValidator(1900)])
    mileage = models.IntegerField(help_text="Mileage in kilometers", validators=[MinValueValidator(0)])
    transmission = models.CharField(max_length=50, choices=[
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ])
    fuel_type = models.CharField(max_length=50, choices=[
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
    ])
    color = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    
    # Features
    has_ac = models.BooleanField(default=True)
    has_power_steering = models.BooleanField(default=True)
    has_abs = models.BooleanField(default=True)
    has_airbags = models.BooleanField(default=True)
    has_alloy_wheels = models.BooleanField(default=True)
    
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.name} ({self.year})"

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    @property
    def main_image(self):
        return self.images.filter(is_main=True).first() or self.images.first()


class ProductImage(models.Model):
    """Product images"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    alt_text = models.CharField(max_length=300, blank=True)
    is_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Image for {self.product.name}"

    def save(self, *args, **kwargs):
        # Only one main image per product
        if self.is_main:
            ProductImage.objects.filter(product=self.product, is_main=True).exclude(pk=self.pk).update(is_main=False)
        super().save(*args, **kwargs)


class Review(models.Model):
    """Product reviews"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    verified_purchase = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.name} for {self.product.name}"


class Inquiry(models.Model):
    """Customer inquiries"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('contacted', 'Contacted'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='inquiries')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name} - {self.status}"
