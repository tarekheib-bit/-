# Analysis guide — reasoning about any business's books

Read this when a folder is unfamiliar or messy. It is a way of thinking, not a
lookup table. The whole point of the skill is that it works on businesses we've
never seen, in languages and layouts we didn't anticipate — so the guidance here
is about *judgment*, with the reasons spelled out so you can extend it yourself.

## How to recognize what a document is (by meaning, not by name)

You read headers and content and ask "what business event does this record?":

- **A list of dated transactions with a running balance** is a bank/cash account.
  The latest-dated row's balance is the current cash. (Watch the date format before
  you decide which row is "latest" — see pitfalls.)
- **A list of sales with amounts** (invoices, receipts, a POS/sales export) is
  revenue. If each line also has a cost, the difference feeds gross margin.
- **A list of people/companies with an outstanding amount** is a ledger: customers
  with balances = receivable (owed to the business); suppliers/vendors with
  balances = payable (owed by the business). Tell them apart by who the entries are
  (clients vs vendors), not by a fixed column name.
- **Recurring outflows** — rent, salaries, utilities, card statements — are
  operating expenses.

The same logic holds in any language: a header you understand as "amount / total /
sum / סכום / مبلغ / Σ" is money; "balance / יתרה / رصيد" trends are an account.
Use your language understanding; don't pattern-match a hardcoded string.

## Use the tools to do arithmetic, not to decide meaning

`read_folder.py <folder>` gives you, per sheet: headers, row count, the **sum of
every numeric column**, head + tail sample rows, and which columns are
low-cardinality labels. From that you decide — by meaning — which column is the
amount, which is the balance, which is the label.

Then, for a breakdown (top products, expense categories), tell the tool which
columns to use:

```bash
python read_folder.py --group "<file>" "<sheet>" "<label column>" "<amount column>"
```

This split matters: a generic script cannot reliably guess which numeric column is
"money" — an invoice-number column and a cumulative-balance column both have huge
sums but mean nothing when added. You know which is the amount because you read the
header; the script just groups and sums what you point it at.

## Reconciliation and de-duplication

Real archives hold the same fact in several places: a sale may appear in an
invoice PDF, a sales sheet, and a bank deposit. Count it once. When a stable id
exists (invoice number), dedupe on it. Watch for the same data duplicated across
files — e.g. a per-year book *and* an all-years export. If two sources should
agree and don't, say so rather than silently picking one.

## Pitfalls to name out loud (don't fake confidence)

- **Date formats.** "Latest balance = cash" only works if you sort dates correctly.
  `2026-05` sorts fine as text; `15/05/2026` does not. Normalize before choosing
  the latest row.
- **Multiple accounts / currencies.** Several bank accounts, or mixed currencies,
  must be separated — never summed into one cash figure. If you can't separate
  them, report per-account or flag it.
- **Identifiers that look like money.** Invoice numbers, customer ids, phone
  numbers are numeric but are not amounts. Never sum them as money.
- **Refunds, credits, opening balances, VAT.** These flip signs or double-count if
  ignored. Treat negative sales as refunds; don't count an opening balance as
  revenue.
- **Image-only scans/PDFs.** No text layer. Read with vision if a needed figure
  lives only there; otherwise leave it "אין נתון" rather than guess.

## The honest answer

When a figure has no trustworthy source, the dashboard shows "אין נתון". That is a
feature: a finance dashboard earns trust by being right and by admitting gaps, not
by looking complete. Every number you do show, you should be able to trace back to
the exact file, sheet, and rows.
