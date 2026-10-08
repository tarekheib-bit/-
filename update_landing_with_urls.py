#!/usr/bin/env python3
"""
Update clinic-ella-landing.html with Cloudinary URLs
Edit the CLOUDINARY_URLS dict below with your actual URLs
"""

CLOUDINARY_URLS = {
    'אווירה.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/אווירה.png',
    'אלה ברנע.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/אלה ברנע.png',
    'הצוות.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/הצוות.png',
    'חדר טיפולים.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/חדר טיפולים.png',
    'חזית הקליניקה.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/חזית הקליניקה.png',
    'חלל הקליניקה.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/חלל הקליניקה.png',
    'טיפול פנים.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/טיפול פנים.png',
    'מוצר.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/מוצר.png',
    'מוצרי טיפוח.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/מוצרי טיפוח.png',
    'עור לפני.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/עור לפני.png',
    'עור אחרי.png': 'https://res.cloudinary.com/your-cloud/image/upload/v123/clinic-ella/עור אחרי.png',
}

from pathlib import Path

html_file = Path('clinic-ella-landing.html')

if not html_file.exists():
    print(f"❌ {html_file} not found")
    exit(1)

content = html_file.read_text(encoding='utf-8')

# Count replacements
replacements = 0

for local_filename, cloudinary_url in CLOUDINARY_URLS.items():
    # Find the local path patterns and replace with Cloudinary URL
    local_paths = [
        f'LESSON6/Lesson-6-Clinic-Ella/01-מאורגן/שיווק-ומותג/תמונות קליניקה/{local_filename}',
        f'LESSON6\\Lesson-6-Clinic-Ella\\01-מאורגן\\שיווק-ומותג\\תמונות קליניקה\\{local_filename}',
    ]

    for local_path in local_paths:
        if local_path in content:
            content = content.replace(local_path, cloudinary_url)
            replacements += 1
            print(f"✅ Updated: {local_filename}")

# Save updated HTML
html_file.write_text(content, encoding='utf-8')
print(f"\n✨ Updated {replacements} image URLs in {html_file}")
print("Your landing page is now using Cloudinary!")
