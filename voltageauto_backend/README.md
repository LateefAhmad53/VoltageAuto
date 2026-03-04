# VoltageAuto - Complete E-Commerce Platform

A modern, full-featured Django-powered e-commerce platform for buying and selling premium vehicles in Nigeria.

## Features

### Frontend
- ✨ Modern, responsive UI with smooth animations
- 🎨 Beautiful gradient design with purple theme
- 📱 Mobile-first responsive design
- 🔍 Advanced product filtering and search
- 📸 Image gallery with thumbnails
- ⭐ Featured products showcase
- 💬 Inquiry system for customer engagement

### Backend
- 🗄️ Robust Django REST API
- 📦 Complete CRUD operations for products
- 🖼️ Product image management
- 📋 Category system for organization
- ⭐ Product ratings and reviews
- 📧 Customer inquiry system
- 🔐 Secure admin panel
- 📊 Advanced filtering and search capabilities

### Admin Panel
- 🎯 Intuitive product management
- 🖼️ Inline image uploads
- 🏆 Featured product management
- 📊 Status tracking (Available, Sold, Reserved)
- 📈 Inquiry management
- 👤 User-friendly dashboard with color-coded badges
- 🔔 Bulk actions for efficient management

## Project Structure

```
voltageauto_backend/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── media/
│   └── products/
├── staticfiles/
├── voltageauto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── products/
    ├── migrations/
    ├── management/
    │   └── commands/
    │       └── populate_products.py
    ├── templates/
    │   └── products/
    │       ├── index.html
    │       ├── products.html
    │       └── detail.html
    ├── static/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── urls_templates.py
    ├── views.py
    └── views_templates.py
├── templates/
│   └── base.html
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Follow the prompts to create your admin account

# Populate sample products
python manage.py populate_products
```

### 4. Copy Existing Images

The existing images from your `voltage/images` folder should be copied to the `media/products/` directory. You can do this manually or create a script to automate the process.

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit:
- **Frontend**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API Documentation**: http://localhost:8000/api/

## API Endpoints

### Products
- `GET /api/products/` - List all products with pagination
- `GET /api/products/{slug}/` - Get product details
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/latest/` - Get latest products
- `GET /api/products/{slug}/related/` - Get related products
- `POST /api/products/` - Create new product (admin only)
- `PUT /api/products/{slug}/` - Update product (admin only)
- `DELETE /api/products/{slug}/` - Delete product (admin only)

### Filtering & Search
- `?search=query` - Search by name, description, color
- `?condition=brand_new` - Filter by condition
- `?fuel_type=petrol` - Filter by fuel type
- `?ordering=-price` - Sort by price (descending)
- `?featured=true` - Get featured products

### Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{slug}/` - Get category details

### Reviews
- `GET /api/reviews/` - List all reviews
- `GET /api/reviews/?product={slug}` - Get reviews for specific product
- `POST /api/reviews/` - Create review

### Inquiries
- `GET /api/inquiries/` - List inquiries
- `POST /api/inquiries/` - Create new inquiry
- `GET /api/inquiries/pending/` - Get pending inquiries (staff only)
- `POST /api/inquiries/{id}/update_status/` - Update inquiry status (staff only)

## Frontend Pages

### Home Page (`/`)
- Featured products showcase
- Latest vehicles
- Features section
- Call-to-action buttons

### Products Listing (`/products/`)
- Grid layout with product cards
- Advanced filtering (condition, fuel type)
- Search functionality
- Pagination
- Sort options

### Product Detail (`/products/{slug}/`)
- High-resolution image gallery
- Complete specifications
- Feature list
- Customer reviews
- Related products
- Inquiry form

## Admin Panel Features

### Product Management
1. **Add/Edit Products**
   - Complete product information
   - Multiple image uploads
   - Feature management
   - Status tracking

2. **Bulk Actions**
   - Mark as available
   - Mark as sold
   - Toggle featured status

3. **Image Management**
   - Drag-and-drop uploads
   - Set main image
   - Preview thumbnails
   - Organize with order field

4. **Status Tracking**
   - Available
   - Sold
   - Reserved

### Inquiry Management
- View all customer inquiries
- Filter by status
- Update inquiry status
- Contact information tracking

## Models

### Product
- UUID primary key
- Category relationship
- Basic info (name, description, price)
- Vehicle details (year, mileage, transmission, fuel type)
- Features (AC, power steering, ABS, airbags, alloy wheels)
- Status tracking
- Featured flag
- Timestamps

### ProductImage
- Association with products
- Multiple images per product
- Main image designation
- Alt text for accessibility
- Order field for sorting

### Category
- Product categorization
- Name and slug
- Description

### Review
- Customer reviews with ratings
- Verified purchase tracking
- Comment system

### Inquiry
- Customer contact information
- Product inquiry tracking
- Status management

## Customization

### Adding Products via Admin
1. Login to admin: http://localhost:8000/admin
2. Click "Products"
3. Click "Add Product"
4. Fill in product details
5. Upload images (click "Add another image" for multiple)
6. Set one image as "main image"
7. Save

### Connecting Existing Images
To automatically link your existing `voltage/images` to products:

```python
# Copy images to media directory first
# Then create ProductImage records in admin
```

### Styling
All CSS is contained in the templates for easy customization. You can:
- Change the gradient colors (currently purple #667eea to #764ba2)
- Modify animations in the style blocks
- Adjust spacing and layout with CSS grid/flexbox

## Environment Variables

Create a `.env` file for production settings:

```env
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/voltageauto
```

Load with `python-decouple`:

```python
from decouple import config
DEBUG = config('DEBUG', default=True, cast=bool)
```

## Deployment

### Using Gunicorn & Nginx

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn voltageauto.wsgi:application --bind 0.0.0.0:8000
```

### Static Files Collection

```bash
python manage.py collectstatic --noinput
```

### Database
For production, use PostgreSQL:

```bash
pip install psycopg2-binary
```

Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'voltageauto',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Performance Tips

1. **Image Optimization**: Compress images before uploading
2. **Caching**: Add Redis caching for product listings
3. **CDN**: Use a CDN for static files and images
4. **Database**: Index frequently searched fields
5. **API Pagination**: Results are limited to 12 per page

## Security

- ✅ CSRF protection enabled
- ✅ SQL injection prevention (Django ORM)
- ✅ XSS protection
- ✅ Secure password storage
- ✅ Admin authentication required
- ✅ CORS configuration for cross-domain requests

## Troubleshooting

### Images not showing
```bash
python manage.py collectstatic --noinput
# Check MEDIA_ROOT and MEDIA_URL in settings.py
```

### Database errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Admin not accessible
```bash
python manage.py createsuperuser
```

## Support & Contact

For issues or questions:
- Email: info@voltageauto.com
- Phone: +234 915 0729116

## License

© 2025 VoltageAuto Services. All rights reserved.

## Changelog

### Version 1.0.0 (Initial Release)
- Complete Django backend
- RESTful API
- Modern responsive frontend
- Admin panel
- Product management
- Inquiry system
- Review system
