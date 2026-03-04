# Static Files Directory

## Logo Storage

**Add your logo here:**

1. Save your logo as `logo.jpg` in this folder: `voltageauto_backend/static/logo.jpg`
2. Recommended logo specifications:
   - **Format**: JPG, PNG, or WEBP
   - **Size**: 200x200px or 300x300px (square works best for circular display)
   - **File Size**: Under 500KB
   - **Background**: Transparent PNG or white background

3. The logo will automatically appear in the navbar on all pages
4. If no logo is found, the lightning bolt icon + "VoltageAuto" text will display instead

## Folder Structure

```
static/
├── logo.jpg              ← Put your logo here!
├── css/                  ← CSS files (if needed)
├── js/                   ← JavaScript files (if needed)
└── images/               ← Images (if needed)
```

## Usage in Production

When deploying to production:

```bash
# Collect all static files
python manage.py collectstatic --noinput
```

This will gather all static files including your logo into `staticfiles/` directory for serving.

## Note

- The logo is completely optional
- If logo.jpg doesn't exist, the default icon + text will show
- You can update the logo anytime by replacing the file
- No need to restart the server
