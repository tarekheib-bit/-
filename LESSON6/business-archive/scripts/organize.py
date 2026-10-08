"""Copy files from the preserved backup into the typed archive, using the (corrected)
categories in catalog.json. Duplicates are skipped — one canonical copy per file —
so 01-מאורגן/ stays clean; the originals all remain safe in 00-מקור-גולמי/.

Reads:   <archive_root>/02-AI-ready/catalog.json
Creates: <archive_root>/01-מאורגן/<category>/...

Usage:  python organize.py "<archive_root>" [--dry-run]
"""
import sys, json, shutil
from pathlib import Path

RAW = "00-מקור-גולמי"
ORG = "01-מאורגן"
AI = "02-AI-ready"


def unique_dest(dest: Path) -> Path:
    """Avoid clobbering when two source files share a name in one category."""
    if not dest.exists():
        return dest
    stem, suf, n = dest.stem, dest.suffix, 2
    while True:
        cand = dest.with_name(f"{stem} ({n}){suf}")
        if not cand.exists():
            return cand
        n += 1


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        print('usage: organize.py "<archive_root>" [--dry-run]', file=sys.stderr)
        sys.exit(2)
    root = Path(args[0]).expanduser()
    catalog_path = root / AI / "catalog.json"
    if not catalog_path.exists():
        print(f"catalog not found: {catalog_path}\nrun build_catalog.py first.",
              file=sys.stderr)
        sys.exit(1)

    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    raw, org = root / RAW, root / ORG
    placed, skipped = 0, 0
    per_cat = {}

    for f in catalog["files"]:
        if f.get("is_duplicate"):
            skipped += 1
            continue
        src = raw / f["path"]
        if not src.exists():
            print(f"  missing in backup, skipped: {f['path']}", file=sys.stderr)
            skipped += 1
            continue
        dest_dir = org / f["category"]
        dest = unique_dest(dest_dir / Path(f["path"]).name)
        per_cat[f["category"]] = per_cat.get(f["category"], 0) + 1
        if dry:
            placed += 1
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        placed += 1

    verb = "would place" if dry else "placed"
    print(f"{verb} {placed} files into {org} ({skipped} duplicates/missing skipped)")
    for c, n in sorted(per_cat.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>6}  {c}")
    if dry:
        print("\n(dry run — nothing copied)")


if __name__ == "__main__":
    main()
