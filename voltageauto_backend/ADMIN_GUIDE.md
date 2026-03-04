# 👨‍💼 Admin Panel Guide - VoltageAuto

A complete guide to managing your car dealership through the Django admin panel.

## Accessing the Admin Panel

**URL:** http://localhost:8000/admin

**Login:** Use your superuser credentials (created during setup)

## Dashboard Overview

The admin dashboard shows:
- **Recently added products**
- **Pending inquiries**
- **Quick stats**
- **App shortcuts**

## Managing Products

### Adding a New Product

1. Click **"Products"** in the left menu
2. Click **"Add Product"** (top right)
3. Fill in the following information:

#### Basic Information
- **Name**: Car model (e.g., "Toyota Camry 2023")
- **Slug**: Auto-generated URL-friendly name
- **Category**: Select from existing categories or create new
- **Description**: Detailed description of the vehicle

#### Pricing & Status
- **Price**: In Nigerian Naira (₦)
- **Status**: 
  - Available (car is for sale)
  - Sold (car has been sold)
  - Reserved (car is being negotiated)
- **Featured**: Check to show on homepage

#### Vehicle Details
- **Year**: Manufacturing year
- **Condition**:
  - Brand New (0 miles)
  - Tokunbo (Foreign used with low mileage)
  - Nigerian Used (Locally used)
- **Mileage**: Total kilometers on odometer
- **Transmission**:
  - Manual
  - Automatic
- **Fuel Type**:
  - Petrol
  - Diesel
  - Hybrid
  - Electric
- **Color**: Vehicle color

#### Features (Collapsible Section)
Check the features your vehicle has:
- ✓ Air Conditioning
- ✓ Power Steering
- ✓ ABS Brakes
- ✓ Airbags
- ✓ Alloy Wheels

#### Adding Images
1. Scroll to **"Images"** section
2. Click **"Add another image"** button
3. **Upload**: Click "Choose file" to select image
4. **Alt Text**: Describe the image (for SEO & accessibility)
5. **Is Main**: ✓ Check this box to set as the product's main image
6. **Order**: Number to control image order in gallery

**Important:** Only ONE image can be marked as "Is Main". This image appears on:
- Product listing page
- Featured products section
- Related products cards

4. Click **"SAVE"** button at bottom right

### Editing a Product

1. Go to **Products**
2. Click the product name or edit button
3. Make changes
4. Click **"SAVE"**

### Deleting a Product

1. Go to **Products**
2. Select product checkbox
3. Choose action: **"Delete selected products"**
4. Click **"Go"**

### Bulk Actions

Select multiple products and perform actions:

- **Mark as Available**: Set status to available
- **Mark as Sold**: Set status to sold
- **Toggle Featured Status**: Add/remove from homepage

### Filtering Products

Use the right sidebar filters:

- **Status**: Filter by Available, Sold, or Reserved
- **Condition**: Filter by Brand New, Tokunbo, Nigerian Used
- **Fuel Type**: Filter by fuel type
- **Transmission**: Filter by manual or automatic
- **Featured**: Show only featured products
- **Date**: Filter by date created

### Searching Products

Use the search box to find:
- Product name
- Product slug
- Description keywords
- Color

## Managing Categories

### Adding a Category

1. Click **"Categories"** in the left menu
2. Click **"Add Category"**
3. Fill in:
   - **Name**: Category name (e.g., "Toyota")
   - **Slug**: Auto-generated, can be customized
   - **Description**: About this category
4. Click **"SAVE"**

### Viewing Category Info

- Shows the number of products in category
- Shows creation date
- Easy filtering of products by category

## Managing Inquiries

### Viewing Inquiries

1. Click **"Inquiries"** in the left menu
2. See all customer inquiries with:
   - Customer name
   - Associated product
   - Status (Pending, Contacted, Resolved, Closed)
   - Email and phone
   - Date created

### Responding to Inquiries

1. Click on an inquiry to view details
2. See:
   - Customer's full name
   - Email address
   - Phone number
   - Product they inquired about
   - Message they sent
   - Current status

3. Update **Status**:
   - **Pending**: New inquiry, not yet contacted
   - **Contacted**: You've reached out to customer
   - **Resolved**: Deal made or inquiry satisfied
   - **Closed**: No longer pursuing

4. Click **"SAVE"**

### Bulk Inquiry Actions

1. Select multiple inquiries
2. Choose action:
   - Mark as Contacted
   - Mark as Resolved
   - Mark as Closed
3. Click **"Go"**

## Managing Reviews

### Viewing Reviews

