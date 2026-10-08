"""Index every file in the preserved backup and assign each a TENTATIVE category.
Built for scale: it triages by extension, filename hints, and a content hash for
dedup — it does NOT decide meaning. The analyst (you) reviews the summary and
corrects categories by what the documents actually are.

Writes:  <archive_root>/02-AI-ready/catalog.json
Prints:  a human summary (counts per category / format, duplicate + unclassified piles)

Usage:  python build_catalog.py "<archive_root>" > catalog_summary.txt
"""
import sys, os, json, hashlib
from datetime import datetime, timezone
from pathlib import Path

RAW = "00-מקור-גולמי"
AI = "02-AI-ready"
MANIFEST = ".backup-manifest.json"
UNCLASSIFIED = "לא-מסווג"

# extension -> coarse format class
FORMAT = {
    "tabular": {".xlsx", ".xls", ".csv", ".tsv", ".ods"},
    "document": {".pdf", ".doc", ".docx", ".rtf", ".txt", ".pages"},
    "presentation": {".ppt", ".pptx", ".key"},
    "image": {".jpg", ".jpeg", ".png", ".webp", ".heic", ".gif", ".tif", ".tiff", ".bmp"},
    "vector": {".svg", ".ai", ".eps", ".psd", ".indd", ".fig"},
    "media": {".mp4", ".mov", ".m4a", ".mp3", ".wav", ".avi", ".mkv"},
    "data": {".json", ".xml", ".zip", ".gz"},
}
EXT_FORMAT = {ext: cls for cls, exts in FORMAT.items() for ext in exts}

# tentative category by keyword in the (lowercased) relative path. Hebrew + English.
# First match wins; order matters (specific before generic).
KEYWORDS = [
    ("שכר-ומשאבי-אנוש", ["תלוש", "payslip", "payroll", "שכר", "salary", "נוכחות",
                          "attendance", "פנסיה", "pension", "126", "102", "עובד",
                          "employee", "michpal", "מיכפל", "חילן", "hilan", "סינאל"]),
    ("בנקאות-ואשראי", ["עו\"ש", "עוש", "בנק", "bank", "statement", "דף חשבון",
                        "אשראי", "credit", "סילוקין", "loan", "הוראת קבע"]),
    ("מסחר-ותשלומים", ["shopify", "woocommerce", "stripe", "paypal", "payplus",
                        "tranzila", "cardcom", "meshulam", "payout", "settlement",
                        "סליקה", "תשלום", "checkout"]),
    ("הנהלת-חשבונות", ["חשבונית", "invoice", "קבלה", "receipt", "מאזן", "balance",
                        "רווח", "profit", "הפסד", "מע\"מ", "מעמ", "vat", "כרטסת",
                        "ledger", "p&l", "pnl", "מקדמ", "ירוקה", "icount", "חשבשבת",
                        "rivhit", "ריווחית", "sumit", "הנהח", "הנהלת חשבונות"]),
    ("מלאי-וקטלוג", ["מלאי", "inventory", "stock", "קטלוג", "catalog", "מחירון",
                     "price list", "pricelist", "sku", "מק\"ט", "מקט"]),
    ("מכירות-ולקוחות-CRM", ["crm", "ליד", "lead", "לקוח", "customer", "contact",
                            "pipeline", "deal", "עסקה", "הצעת מחיר", "quote",
                            "salesforce", "hubspot", "מכירות", "sales"]),
    ("תפעול-ERP", ["erp", "הזמנה", "order", "work order", "פרויקט", "project", "bom",
                   "production", "priority", "פריוריטי", "sap", "netsuite", "ייצור"]),
    ("שיווק-ומותג", ["brand", "מותג", "logo", "לוגו", "creative", "קריאייטיב",
                     "banner", "באנר", "social", "מצגת", "presentation", "deck",
                     "פרסום", "advert", " ad ", "campaign", "קמפיין", "guidelines",
                     "צבע", "palette"]),
    ("משפטי-וחוזים", ["חוזה", "contract", "הסכם", "agreement", "תקנון", "terms",
                      "privacy", "פרטיות", "ביטוח", "insurance", "nda", "license",
                      "רישיון", "תקנון"]),
    ("דיגיטל-ולינקים", ["domain", "דומיין", "link", "לינק", "url", "website", "אתר",
                        "hosting", "אחסון", "analytics", "אנליטיקס"]),
    ("תקשורת-וביקורות", ["review", "ביקורת", "testimonial", "המלצה", "feedback",
                         "משוב", "ticket", "פנייה", "whatsapp", "וואטסאפ", "chat",
                         "מייל", "email", "press", "תקשורת"]),
]

