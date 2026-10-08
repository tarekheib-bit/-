#!/usr/bin/env python3
"""
Archive Backup Script - Preserve the originals
Copies the entire source tree into 00-מקור-גולמי/ and makes it read-only
"""

import os
import sys
import shutil
import hashlib
from pathlib import Path
from datetime import datetime

def get_directory_hash(root_path):
    """Calculate a hash of all files in a directory (for integrity verification)"""
    hasher = hashlib.sha256()
    for filepath in sorted(Path(root_path).rglob('*')):
        if filepath.is_file():
            with open(filepath, 'rb') as f:
                hasher.update(f.read())
    return hasher.hexdigest()

def make_readonly(path):
    """Make a file or directory read-only"""
    import stat
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    except Exception as e:
        print(f"Warning: Could not make {path} read-only: {e}")

def backup_archive(source_folder, archive_root):
    """
    Backup the source folder into 00-מקור-גולמי/
    Makes the backup read-only and records a checksum
    """
    backup_dir = os.path.join(archive_root, "00-מקור-גולמי")

    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # If backup already exists, verify and skip
    source_name = os.path.basename(source_folder)
    backup_target = os.path.join(backup_dir, source_name)

    if os.path.exists(backup_target):
        print(f"✓ Backup already exists at: {backup_target}")
        print("  (Idempotent: skipping re-copy)")
        return backup_target

    # Copy the entire source tree
    print(f"Backing up: {source_folder}")
    print(f"Destination: {backup_target}")
    print("This preserves the originals exactly as they are...")

    shutil.copytree(source_folder, backup_target, dirs_exist_ok=True)

    # Calculate hash before making read-only
    print("Calculating integrity hash...")
    backup_hash = get_directory_hash(backup_target)

    # Make backup read-only
    print("Making backup read-only...")
    for root, dirs, files in os.walk(backup_target):
        for file in files:
            make_readonly(os.path.join(root, file))
        for dir in dirs:
            make_readonly(os.path.join(root, dir))
    make_readonly(backup_target)

    # Record the checksum
    checksum_file = os.path.join(backup_dir, "CHECKSUM.txt")
    with open(checksum_file, 'w', encoding='utf-8') as f:
        f.write(f"Archive Backup Integrity Checksum\n")
        f.write(f"Date: {datetime.now().isoformat()}\n")
        f.write(f"Source: {source_folder}\n")
        f.write(f"Backup: {backup_target}\n")
        f.write(f"SHA256: {backup_hash}\n")

    print(f"\n✓ Backup complete!")
    print(f"  Checksum: {backup_hash}")
    print(f"  Checksum file: {checksum_file}")

    return backup_target

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python archive_backup.py <source_folder> <archive_root>")
        sys.exit(1)

    source = sys.argv[1]
    archive = sys.argv[2]

    if not os.path.isdir(source):
        print(f"Error: Source folder not found: {source}")
        sys.exit(1)

    backup_archive(source, archive)
