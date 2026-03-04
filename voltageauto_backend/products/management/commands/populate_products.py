from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product, ProductImage
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populate database with sample car products'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Toyota', 'description': 'Premium Toyota vehicles'},
            {'name': 'Honda', 'description': 'Reliable Honda automobiles'},
            {'name': 'BMW', 'description': 'Luxury BMW models'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories[cat_data['name']] = cat
            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'{status}: Category {cat.name}'))

        # Create sample products
        products_data = [
            {
                'name': 'Toyota Camry 2023',
                'category': 'Toyota',
                'description': 'Sleek sedan with premium features and excellent fuel efficiency. Perfect for daily commuting and long drives.',
                'price': '45000000',
                'year': 2023,
                'mileage': 5000,
                'transmission': 'automatic',
                'fuel_type': 'petrol',
                'color': 'Silver',
                'condition': 'brand_new',
                'featured': True,
            },
            {
                'name': 'Honda Accord 2022',
                'category': 'Honda',
                'description': 'Stunning sedan with comfort and performance. Tokunbo with minimal mileage.',
                'price': '38000000',
                'year': 2022,
                'mileage': 15000,
                'transmission': 'automatic',
                'fuel_type': 'petrol',
                'color': 'Black',
                'condition': 'tokunbo',
                'featured': True,
            },
            {
                'name': 'BMW 3 Series 2021',
                'category': 'BMW',
                'description': 'Luxury sedan with state-of-the-art technology. Pristine condition.',
                'price': '55000000',
                'year': 2021,
                'mileage': 22000,
                'transmission': 'automatic',
                'fuel_type': 'diesel',
                'color': 'White',
                'condition': 'tokunbo',
                'featured': True,
            },
        ]

        media_path = Path(__file__).resolve().parent.parent.parent.parent / 'media' / 'products'
        media_path.mkdir(parents=True, exist_ok=True)

        for prod_data in products_data:
            category = categories[prod_data.pop('category')]
            slug = slugify(prod_data['name'])
            
            product, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    **prod_data,
                    'category': category,
                    'status': 'available',
                }
            )

            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f'{status}: Product {product.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))
