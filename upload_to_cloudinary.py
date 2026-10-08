#!/usr/bin/env python3
"""
Upload Clinic Ella images to Cloudinary
Before running, set your Cloudinary credentials as environment variables:

Windows PowerShell:
$env:CLOUDINARY_URL = "cloudinary://api_key:api_secret@cloud_name"

Then run:
python upload_to_cloudinary.py
"""

import os
import sys
from pathlib import Path

try:
    import cloudinary
    import cloudinary.uploader
except ImportError:
    print("❌ cloudinary package not found. Install it with:")
    print("   pip install cloudinary")
    sys.exit(1)

# Configure Cloudinary with your credentials
# Set CLOUDINARY_URL environment variable or configure directly
if not os.environ.get('CLOUDINARY_URL'):
    print("❌ CLOUDINARY_URL not set!")
    print("\nSet it with:")
    print("PowerShell: $env:CLOUDINARY_URL = 'cloudinary://YOUR_API_KEY:YOUR_API_SECRET@YOUR_CLOUD_NAME'")
    print("Bash: export CLOUDINARY_URL='cloudinary://YOUR_API_KEY:YOUR_API_SECRET@YOUR_CLOUD_NAME'")
    print("\nFind your credentials at: https://cloudinary.com/console")
    sys.exit(1)

cloudinary.config(secure=True)

# Path to clinic images
images_dir = Path("LESSON6/Lesson-6-Clinic-Ella/01-מאורגן/שיווק-ומותג/תמונות קליניקה")

if not images_dir.exists():
    print(f"❌ Images directory not found: {images_dir}")
    sys.exit(1)

# Get all images
image_files = list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg"))

if not image_files:
    print(f"❌ No images found in {images_dir}")
    sys.exit(1)

print(f"📸 Found {len(image_files)} images to upload")
print("=" * 60)

uploaded_urls = []

for i, image_path in enumerate(image_files, 1):
    try:
        print(f"\n[{i}/{len(image_files)}] Uploading: {image_path.name}")

        response = cloudinary.uploader.upload(
            str(image_path),
            folder="clinic-ella",  # Upload to clinic-ella folder
            public_id=image_path.stem,  # Use filename without extension
            overwrite=True,
            resource_type="auto"
        )

        url = response['secure_url']
        uploaded_urls.append({
            'name': image_path.name,
            'url': url
        })

        print(f"   ✅ Success: {url}")

    except Exception as e:
        print(f"   ❌ Failed: {e}")

print("\n" + "=" * 60)
print(f"\n✨ Upload complete! {len(uploaded_urls)}/{len(image_files)} images uploaded")

if uploaded_urls:
    print("\n📋 URLs for your landing page:\n")

    # Create a mapping of common names
    name_map = {
        'אווירה': 'hero-image',
        'אלה ברנע': 'about-ella',
        'הצוות': 'team',
        'חדר טיפולים': 'treatment-room',
        'חזית הקליניקה': 'clinic-entrance',
        'חלל הקליניקה': 'clinic-space',
        'טיפול פנים': 'facial-treatment',
        'עור לפני': 'before',
        'עור אחרי': 'after'
    }

    for item in uploaded_urls:
        name = item['name'].replace('.png', '').replace('.jpg', '')
        key = name_map.get(name, name)
        print(f"{key}:")
        print(f"  {item['url']}\n")

    print("\n💡 Save these URLs and update your HTML image src attributes")

    # Save to a file for reference
    with open('cloudinary_urls.txt', 'w', encoding='utf-8') as f:
        for item in uploaded_urls:
            f.write(f"{item['name']}\n{item['url']}\n\n")

    print("   URLs saved to: cloudinary_urls.txt")
