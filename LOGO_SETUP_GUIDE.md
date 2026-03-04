# 🎨 LOGO SETUP - COMPLETE GUIDE

## Where to Place Your Logo

Your VoltageAuto logo will appear on **EVERY PAGE** in the top-left corner of the navigation bar.

### 📍 Exact Location

```
voltageauto_backend/
└── products/
    └── static/
        └── products/
            └── images/
                └── logo.jpg  ← PLACE YOUR LOGO HERE
```

### 📂 Full Path
```
c:\Users\user\Desktop\VoltageAuto\voltageauto_backend\products\static\products\images\logo.jpg
```

---

## 📸 Logo Requirements

| Requirement | Details |
|-------------|---------|
| **Format** | JPG, PNG, or GIF |
| **File Name** | `logo.jpg` (or logo.png / logo.gif) |
| **Recommended Size** | 200x50px to 300x80px |
| **Max File Size** | 100KB |
| **Aspect Ratio** | Wide/landscape (horizontal works best) |
| **Color** | White background recommended for navbar |

---

## 🚀 How to Add Your Logo

### Step 1: Prepare Your Logo
- Create or export your logo file (JPG, PNG, or GIF)
- Recommended dimensions: 250x60px
- File size: Keep under 100KB
- Transparent background (PNG) works best

### Step 2: Place the File
Navigate to this folder:
```
voltageauto_backend/products/static/products/images/
```

Copy your logo file here and name it one of:
- `logo.jpg` (recommended)
- `logo.png`
- `logo.gif`

### Step 3: Restart Server
```bash
# Stop current server (Ctrl+C)
# Then restart:
python manage.py runserver
```

### Step 4: Verify
- Visit http://localhost:8000
- Check the navbar - your logo should appear!
- It will also appear on:
  - http://localhost:8000/products/
  - http://localhost:8000/products/{product-slug}/
  - http://localhost:8000/admin/

---

## 🔄 How It Works

The navbar template automatically looks for your logo:

```html
<img src="/static/products/images/logo.jpg" 
     onerror="this.style.display='none'">
```

If the file exists → **Logo displays**
If the file doesn't exist → **Shows fallback (lightning bolt icon + text)**

---

## 📐 Logo Design Tips

### Best Practices
✅ Use simple, clean designs
✅ Keep it wide/landscape
✅ Ensure it's readable at small sizes
✅ Use white or transparent background
✅ Avoid text that's too small
✅ Keep brand colors consistent

### What to Avoid
❌ Very tall/narrow logos
❌ Complex details (won't show well small)
❌ Text that's hard to read
❌ Very large file sizes
❌ Colors that don't contrast with navbar

---

## 🎨 Logo Examples

### Good Logo Sizes:
- 250x60px
- 300x75px
- 280x70px
- 200x50px

### Example Structure:
```
My Company Logo (Text)     ← Should be readable
[================]         ← Wide format
50-60px height
```

---

## 🔗 Multiple Logo Formats

You can add multiple formats if needed:

```
images/
├── logo.jpg        ← Main (recommended)
├── logo.png        ← Backup
└── logo.gif        ← Alternative
```

The system will look for `logo.jpg` first.

---

## 💾 File Management

### If You Want to Change Logo:
1. Open: `voltageauto_backend/products/static/products/images/`
2. Delete the old `logo.jpg`
3. Add your new `logo.jpg`
4. Refresh browser (Ctrl+Shift+R for hard refresh)

### If You Want to Remove Logo:
1. Delete `logo.jpg`
2. Server will automatically show fallback icon + text
3. No code changes needed!

---

## 🖥️ On Different Pages

Your logo will automatically display on:

| Page | URL | Logo Position |
|------|-----|---------------|
| **Home** | http://localhost:8000 | Navbar top-left |
| **Products** | http://localhost:8000/products/ | Navbar top-left |
| **Product Detail** | http://localhost:8000/products/{slug}/ | Navbar top-left |
| **Admin** | http://localhost:8000/admin | May vary |

---

## 🔧 Troubleshooting

### Logo Not Showing?

**Solution 1: Hard Refresh**
```
Press: Ctrl + Shift + R (Windows/Linux)
Or: Cmd + Shift + R (Mac)
```

**Solution 2: Check File Path**
Ensure file is in exactly:
```
voltageauto_backend/products/static/products/images/
```

**Solution 3: Check File Name**
Ensure filename is exactly:
```
logo.jpg  (lowercase .jpg)
```

**Solution 4: Restart Server**
```bash
# Stop server (Ctrl+C)
python manage.py runserver
```

**Solution 5: Check File Size**
Ensure it's a valid image file:
- Not corrupted
- Under 100KB
- Correct format (JPG/PNG/GIF)

---

## 📱 Responsive Logo

The logo will automatically:
- Scale down on mobile
- Maintain aspect ratio
- Stay readable at all sizes
- Never push other navbar items off-screen

### Current CSS:
```css
style="height: 40px; max-width: 150px; object-fit: contain;"
```

This ensures:
- Maximum height: 40px
- Maximum width: 150px
- Maintains aspect ratio
- Responsive on mobile

---

## 🎯 After Adding Logo

### What's Next?
1. ✅ Logo added
2. ⬜ Start server
3. ⬜ Add products
4. ⬜ Upload product images
5. ⬜ Test website
6. ⬜ Deploy to production

---

## 💡 Pro Tips

1. **Brand Consistency**
   - Use your official company logo
   - Maintain brand colors
   - Keep font consistent

2. **File Optimization**
   - Use TinyPNG or similar to compress
   - Saves server bandwidth
   - Faster loading times

3. **Multiple Versions**
   - Keep original file backed up
   - Have light and dark versions if needed
   - Test on different backgrounds

4. **Testing**
   - Test on mobile and desktop
   - Check on different browsers
   - Verify contrast and readability

---

## 📞 Quick Reference

| Task | Action |
|------|--------|
| **Add Logo** | Copy to `products/static/products/images/logo.jpg` |
| **Change Logo** | Replace the file with new one |
| **Remove Logo** | Delete the file |
| **View on Site** | Visit http://localhost:8000 |
| **Hard Refresh** | Ctrl+Shift+R (Chrome/Firefox/Edge) |
| **Restart Server** | Ctrl+C then `python manage.py runserver` |

---

## ✅ Checklist

- [ ] Logo file created/prepared
- [ ] File is JPG/PNG/GIF format
- [ ] File is named `logo.jpg` (or .png/.gif)
- [ ] File is less than 100KB
- [ ] Copied to: `voltageauto_backend/products/static/products/images/`
- [ ] Server restarted
- [ ] Logo appears on http://localhost:8000
- [ ] Logo looks good on mobile
- [ ] Logo looks good on desktop

---

**Your logo will appear instantly once you place it in the correct folder!**

For any issues, see the troubleshooting section above. 🚀
