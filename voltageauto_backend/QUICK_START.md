# 🚀 Quick Start Guide - VoltageAuto

## First Time Setup (Choose One)

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
cd voltageauto_backend
setup.bat
```

**macOS/Linux:**
```bash
cd voltageauto_backend
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

```bash
# 1. Navigate to backend folder
cd voltageauto_backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create database
python manage.py migrate

# 6. Create admin account
python manage.py createsuperuser
# Follow prompts (username, email, password)

# 7. (Optional) Populate sample data
python manage.py populate_products

# 8. Start server
python manage.py runserver
```

## Access the Application

Once the server is running:

- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin (login with superuser credentials)
- **API**: http://localhost:8000/api/

## First Steps

1. **Login to Admin Panel**
   - Go to http://localhost:8000/admin
   - Use your superuser credentials

2. **Add Products**
   - Click "Products" → "Add Product"
   - Fill in car details
   - Upload images (click "Add another image" for multiple)
   - Set one image as "main image" (checkbox)
   - Save

3. **Manage Categories**
   - Pre-populated with: Toyota, Honda, BMW
   - Add more as needed

4. **View on Frontend**
   - Go to http://localhost:8000
   - See products on home page and /products/ page

## Common Commands

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Populate sample data
python manage.py populate_products

# Collect static files (production)
python manage.py collectstatic --noinput

# Access Django shell
python manage.py shell

# Run tests
python manage.py test
```

## Adding Your Images

### Option A: Via Admin Panel (Easiest)
1. Add product → Scroll to "Images" section
2. Upload images one by one
3. Click "Add another image" for multiple
4. Click checkbox for main image
5. Save

### Option B: Copy Images Directory
1. Copy your `voltage/images` folder contents
2. Paste into `voltageauto_backend/media/products/`
3. In admin, create products and link images

## Important Folders

```
voltageauto_backend/
├── media/              ← Uploaded images go here
├── staticfiles/        ← Static files (CSS, JS)
├── db.sqlite3          ← Database file
├── manage.py           ← Django management
└── products/           ← Main app code
```

## API Quick Reference

### Get Featured Products
```
GET http://localhost:8000/api/products/featured/
```

### Get All Products with Filters
```
GET http://localhost:8000/api/products/?condition=brand_new&fuel_type=petrol&ordering=-price
```

### Get Product Details
```
GET http://localhost:8000/api/products/{slug}/
```

### Create Inquiry
```
POST http://localhost:8000/api/inquiries/
Body: {
  "product": "product-uuid",
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+2341234567890",
  "message": "Interested in this car"
}
```

## Troubleshooting

### Port 8000 already in use
```bash
python manage.py runserver 8001
# Use a different port
```

### Images not showing
```bash
python manage.py collectstatic --noinput
# Check that MEDIA_URL and MEDIA_ROOT are correct in settings.py
```

### Database errors
```bash
# Delete db.sqlite3 and start fresh (WARNING: loses all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Module not found error
```bash
# Reactivate virtual environment and reinstall
pip install -r requirements.txt
```

## Next Steps

1. ✅ Set up the platform
2. 📸 Add your car inventory
3. 🎨 Customize colors/branding in templates
4. 📧 Configure email for inquiries
5. 🚀 Deploy to production

## Support

For questions or issues:
- Check README.md for detailed documentation
- Review Django admin interface for data management
- Check console for error messages

Happy selling! 🎉
