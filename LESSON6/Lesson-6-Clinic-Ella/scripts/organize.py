#!/usr/bin/env python3
"""
Organize Script - Sort files by category
Copies files from 00-מקור-גולמי/ into 01-מאורגן/ based on catalog.json
"""

import os
import sys
import json
import shutil
from pathlib import Path
from collections import defaultdict

def organize_files(archive_root):
    """
    Read catalog.json and organize files into 01-מאורגן/
    respecting the category assignments
    """
    backup_dir = os.path.join(archive_root, "00-מקור-גולמי")
    organized_dir = os.path.join(archive_root, "01-מאורגן")
    catalog_path = os.path.join(archive_root, "02-AI-ready", "catalog.json")

    # Load catalog
    if not os.path.exists(catalog_path):
        print(f"Error: Catalog not found at {catalog_path}")
        print("Run build_catalog.py first")
        sys.exit(1)

    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Create organized directory
    os.makedirs(organized_dir, exist_ok=True)

    # Group files by category
    files_by_category = defaultdict(list)
    for entry in catalog["files"]:
        category = entry["category"]
        files_by_category[category].append(entry)

    # Copy files to organized directories
    print("\n" + "="*60)
    print("📂 ORGANIZING FILES")
    print("="*60)

    total_copied = 0
    for category in sorted(files_by_category.keys()):
        category_dir = os.path.join(organized_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        files = files_by_category[category]
        print(f"\n{category}: ({len(files)} files)")

        for entry in files:
            try:
                source_path = os.path.join(backup_dir, entry["path"])

                # Create subdirectories in organized folder
                dest_rel_path = entry["path"]
                dest_path = os.path.join(category_dir, Path(dest_rel_path).name)

                # Create parent directory if needed
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Copy file
                if os.path.exists(source_path):
                    shutil.copy2(source_path, dest_path)
                    total_copied += 1
                    print(f"  ✓ {Path(dest_rel_path).name}")
                else:
                    print(f"  ✗ Not found: {entry['path']}")

            except Exception as e:
                print(f"  ✗ Error copying {entry['path']}: {e}")

    print(f"\n✓ Organization complete!")
    print(f"  Total files copied: {total_copied}")
    print(f"  Organized directory: {organized_dir}")
    print("="*60)

if __name__ == "__main__":
    archive_root = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_files(archive_root)
