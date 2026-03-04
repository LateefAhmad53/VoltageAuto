# Logo Storage

## Where to Place Your Logo

Place your `logo.jpg` file in this directory:

```
voltageauto_backend/
└── products/
    └── static/
        └── products/
            └── images/
                └── logo.jpg  ← Place it HERE
```

## How It Works

1. **Save your logo** as `logo.jpg` (or `.png`, `.gif`)
2. **Place it** in this exact folder (`products/static/products/images/`)
3. **The logo will automatically appear** on all pages:
   - Homepage
   - Products listing
   - Product details
   - Navigation bar

## Logo Requirements

- **Format**: JPG, PNG, or GIF
- **Recommended Size**: 200x50px to 300x80px
- **Recommended File Size**: Under 100KB
- **Aspect Ratio**: Keep it wide (landscape format works best)

## Example

If your logo file is named `logo.jpg`, it will be served from:
```
/static/products/images/logo.jpg
```

And will display in the navbar on all pages!

## Dynamic Logo Loading

The templates include automatic logo detection. If `logo.jpg` exists, it will:
- Show on the navbar
- Appear as a clickable link to homepage
- Scale responsively on mobile devices

If the file doesn't exist, a fallback text logo appears instead.
