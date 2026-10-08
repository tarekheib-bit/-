---
name: business-archive
description: Use when someone points at a real business's files and wants to make sense of the whole pile before doing anything with it - the messy folder of Excel/PDF/Word/scans/images/exports a business accumulates over years. Trigger on "organize these business files", "I have a folder of everything from the business", "turn this mess into something usable", "prepare these files for a dashboard / website", "what assets does this business have", even before any specific deliverable is named. This skill is the upstream ingestion stage: it backs up the originals untouched, builds a complete index, classifies every file by what it MEANS, organizes it into a clean typed archive, systematically surfaces what's missing, and produces an AI-ready layer that downstream skills (financial-dashboard, landing pages) consume. It expects anything from 20 files to tens of thousands, in any language and any format, from any business software. It commits to no fixed list - it researches and reasons.
---

# Business archive — turn a real business's pile of files into a clean, AI-ready archive

A real business is not 20 tidy files. It is years of accumulation across dozens of
tools: accounting exports, bank statements, payroll runs, CRM dumps, product
catalogs, contracts, a chaos of logos and photos, screenshots, scans, duplicates,
"סופי סופי 2 העתק.xlsx". Hundreds to tens of thousands of files, in Hebrew and
English, from software you've never seen. Before anyone builds a dashboard or a
website from it, **someone has to make sense of the whole pile** without losing or
corrupting a single original. That is this skill.

You are an archivist and analyst, not a file mover. You **reason about what each
document means** and **expect the full universe of business assets** — you don't
match filenames, and you commit to no fixed list of file types or software. The
output is a clean, indexed, typed archive plus an AI-ready layer that the
financial-dashboard skill and landing-page skill build on.

## Two unbreakable rules

1. **Back up and preserve the existing state before you touch anything.** The first
   action is always a read-only backup of every original, exactly as it is now. You
   reorganize *copies*, never the source. If a later step is wrong, the preserved
   backup is the safety net.
2. **The index is the source of truth.** `catalog.json` records what actually
   exists — every file, its hash, its detected category. You never invent a file,
   a number, or an asset that isn't there. Missing is "חסר נתון" / "לא נמצא", said
   out loud, with the option to collect it.

## The archive layout