# format-based fallback when no keyword matches
FORMAT_FALLBACK = {
    "image": "שיווק-ומותג",
    "vector": "שיווק-ומותג",
    "media": "שיווק-ומותג",
}


def classify(rel_path: str, fmt: str) -> str:
    low = rel_path.lower()
    for category, words in KEYWORDS:
        for w in words:
            if w.lower() in low:
                return category
    return FORMAT_FALLBACK.get(fmt, UNCLASSIFIED)


def file_hash(p: Path, chunk=1 << 20) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for blk in iter(lambda: f.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


def main():
    if len(sys.argv) < 2:
        print('usage: build_catalog.py "<archive_root>"', file=sys.stderr)
        sys.exit(2)
    root = Path(sys.argv[1]).expanduser()
    raw = root / RAW
    if not raw.is_dir():
        print(f"backup not found: {raw}\nrun archive_backup.py first.",
              file=sys.stderr)
        sys.exit(1)

    files, seen = [], {}
    for p in sorted(raw.rglob("*")):
        if not p.is_file() or p.name == MANIFEST:
            continue
        rel = p.relative_to(raw).as_posix()
        ext = p.suffix.lower()
        fmt = EXT_FORMAT.get(ext, "other")
        size = p.stat().st_size
        digest = file_hash(p)
        # Dedup only same-content AND same-extension. Empty files are never
        # "duplicates" — a 0-byte .pdf and a 0-byte .docx are distinct stubs,
        # not copies of each other.
        key = (ext, digest)
        is_dup = size > 0 and key in seen
        files.append({
            "path": rel,
            "ext": ext,
            "format": fmt,
            "size": size,
            "hash": digest,
            "category": classify(rel, fmt),
            "is_empty": size == 0,
            "is_duplicate": is_dup,
            "duplicate_of": seen.get(key, "") if is_dup else "",
        })
        if size > 0 and not is_dup:
            seen[key] = rel

    by_cat, by_fmt = {}, {}
    dup = unclassified = empty = 0
    for f in files:
        if f["is_empty"]:
            empty += 1
        if f["is_duplicate"]:
            dup += 1
            continue
        by_cat[f["category"]] = by_cat.get(f["category"], 0) + 1
        by_fmt[f["format"]] = by_fmt.get(f["format"], 0) + 1
        if f["category"] == UNCLASSIFIED:
            unclassified += 1

    catalog = {
        "business_root": str(root),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "totals": {"files": len(files), "unique": len(files) - dup,
                   "duplicates": dup, "empty": empty,
                   "unclassified": unclassified},
        "by_category": by_cat,
        "by_format": by_fmt,
        "files": files,
        "note": "category is TENTATIVE (triage by extension + filename). "
                "Review and correct by meaning before organizing.",
    }
    out_dir = root / AI
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "catalog.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")

    # human summary
    print(f"indexed {len(files)} files "
          f"({len(files) - dup} unique, {dup} duplicates, {empty} empty)")
    print(f"catalog -> {out_dir / 'catalog.json'}\n")
    print("by category (unique files):")
    for c, n in sorted(by_cat.items(), key=lambda kv: -kv[1]):
        flag = "  ← review" if c == UNCLASSIFIED else ""
        print(f"  {n:>6}  {c}{flag}")
    print("\nby format:")
    for c, n in sorted(by_fmt.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>6}  {c}")
    if unclassified:
        print(f"\n{unclassified} files are לא-מסווג — classify these by meaning.")


if __name__ == "__main__":
    main()
