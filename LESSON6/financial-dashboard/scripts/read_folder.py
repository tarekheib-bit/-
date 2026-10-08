"""Generic, semantics-free folder reader for the financial-dashboard skill.

Turns a messy business folder into a compact, readable SUMMARY so an analyst
(Claude) can reason over large files without ingesting every row. For each
spreadsheet sheet / CSV it prints: the headers, the row count, the SUM of every
numeric column, head + tail sample rows (so the latest balance is visible), and a
generic breakdown (top values of the dominant label column by the largest numeric
column). It assigns NO meaning — it does not decide what is revenue, a supplier,
or a bank account. That interpretation is the analyst's job, using business
understanding, in whatever language the files use.

Usage:  python read_folder.py "<folder>"   ->  prints a text summary
Works on .xlsx and .csv. PDFs / images / other files are listed, not parsed.
"""
import sys, os, csv, glob
from collections import defaultdict

try:
    from openpyxl import load_workbook
except ImportError:
    load_workbook = None


def _num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if v is None:
        return None
    s = str(v).replace(",", "").replace("₪", "").replace('ש"ח', "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def _cell(c):
    return "" if c is None else str(c)


def _summarize(name, headers, rows, out):
    headers = [_cell(h).strip() for h in headers]
    ncol = len(headers)
    col_sum, col_numcount, distinct = defaultdict(float), defaultdict(int), defaultdict(set)
    for r in rows:
        for i in range(min(ncol, len(r))):
            n = _num(r[i])
            if n is not None:
                col_sum[i] += n
                col_numcount[i] += 1
            else:
                distinct[i].add(_cell(r[i]))
    is_num = {i: col_numcount[i] >= max(1, len(rows) * 0.6) for i in range(ncol)}

    out.append(f"### {name}")
    out.append(f"rows: {len(rows)} | columns: {headers}")
    sums = {headers[i] or f"col{i}": round(col_sum[i], 2) for i in range(ncol) if is_num.get(i)}
    if sums:
        out.append(f"numeric column totals: {sums}")

    # report which columns look categorical (low-cardinality labels) — WITHOUT
    # guessing which numeric column is "money". You (the analyst) decide that by
    # meaning, then ask for a breakdown with:  read_folder.py --group <file> <sheet> <label> <value>
    cats = {headers[i]: len(distinct[i]) for i in range(ncol)
            if not is_num.get(i) and 1 < len(distinct[i]) <= 60}
    if cats:
        out.append(f"label columns (distinct counts): {cats}")

    for r in rows[:3]:
        out.append(f"  head: {[_cell(c) for c in r[:ncol]]}")
    if len(rows) > 3:
        for r in rows[-2:]:
            out.append(f"  tail: {[_cell(c) for c in r[:ncol]]}")
    out.append("")


def read_folder(folder):
    out = [f"# Folder summary: {folder}", ""]
    xlsx = sorted(glob.glob(os.path.join(folder, "**", "*.xlsx"), recursive=True))
    csvs = sorted(glob.glob(os.path.join(folder, "**", "*.csv"), recursive=True))
    others = [p for p in glob.glob(os.path.join(folder, "**", "*"), recursive=True)
              if os.path.isfile(p) and not p.endswith((".xlsx", ".csv"))]

    out.append(f"## Spreadsheets ({len(xlsx)} xlsx, {len(csvs)} csv)\n")
    for path in xlsx:
        rel = os.path.relpath(path, folder)
        if load_workbook is None:
            out.append(f"### {rel} (openpyxl not installed)")
            continue
        try:
            wb = load_workbook(path, read_only=True, data_only=True)
        except Exception as e:
            out.append(f"### {rel} (unreadable: {e})")
            continue
        for ws in wb.worksheets:
            data = list(ws.iter_rows(values_only=True))
            if data:
                _summarize(f"{rel} :: sheet '{ws.title}'", data[0], data[1:], out)
    for path in csvs:
        rel = os.path.relpath(path, folder)
        try:
            with open(path, encoding="utf-8-sig") as f:
                data = list(csv.reader(f))
        except Exception as e:
            out.append(f"### {rel} (unreadable: {e})")
            continue
        if data:
            _summarize(rel, data[0], data[1:], out)

    out.append(f"## Other files ({len(others)}) — not parsed; open with vision if needed")
    for p in others:
        out.append(f"  - {os.path.relpath(p, folder)}")
    return "\n".join(out)


def _load_table(path, sheet):
    if path.endswith(".xlsx"):
        wb = load_workbook(path, read_only=True, data_only=True)
        ws = wb[sheet] if sheet else wb.worksheets[0]
        data = list(ws.iter_rows(values_only=True))
    else:
        with open(path, encoding="utf-8-sig") as f:
            data = list(csv.reader(f))
    return [_cell(h).strip() for h in data[0]], data[1:]


def group_sum(path, sheet, key, val, n=8):
    """Group rows by the `key` column and sum the `val` column. The analyst picks
    which columns these are (by meaning); the script just does the arithmetic."""
    headers, rows = _load_table(path, sheet)
    ki, vi = headers.index(key), headers.index(val)
    agg = defaultdict(float)
    for r in rows:
        if ki < len(r) and vi < len(r):
            x = _num(r[vi])
            if x is not None:
                agg[_cell(r[ki])] += x
    return sorted(agg.items(), key=lambda x: -x[1])[:n]


if __name__ == "__main__":
    if len(sys.argv) >= 6 and sys.argv[1] == "--group":
        # read_folder.py --group <file> <sheet|""> <label_header> <value_header>
        for k, v in group_sum(sys.argv[2], sys.argv[3] or None, sys.argv[4], sys.argv[5]):
            print(f"{k}\t{round(v)}")
    elif len(sys.argv) >= 2:
        print(read_folder(sys.argv[1]))
    else:
        print("usage: read_folder.py <folder>  |  read_folder.py --group <file> <sheet> <label> <value>",
              file=sys.stderr)
        sys.exit(2)