Everything lives under a working root the user chooses. Folder and category names
are Hebrew (this is the user's real deliverable); code, identifiers and tool flags
are English.

```
<עסק>/
  00-מקור-גולמי/      read-only backup preserving the originals as-is — NEVER mutated
  01-מאורגן/          classified copies sorted into typed category folders
    הנהלת-חשבונות/  בנקאות-ואשראי/  שכר-ומשאבי-אנוש/  מכירות-ולקוחות-CRM/
    תפעול-ERP/  מלאי-וקטלוג/  מסחר-ותשלומים/  שיווק-ומותג/  משפטי-וחוזים/
    דיגיטל-ולינקים/  תקשורת-וביקורות/  לא-מסווג/
  02-AI-ready/        normalized, deduped, machine-clean layer
    catalog.json      the index of every file (path, type, size, hash, category, source)
    <clean per-type documents downstream skills read>
```

`שיווק-ומותג/` itself holds `תיק-מותג/`, `לוגואים/`, `ויזואלי-וקריאייטיב/`.
Downstream skills (dashboard, landing page) read **only** from `02-AI-ready/`.

The archive lives under a **working folder the user chooses** — it can be wherever
their files already sit, or a new folder made for this. The skill never depends on a
specific absolute path, and it locates its own scripts/references relative to its own
directory, so it works wherever it's installed or copied. No setup, no config, no
assumptions about whose machine this is.

## The process (top to bottom)

### 0. Orient — search first, then ask (never block the flow)
Open by telling the user, in one breath, what's about to happen and that it's safe:
*"קודם אני מקים גיבוי read-only שמשמר את הקבצים המקוריים שלך בדיוק כפי שהם, בלי לגעת
בהם, ואז מסדר הכל לארכיון נקי, מבין את העסק, ובונה דשבורד."* The backup-first promise is
what makes it safe to point this at real business data; say it up front.

Then find the files. The machine is messy and that's fine — you adapt, you don't fail.

- **Look first.** Check the obvious homes: the folder open in the editor, the
  Desktop, Documents, Downloads. A folder holding many mixed business files (Excel,
  PDF, images, exports) is almost certainly the one.
- **Then ask, plainly.** If you can't identify it confidently, ask:
  *"איפה התיקייה עם קבצי העסק?"* One question, not a form. A wrong guess wastes their
  time; a quick question doesn't.
- **Settle the two paths.** The **source** is the business folder they point you at;
  the **working folder** (archive root) is where 00/01/02 will live — offer to create
  it if it doesn't exist. Quote every path: names have spaces and non-Latin
  characters. Keep the archive root separate from the source so the backup never
  nests inside the folder it's copying.

### 1. Back up and preserve the originals
Before anything else, copy the whole source tree into `00-מקור-גולמי/` and make it
read-only, preserving the existing state exactly as it is. This is non-negotiable and
comes first even on a tiny folder.

```bash
python3 scripts/archive_backup.py "<source folder>" "<עסק>"
```

It copies the tree, makes the backup read-only, and records a top-level checksum so
you can prove later that no original changed. Idempotent: re-running won't
re-copy or overwrite the preserved backup.

### 2. Index everything (built for scale)
You cannot read tens of thousands of files into context, and you shouldn't try.
Build the catalog first — it triages by extension and a content sniff, hashes for
dedup, and assigns a *tentative* category to every file:

```bash
python3 scripts/build_catalog.py "<עסק>" > catalog_summary.txt
```

It writes `02-AI-ready/catalog.json` and prints a summary: counts per category,
per file type, duplicate clusters, and the files it couldn't classify. The script
**triages**; it does not decide meaning — you do, in the next step.

### 3. Survey and classify by meaning
Read the summary (not every file). For each cluster, judge by contents what it
really is and which category it belongs to — names lie, and the same software
exports under wildly different headers per business. Where the tentative category
is wrong or "לא-מסווג", correct it. Use `reference/asset-taxonomy.md` to know what
to expect: the full asset universe, the Israeli and global software that produces
each kind of file, and the tell-tales that identify them. Spot-read a few
representative files per cluster to confirm; deep-read only when a downstream
deliverable will need that file's contents.

### 4. Organize into the typed archive
Apply the corrected classification: copy files from the preserved backup into
`01-מאורגן/<category>/`. Anything you genuinely can't place goes to `לא-מסווג/` and
is surfaced, never silently dropped.

```bash
python3 scripts/organize.py "<עסק>"   # reads catalog.json, copies into 01-מאורגן/
```

### 5. Collect what's missing — systematic, but always skippable
Walk the taxonomy category by category and name what's absent. For each gap,
follow the fallback chain in `reference/asset-taxonomy.md` (e.g. brand kit → logos
folder → scan the archive for logo-like files → create an organized brand folder).
Every time, tell the user plainly: **"אפשר לדלג, אבל הנה מה שחסר ולמה זה משנה."**
Collection is systematic and thorough; skipping is always allowed and always
explained. A digital-assets/links inventory (domains, social, site, hosting) often
doesn't exist as a file — offer to assemble one.

### 6. Produce the AI-ready layer
`02-AI-ready/` is the clean handoff. `catalog.json` is already there. Add the
normalized, source-cited documents downstream skills need — for financials that is
`findings.json` (the financial-dashboard skill owns its schema and arithmetic).
Keep `02-AI-ready/` machine-clean: no duplicates, consistent naming, every derived
fact traceable back through `catalog.json` to a file in `00-מקור-גולמי/`.

### 7. Hand off to the consumer skill
Point the next skill at `02-AI-ready/`:
- **financial-dashboard** reads the financial/accounting/bank material and renders
  the dashboard.
- **landing-page** skill reads `שיווק-ומותג/` (brand kit, logos, visuals) and the
  reviews/testimonials for copy.

## Scale strategy (tens of thousands of files)

- **Catalog before content.** Build the index first; never bulk-load file bodies.
- **Triage by type, then sample.** Group by extension/category; read a few
  representatives per cluster, not the whole cluster.
- **Dedup hard.** By content hash, and by business identifier (invoice number,
  customer id) for tabular data — the same fact recurs across many files.
- **Deep-read on demand only.** A file's full contents are read only when a
  specific deliverable needs them.
- **Surface, don't drown.** Report per-category counts and the unclassified pile;
  let the user steer where to dig.

## The faithfulness contract

`00-מקור-גולמי/` is never mutated. `catalog.json` reflects exactly what exists.
Nothing is invented — not a file, not a category membership you're unsure of, not a
missing asset. When you can't classify or can't find something, you say so and
offer to collect it. An honest, partial archive that the user can trust beats an
impressive, fabricated one.

## References
- `reference/asset-taxonomy.md` — the full asset universe: every category, what to
  expect inside it, the Israeli + global software that produces it, the tell-tales
  that identify each kind of file, and the fallback chain when a category is missing.

## Why this is evergreen
It encodes a **process** — back up, index, classify by meaning, organize, collect
the gaps, normalize — and an *expectation of the whole business-asset universe*,
not a fixed list of filenames or a closed set of tools. Hand it any business in any
language, with twenty files or fifty thousand, and the same process applies. If you
catch yourself hardcoding "the payroll file is always called X" or "only handle
these five formats", that's the signal you've drifted from archiving into parsing —
expect more, reason more.
