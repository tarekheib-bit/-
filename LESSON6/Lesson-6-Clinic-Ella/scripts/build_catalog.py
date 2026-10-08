#!/usr/bin/env python3
"""
Build Catalog Script - Index all files
Creates catalog.json with file metadata: path, type, size, hash, tentative category
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from collections import defaultdict

# File type mappings
FILE_EXTENSIONS = {
    # Accounting & Finance
    'xlsx': 'accounting', 'xls': 'accounting', 'csv': 'accounting',
    'pdf': 'accounting', 'txt': 'accounting',

    # Documents
    'docx': 'documents', 'doc': 'documents', 'pptx': 'documents', 'ppt': 'documents',

    # Images
    'jpg': 'images', 'jpeg': 'images', 'png': 'images', 'gif': 'images', 'bmp': 'images',

    # Brand & Marketing
    'zip': 'brand-kit',
}

def get_file_hash(filepath):
    """Calculate SHA256 hash of a file"""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            # Read in chunks to handle large files
            for chunk in iter(lambda: f.read(8192), b''):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"error: {str(e)}"

def categorize_file(filename, filepath):
    """Tentatively categorize a file based on extension and content hints"""
    # Get extension
    ext = Path(filename).suffix.lower().lstrip('.')

    # Check filename hints
    name_lower = filename.lower()

    # Accounting & Finance
    if any(x in name_lower for x in ['חשבונ', 'תשלום', 'הנהלה', 'בנק', 'הוצאה', 'הכנסה', 'שכר', 'תזרים', 'מחיר', 'חשבו']):
        return 'הנהלת-חשבונות'

    # Credit/Loans
    if any(x in name_lower for x in ['אשראי', 'הלוואה', 'כרטיס']):
        return 'בנקאות-ואשראי'

    # HR/Payroll
    if any(x in name_lower for x in ['שכר', 'עובד', 'צוות', 'העסקה', 'דו"ח כח אדם']):
        return 'שכר-ומשאבי-אנוש'

    # Sales/CRM
    if any(x in name_lower for x in ['לקוח', 'מכירה', 'חבילה', 'כרטסת', 'ספק', 'קשר']):
        return 'מכירות-ולקוחות-CRM'

    # Marketing & Branding
    if any(x in name_lower for x in ['לוגו', 'מיתוג', 'צבע', 'פונט', 'שיווק', 'קמפיין', 'פלייר', 'ניוזלטר', 'תמונה']):
        return 'שיווק-ומותג'

    # Operations/ERP
    if any(x in name_lower for x in ['מלאי', 'הנהלה', 'תהליך', 'נוהל', 'מפעיל']):
        return 'תפעול-ERP'

    # Legal & Contracts
    if any(x in name_lower for x in ['חוזה', 'הסכם', 'משפט', 'הסכמה', 'מדיניות', 'תנאים']):
        return 'משפטי-וחוזים'

    # Digital & Links
    if any(x in name_lower for x in ['קישור', 'אתר', 'דומיין', 'דיגיטל', 'אינטרנט']):
        return 'דיגיטל-ולינקים'

    # Reviews & testimonials
    if any(x in name_lower for x in ['ביקור', 'דירוג', 'המלצה', 'ביקורת']):
        return 'תקשורת-וביקורות'

    # Use extension-based category if no hints found
    if ext in FILE_EXTENSIONS:
        return FILE_EXTENSIONS[ext]

    return 'לא-מסווג'

def build_catalog(archive_root):
    """Build the catalog of all files"""
    backup_dir = os.path.join(archive_root, "00-מקור-גולמי")
    ai_ready_dir = os.path.join(archive_root, "02-AI-ready")

    # Create AI-ready directory
    os.makedirs(ai_ready_dir, exist_ok=True)

    catalog = {
        "metadata": {
            "archive_root": archive_root,
            "created": str(Path.cwd()),
            "total_files": 0,
            "categories": {}
        },
        "files": []
    }

    category_counts = defaultdict(int)
    duplicate_groups = defaultdict(list)
    file_type_counts = defaultdict(int)

    # Walk through backup directory
    if os.path.exists(backup_dir):
        for root, dirs, files in os.walk(backup_dir):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    # Get file stats
                    stat = os.stat(filepath)
                    file_hash = get_file_hash(filepath)

                    # Get relative path
                    rel_path = os.path.relpath(filepath, backup_dir)

                    # Categorize
                    category = categorize_file(file, filepath)

                    # Get extension
                    ext = Path(file).suffix.lower().lstrip('.')

                    # Create file entry
                    entry = {
                        "path": rel_path,
                        "filename": file,
                        "size": stat.st_size,
                        "hash": file_hash,
                        "category": category,
                        "type": ext if ext else "no-extension"
                    }

                    catalog["files"].append(entry)
                    category_counts[category] += 1
                    file_type_counts[ext] += 1

                    # Track duplicates
                    duplicate_groups[file_hash].append(rel_path)

                except Exception as e:
                    print(f"Warning: Could not process {filepath}: {e}")

    catalog["metadata"]["total_files"] = len(catalog["files"])
    catalog["metadata"]["categories"] = dict(category_counts)

    # Write catalog.json
    catalog_path = os.path.join(ai_ready_dir, "catalog.json")
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "="*60)
    print("📋 CATALOG SUMMARY")
    print("="*60)
    print(f"Total files: {len(catalog['files'])}")
    print(f"\nCategories:")
    for category, count in sorted(category_counts.items()):
        status = "✓" if category != "לא-מסווג" else "?"
        print(f"  {status} {category}: {count}")

    print(f"\nFile types:")
    for ext, count in sorted(file_type_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  .{ext}: {count}")

    # List duplicates
    duplicates = {k: v for k, v in duplicate_groups.items() if len(v) > 1}
    if duplicates:
        print(f"\nDuplicate files (by content hash):")
        for file_hash, paths in sorted(duplicates.items())[:5]:
            print(f"  {file_hash[:8]}...")
            for path in paths[:2]:
                print(f"    - {path}")
            if len(paths) > 2:
                print(f"    ... and {len(paths) - 2} more")

    print(f"\n✓ Catalog saved to: {catalog_path}")
    print("="*60)

    return catalog_path

if __name__ == "__main__":
    archive_root = sys.argv[1] if len(sys.argv) > 1 else "."
    build_catalog(archive_root)
