# Asset taxonomy — the full universe of business assets

Read this to know **what to expect** in a real business archive: every category, the
documents inside it, the software (Israeli and global) that produces them, the
tell-tales that identify a file by meaning, and the **fallback chain** when a
category is missing. This is not a closed list to match against — it is a map of the
territory so you're never surprised. A real business may have files this doesn't
name; classify them by the same reasoning.

Folder/category names below are the Hebrew names used in `01-מאורגן/`. Software
names stay in their original form.

## Contents
1. [How to expect, sniff, and classify](#1-how-to-expect-sniff-and-classify)
2. [Categories](#2-categories)
   - Accounting · Banking & credit · Payroll & HR · Sales/CRM · Operations/ERP ·
     Inventory & catalog · Commerce & payments · Marketing & brand · Legal ·
     Digital & links · Communications & reviews
3. [Fallback chains](#3-fallback-chains-when-a-category-is-missing)
4. [File-format expectations at scale](#4-file-format-expectations-at-scale)

---

## 1. How to expect, sniff, and classify

Three signals, in order of trust:
1. **Contents** (most trustworthy). Headers, columns, recurring fields, totals.
   A sheet with dated rows and a running balance is a bank account whatever it's
   called.
2. **Software fingerprint.** Exports carry tells: a Hebrew accounting export from
   חשבונית ירוקה / iCount / חשבשבת has recognizable column sets and logos; a payroll
   PDF from מיכפל / חילן has a standard תלוש layout; a Shopify export has a known
   CSV header. Knowing the tool narrows what the file is.
3. **Filename and folder** (least trustworthy — names lie). A hint, never a verdict.

Classify by what the document *records about the business*, not by extension. The
same `.xlsx` could be a sales ledger, a stock count, or a customer list.

## 2. Categories

### הנהלת-חשבונות — Accounting
- **Expect:** profit & loss (רווח והפסד), balance sheet (מאזן), cash-flow, trial
  balance (מאזן בוחן), general ledger (ספר ראשי / כרטסת), invoices (חשבוניות),
  receipts (קבלות), credit/refund notes (זיכויים), VAT reports (דוחות מע"מ), advance
  tax (מקדמות), annual statements (דוחות שנתיים), expense logs.
- **Software:** חשבונית ירוקה (Green Invoice), iCount, חשבשבת (Hashavshevet),
  ריווחית (Rivhit), SUMIT, YPAY, iFreelance · QuickBooks, Xero, FreshBooks, Wave,
  Priority / SAP Business One (also ERP).
- **Tell-tales:** amount + date + document-number columns; VAT (מע"מ) lines;
  cumulative totals; customer/supplier names beside sums.

### בנקאות-ואשראי — Banking & credit
- **Expect:** bank statements (דפי עו"ש), credit-card statements (פירוט כרטיס
  אשראי), loan amortization schedules (לוחות סילוקין), standing orders (הוראות קבע),
  credit/business-risk reports (דוחות אשראי).
- **Source:** the banks directly; credit bureaus (BDI / דן אנד ברדסטריט, נתוני אשראי
  של בנק ישראל).
- **Tell-tales:** dated transactions with a **running balance**; the latest-dated
  row's balance is current cash. Watch date formats and separate accounts/currencies.

### שכר-ומשאבי-אנוש — Payroll & HR
- **Expect:** payslips (תלושי שכר), payroll summary reports (דוחות שכר), Form 102 /
  126, attendance/time exports (נוכחות), pension & benefits (פנסיה, הפרשות), employee
  roster, contracts of employment.
- **Software:** מיכפל (Michpal), חילן (Hilan), מלם (Malam), סינאל (Synel), עוקץ
  (Oketz), סינריון (Synerion), שקלולית · ADP, Gusto.
- **Tell-tales:** gross/net (ברוטו/נטו), employer cost, deductions, monthly per-employee
  rows; standard תלוש layout.

### מכירות-ולקוחות-CRM — Sales & customers (CRM)
- **Expect:** customer lists, contacts, leads, deals/pipeline, sales activity, quotes
  (הצעות מחיר), churn/retention exports.
- **Software:** Salesforce, HubSpot, Monday, Zoho, Pipedrive, Powerlink (ישראלי).
- **Tell-tales:** people/companies with stage, owner, value, dates; one row per
  lead/deal/contact.

### תפעול-ERP — Operations (ERP)
- **Expect:** orders (הזמנות), work orders, projects, production/BOM, procurement,
  fulfillment, scheduling.
- **Software:** Priority (פריוריטי), SAP Business One, Oracle NetSuite, Monday.
- **Tell-tales:** order/work-order numbers, statuses, quantities, links between
  customers, products and dates.

### מלאי-וקטלוג — Inventory & catalog
- **Expect:** stock counts (ספירות מלאי), product catalog (קטלוג מוצרים), price lists
  (מחירונים), SKU lists, supplier price sheets.
- **Tell-tales:** SKU/מק"ט, quantity-on-hand, unit price, cost; product rows without
  a date dimension (a catalog, not a transaction log).

### מסחר-ותשלומים — Commerce & payments
- **Expect:** online-store order/product/customer exports, payment-gateway
  settlements, payout reports, subscription/MRR exports.
- **Software:** Shopify, WooCommerce, Wix, Stripe, PayPal · Israeli gateways: PayPlus,
  Tranzila, Cardcom, Meshulam, Grow (ex-Pay).
- **Tell-tales:** standard platform CSV headers; gross vs fees vs net payout;
  settlement dates.

### שיווק-ומותג — Marketing & brand
Holds three sub-folders: `תיק-מותג/`, `לוגואים/`, `ויזואלי-וקריאייטיב/`.
- **Brand kit (תיק מותג):** logo variations, color palette, typography, imagery
  guidelines, brand guidelines / style guide (often a PDF), approved templates.
- **Logos:** primary/secondary/mono logos in multiple formats (SVG, PNG with
  transparency, EPS/AI), favicons.
- **Creative & visual:** photos, video, social posts, ads, presentations (מצגות),
  one-pagers, banners.
- **Software:** Canva, Figma, Adobe (AI/PSD/INDD), brand-portal tools (Frontify,
  Brandkit).
- **Tell-tales:** image/vector/video extensions; "logo", "brand", "guidelines" in
  names; consistent color/typeface across files.

### משפטי-וחוזים — Legal & contracts
- **Expect:** contracts & agreements (חוזים, הסכמים), terms of service / privacy
  (תקנון, מדיניות פרטיות), IP/trademarks, licenses, insurance policies (ביטוחים),
  NDAs, incorporation documents.
- **Tell-tales:** clause-numbered prose, signature blocks, effective dates, party
  names.

### דיגיטל-ולינקים — Digital assets & links
- **Expect:** domains, website files/exports, hosting details, social handles,
  link lists, analytics exports, an inventory of accounts (without secrets).
- **Note:** this often **does not exist as a file**. Offer to assemble a links/digital
  inventory. Never record passwords or secrets — references only.

### תקשורת-וביקורות — Communications & reviews
- **Expect:** customer reviews (Google, Facebook, Tripadvisor), testimonials
  (המלצות), email threads, support tickets, WhatsApp/chat exports, press.
- **Use:** primary fuel for copywriting on the landing page; quote faithfully, never
  fabricate a testimonial.

### לא-מסווג — Unclassified
Anything you genuinely cannot place. Never silently dropped — surfaced for the user
to review or reclassify.

## 3. Fallback chains (when a category is missing)

Search systematically; degrade gracefully; always allow skipping. The pattern,
shown for the hardest case (brand) and generalized:

**Brand kit:**
1. A real brand kit / guidelines folder or PDF → use it.
2. No kit, but a logos folder → use that as the brand source.
3. No logos folder → scan the whole archive for logo-like files (vector files,
   transparent PNGs, files named logo/brand/מותג).
4. Nothing found → create an organized `שיווק-ומותג/` with empty sub-folders and
   tell the user exactly what to add and why it matters for the website.

**General chain for any category:** organized source → looser source → scan the
archive by content → assemble/create the structure and name the gap. At every rung:
*"אפשר לדלג, אבל הנה מה שחסר ולמה זה משנה."*

## 4. File-format expectations at scale

Expect, and triage by, the full spread:
- **Tabular:** `.xlsx .xls .csv .tsv .ods` — ledgers, exports, catalogs (read via the
  financial-dashboard reader when financial).
- **Documents:** `.pdf .doc .docx .rtf .txt .pages` — invoices, contracts, reports,
  letters; some PDFs are **image-only scans** with no text layer (read with vision
  only when a needed figure lives there).
- **Presentations:** `.ppt .pptx .key` — pitch decks, internal reviews.
- **Images:** `.jpg .png .webp .heic .gif .tif` — photos, scans, screenshots, logos.
- **Vector/design:** `.svg .ai .eps .psd .indd .fig` — logos, brand assets.
- **Video/audio:** `.mp4 .mov .m4a .mp3` — ads, testimonials, recordings.
- **Data/config:** `.json .xml .zip` — exports, backups, archives (unzip and index
  contents).

At tens of thousands of files this spread is normal. Index everything, dedup by
hash, and only open what a deliverable needs. The point is not to read it all — it
is to *know what's there* and reach for the right file when a downstream skill asks.