1. Click **"Reviews"** in the left menu
2. See all customer reviews with:
   - Customer name
   - Product reviewed
   - Star rating (⭐)
   - If purchase is verified
   - Date posted

### Filtering Reviews

- **Product**: Filter by which car
- **Rating**: Filter by star rating
- **Verified Purchase**: Show only verified buyers

### Moderating Reviews

Reviews are typically auto-approved. To delete inappropriate reviews:

1. Click review
2. Click **"DELETE"** button
3. Confirm deletion

## Managing Images

### Viewing All Product Images

1. Click **"Product Images"** in the left menu
2. See all uploaded images with:
   - Thumbnail preview
   - Associated product
   - If it's the main image
   - Upload date

### Reordering Images

1. Click on image
2. Change the **"Order"** number (lower = earlier in gallery)
3. Click **"SAVE"**

### Deleting Images

1. Select image(s)
2. Choose action: **"Delete selected product images"**
3. Click **"Go"**

## Best Practices

### Product Data Entry
- ✅ Use clear, descriptive names
- ✅ Include all relevant specifications
- ✅ Upload high-quality images (optimize first)
- ✅ Write honest descriptions
- ✅ Set ONE main image for consistency
- ✅ Order images logically (exterior, interior, details)

### Image Management
- ✅ Compress images before uploading (smaller = faster load)
- ✅ Use descriptive alt text (helps SEO)
- ✅ Upload at least 3 photos per vehicle
- ✅ Include: exterior, interior, engine, details
- ✅ Set a clear main image for gallery

### Pricing
- ✅ Keep prices competitive
- ✅ Update regularly based on market
- ✅ Mark as Sold when sold
- ✅ Use Reserve status during negotiations

### Customer Service
- ✅ Respond to inquiries quickly
- ✅ Update status regularly
- ✅ Keep customer information private
- ✅ Provide honest information

## Useful Features

### Search & Filter
- Quickly find products
- Filter by multiple criteria
- Find specific inquiries

### Admin Actions
- Bulk edit status
- Bulk delete products
- Toggle featured status
- Mark inquiries as contacted

### Date Filtering
- See recently added products
- See recent inquiries
- Sort by date

## Keyboard Shortcuts

- **Tab**: Navigate between fields
- **Alt + S**: Save form
- **Alt + D**: Delete form
- **Ctrl/Cmd + Click**: Select multiple items

## Common Tasks

### Task: Feature a Product on Homepage

1. Go to **Products**
2. Click product name
3. Check **"Featured"** checkbox
4. Click **"SAVE"**
5. Product now shows on homepage

### Task: Mark Car as Sold

1. Go to **Products**
2. Select product
3. Choose action: **"Mark as Sold"**
4. Click **"Go"**
5. Status changes to "Sold" (won't show in listings)

### Task: Add Multiple Images

1. Go to **Products** → Select product
2. Scroll to **"Images"** section
3. Click **"Add another image"** 
4. Upload first image → Click "Add another image"
5. Upload second image → Continue...
6. For last image, just click **"SAVE"**

### Task: Respond to Customer Inquiry

1. Go to **Inquiries**
2. Click on inquiry
3. Read customer message
4. **Contact customer** using email/phone provided
5. Change status to **"Contacted"**
6. Click **"SAVE"**
7. After resolving, change to **"Resolved"**

### Task: Update Product Details

1. Go to **Products**
2. Click product name
3. Edit fields (price, status, mileage, etc.)
4. Click **"SAVE"**

## Customization

### Change Dashboard Title
In `settings.py`, change:
```python
admin.site.site_header = "Your Company Name"
```

### Add More Categories
1. Go to **Categories**
2. Click **"Add Category"**
3. Enter name and description
4. Click **"SAVE"**

### Change Color Scheme
Edit the admin CSS in your template overrides (advanced)

## Troubleshooting

### Can't Upload Images
- Check file size (recommend < 2MB)
- Use common formats: JPG, PNG
- Check file permissions
- Try different browser

### Product Not Appearing on Site
- Check **Status** is "Available"
- Make sure product is **saved**
- Clear browser cache
- Check featured products count

### Images Not Showing on Frontend
- Check image file exists in media folder
- Verify file permissions
- Run `python manage.py collectstatic`
- Check browser console for errors

### Lost Superuser Password
```bash
python manage.py changepassword username
```

## Support

For issues:
1. Check this guide
2. Review Django admin help (click ?)
3. Check README.md
4. Check console for error messages

---

**Last Updated:** 2025
**Version:** 1.0.0
