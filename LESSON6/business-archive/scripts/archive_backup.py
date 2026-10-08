"""Back up a business's original files into a read-only copy that preserves the
existing state, before anything touches them. This is always the FIRST step — you
reorganize copies, never the source. Idempotent: if the backup already exists, it is
left untouched.

Layout created:
    <archive_root>/00-מקור-גולמי/   ← read-only copy of <source> contents
    <archive_root>/00-מקור-גולמי/.backup-manifest.json  ← proof nothing changed

Usage:  python archive_backup.py "<source folder>" "<archive_root>"
"""
import sys, os, json, hashlib, shutil, stat
from datetime import datetime, timezone
from pathlib import Path

RAW = "00-מקור-גולמי"
MANIFEST = ".backup-manifest.json"


def make_readonly(root: Path):
    """Strip write bits from every file and dir under root."""
    for p in root.rglob("*"):
        try:
            mode = p.stat().st_mode
            p.chmod(mode & ~stat.S_IWUSR & ~stat.S_IWGRP & ~stat.S_IWOTH)
        except OSError:
            pass


def manifest_for(root: Path) -> dict:
    """A light proof-of-integrity: count, total bytes, and a hash over the
    sorted (relpath, size) list. Cheap even for tens of thousands of files."""
    entries, total = [], 0
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.name != MANIFEST:
            size = p.stat().st_size
            entries.append(f"{p.relative_to(root).as_posix()}:{size}")
            total += size
    digest = hashlib.sha256("\n".join(entries).encode("utf-8")).hexdigest()
    return {"file_count": len(entries), "total_bytes": total,
            "structure_hash": digest,
            "backed_up_at": datetime.now(timezone.utc).isoformat()}


def main():
    if len(sys.argv) < 3:
        print('usage: archive_backup.py "<source folder>" "<archive_root>"',
              file=sys.stderr)
        sys.exit(2)
    source = Path(sys.argv[1]).expanduser()
    archive_root = Path(sys.argv[2]).expanduser()
    if not source.is_dir():
        print(f"source folder not found: {source}", file=sys.stderr)
        sys.exit(1)

    raw = archive_root / RAW
    if raw.exists() and any(raw.iterdir()):
        print(f"backup already exists, leaving untouched: {raw}")
        m = raw / MANIFEST
        if m.exists():
            print("manifest:", m.read_text(encoding="utf-8"))
        return

    archive_root.mkdir(parents=True, exist_ok=True)
    print(f"backing up {source} -> {raw} ...")
    # copy2 preserves timestamps; dirs_exist_ok keeps it idempotent-friendly
    shutil.copytree(source, raw, dirs_exist_ok=True)

    manifest = manifest_for(raw)
    (raw / MANIFEST).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    make_readonly(raw)

    print(f"backed up {manifest['file_count']} files "
          f"({manifest['total_bytes']/1e6:.1f} MB), preserved read-only.")
    print(f"integrity hash: {manifest['structure_hash'][:16]}…")


if __name__ == "__main__":
    main()
