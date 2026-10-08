"""Render a KPI JSON (findings.json, written by the skill) into a beautiful, self-contained
HTML dashboard. Rubik, RTL, premium light theme, inline charts. Numbers come
straight from the JSON — the renderer NEVER invents a value; missing → "חסר נתון".

Usage:  python3 render_dashboard.py <kpi.json> <out.html> ["Business Name"]
"""
import sys, json


CURRENCY_SYMBOLS = {"ILS": "₪", "USD": "$", "EUR": "€", "GBP": "£"}
_SYM = "₪"
NO_DATA = "חסר נתון"


def _n(v):
    """Coerce to a number, or None. Never raises: a bad value is missing data."""
    if v is None or v == "":
        return None
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return v
    try:
        t = str(v)
        for ch in (",", "₪", "$", "€", "£", '\u05e9"\u05d7'):
            t = t.replace(ch, "")
        return float(t.strip())
    except ValueError:
        return None


def shekel(v):
    v = _n(v)
    return NO_DATA if v is None else _SYM + format(int(v), ",")


def render(kpi, business):
    global _SYM
    _SYM = CURRENCY_SYMBOLS.get(str(kpi.get("currency") or "ILS").upper(), "₪")
    sym = _SYM

    by_year = {k: _n(v) for k, v in (kpi.get("revenue_by_year") or {}).items()}
    by_year = {k: v for k, v in by_year.items() if v is not None}
    by_month = {k: _n(v) for k, v in (kpi.get("revenue_by_month") or {}).items()}
    by_month = {k: v for k, v in by_month.items() if v is not None}
    top = [(n, _n(v)) for n, v in (kpi.get("top_items") or []) if _n(v) is not None]
    exp = kpi.get("expenses") or kpi.get("expenses_from_bank") or []
    if isinstance(exp, dict):
        exp = list(exp.items())
    exp = [(n, _n(v)) for n, v in exp if _n(v) is not None]

    # AR/AP/cash may legitimately be absent. null must render, never crash.
    ar = _n(kpi.get("ar_total"))
    ap = _n(kpi.get("ap_total"))
    rev = _n(kpi.get("revenue_total")) or 0
    cogs_raw = _n(kpi.get("cogs_total"))
    cogs = cogs_raw or 0
    margin = _n(kpi.get("gross_margin_pct"))
    # Only claim a margin when cost of goods is actually in the files. Otherwise a
    # business with no COGS column silently reports a fabricated 100%.
    if margin is None and rev and cogs_raw is not None:
        margin = round((rev - cogs) / rev * 100, 1)
    top_label = kpi.get("top_items_label") or "השירותים המובילים לפי הכנסה"

    maxY = max(by_year.values()) if by_year else 1
    maxM = max(by_month.values()) if by_month else 1
    maxT = (top[0][1] if top else 1) or 1
    maxE = max((v for _lbl, v in exp), default=1) or 1

    year_bars = "".join(
        f'<div class="bar{" peak" if v==maxY else ""}"><i style="height:{round(v/maxY*100)}%"></i>'
        f'<b>{sym}{v/1000:.0f}k</b><span>{y}</span></div>' for y, v in by_year.items())
    month_bars = "".join(
        f'<div class="mb" title="{m}: {sym}{v:,.0f}"><i style="height:{max(4,round(v/maxM*100))}%"></i></div>'
        for m, v in by_month.items())
    top_rows = "".join(
        f'<div class="rl"><div class="t"><b>{n}</b><span>{sym}{v:,.0f}</span></div>'
        f'<div class="tr"><i style="width:{round(v/maxT*100)}%"></i></div></div>' for n, v in top)
    exp_rows = "".join(
        f'<div class="rl"><div class="t"><b>{n}</b><span>{sym}{int(v):,}</span></div>'
        f'<div class="tr"><i style="width:{round(v/maxE*100)}%;background:var(--ink-soft)"></i></div></div>'
        for n, v in exp)
    months_span = ""
    if by_month:
        keys = list(by_month)
        months_span = f"{keys[0]} – {keys[-1]}"

    niche = kpi.get("niche") or ""
    nk = kpi.get("niche_kpis") or []
    niche_cards = "".join(
        f'<div class="kpi"><div class="l">{k.get("label", "")}</div>'
        f'<div class="v">{k.get("value", NO_DATA)}</div>'
        f'<div class="l" style="margin-top:4px;font-size:11px">{k.get("note", "")}</div></div>'
        for k in nk)
    niche_band = (
        f'<div style="margin:6px 0 18px"><h3 style="font-size:14px;color:var(--ink-soft);'
        f'font-weight:600;margin-bottom:12px">מדדי הנישה{(" · " + niche) if niche else ""}</h3>'
        f'<div class="kpis">{niche_cards}</div></div>') if nk else ""

    # Ratios — analyst figures (label / value / note). Rendered as compact pills.
    ratios = kpi.get("ratios") or []
    ratio_cards = "".join(
        f'<div class="ratio"><div class="rv">{r.get("value", NO_DATA)}</div>'
        f'<div class="rlbl">{r.get("label", "")}</div>'
        f'<div class="rnote">{r.get("note", "")}</div></div>' for r in ratios)
    ratio_band = (
        f'<div class="card" style="margin-top:16px"><h3>יחסים פיננסיים</h3>'
        f'<div class="ratios">{ratio_cards}</div></div>') if ratios else ""

    # Recommendations — advisory, each anchored to a cited metric. Never fabricated.
    recos = kpi.get("recommendations") or []
    reco_rows = "".join(
        f'<div class="reco"><p>{r.get("text", "")}</p>'
        f'<span class="metric">{r.get("metric", "")}</span></div>' for r in recos)
    reco_section = (
        f'<div class="card recos" style="margin-top:16px"><h3>תובנות והמלצות</h3>'
        f'{reco_rows}<p class="reco-foot">ההמלצות הן עצה מקצועית ולא נתון. בינה מלאכותית '
        f'עלולה לטעות, יש לבדוק אותה בקפידה.</p></div>') if recos else ""

    return f"""<!doctype html>
<html dir="rtl" lang="he"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{business} · דשבורד פיננסי</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<style>
:root{{--bg:#f4f5f7;--card:#fff;--ink:#1d2230;--ink-soft:#8b93a7;--muted:#aeb4c2;
--rose:#c08868;--rose-deep:#a96a4c;--gold:#c9a86a;--line:rgba(29,34,48,.08);--shadow:0 16px 44px -26px rgba(29,34,48,.5);}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--ink);font-family:"Rubik",sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1100px;margin:0 auto;padding:40px 28px 90px}}
.head{{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:12px;margin-bottom:28px}}
.head .ttl{{font-size:30px;font-weight:800;letter-spacing:-.01em}}
.head .ttl span{{color:var(--rose)}}
.head .meta{{font-size:13px;color:var(--ink-soft)}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-bottom:18px}}
.kpi{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:var(--shadow)}}
.kpi .l{{font-size:12.5px;color:var(--ink-soft)}}
.kpi .v{{font-size:27px;font-weight:700;margin-top:6px;letter-spacing:-.01em}}
.kpi .v small{{font-size:14px;color:var(--ink-soft);font-weight:500}}
.kpi.hero{{background:linear-gradient(135deg,#23283a,#161a26);color:#fff;border:none}}
.kpi.hero .l{{color:#aab2c8}} .kpi.hero .v{{color:#fff}}
.grid{{display:grid;grid-template-columns:1.5fr 1fr;gap:16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;box-shadow:var(--shadow)}}
.card h3{{font-size:14px;font-weight:600;color:var(--ink-soft);margin-bottom:18px;letter-spacing:.02em}}
.bars{{display:flex;align-items:flex-end;gap:18px;height:170px}}
.bar{{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;height:100%;justify-content:flex-end}}
.bar i{{width:100%;background:linear-gradient(180deg,var(--rose),var(--gold));border-radius:7px 7px 0 0}}
.bar.peak i{{background:linear-gradient(180deg,var(--rose-deep),var(--rose))}}
.bar b{{font-size:13px;font-weight:600}} .bar span{{font-size:12px;color:var(--muted)}}
.spark{{display:flex;align-items:flex-end;gap:3px;height:90px;margin-top:8px}}
.mb{{flex:1;display:flex;align-items:flex-end;height:100%}}
.mb i{{width:100%;background:var(--rose);opacity:.55;border-radius:2px 2px 0 0}}
.spark-cap{{font-size:11px;color:var(--muted);margin-top:8px}}
.rl{{margin-bottom:13px}}
.rl .t{{display:flex;justify-content:space-between;font-size:13.5px;margin-bottom:5px}}
.rl .t span{{color:var(--ink-soft)}}
.rl .tr{{height:8px;background:#eceef3;border-radius:99px;overflow:hidden}}
.rl .tr i{{display:block;height:100%;background:var(--rose);border-radius:99px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}}
.ratios{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}}
.ratio{{background:#fafbfc;border:1px solid var(--line);border-radius:12px;padding:14px 16px}}
.ratio .rv{{font-size:22px;font-weight:700;letter-spacing:-.01em}}
.ratio .rlbl{{font-size:13px;color:var(--ink);margin-top:2px}}
.ratio .rnote{{font-size:11px;color:var(--muted);margin-top:3px}}
.recos .reco{{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;
padding:13px 0;border-bottom:1px solid var(--line)}}
.recos .reco:last-of-type{{border-bottom:none}}
.recos .reco p{{font-size:14px;line-height:1.5;margin:0;flex:1}}
.recos .metric{{flex:none;font-size:11.5px;color:var(--rose-deep);background:rgba(192,136,104,.1);
border-radius:99px;padding:4px 11px;white-space:nowrap;font-weight:600}}
.recos .reco-foot{{font-size:11.5px;color:var(--muted);margin-top:14px}}
.foot{{margin-top:26px;font-size:12px;color:var(--muted);text-align:center}}
@media(max-width:780px){{.grid,.two{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="wrap">
  <div class="head">
    <div class="ttl">{business} · <span>דשבורד פיננסי</span></div>
    <div class="meta">{(niche + " · ") if niche else ""}{months_span} · {kpi.get('invoice_count','')} חשבוניות · נאמן למקור</div>
  </div>
  <div class="kpis">
    <div class="kpi hero"><div class="l">מזומן בבנק</div><div class="v">{shekel(kpi.get('cash_balance'))}</div></div>
    <div class="kpi"><div class="l">הכנסות מצטברות</div><div class="v">{shekel(kpi.get('revenue_total'))}</div></div>
    <div class="kpi"><div class="l">רווח גולמי</div><div class="v">{shekel(rev-cogs) if rev else NO_DATA} <small>{str(margin)+'%' if margin is not None else ''}</small></div></div>
    <div class="kpi"><div class="l">חייבים (AR)</div><div class="v">{shekel(ar)}</div></div>
    <div class="kpi"><div class="l">ספקים (AP)</div><div class="v">{shekel(ap)}</div></div>
  </div>
  {niche_band}
  <div class="grid">
    <div class="card"><h3>הכנסות לפי שנה</h3><div class="bars">{year_bars}</div>
      <div class="spark">{month_bars}</div><div class="spark-cap">הכנסות חודשיות ({len(by_month)} חודשים)</div></div>
    <div class="card"><h3>{top_label}</h3>{top_rows}</div>
  </div>
  <div class="two">
    <div class="card"><h3>הוצאות עיקריות (מתנועות בנק)</h3>{exp_rows}</div>
    <div class="card"><h3>יחס חייבים / ספקים</h3>
      <div class="rl"><div class="t"><b>חייבים לנו (AR)</b><span>{shekel(ar)}</span></div><div class="tr"><i style="width:100%"></i></div></div>
      <div class="rl"><div class="t"><b>אנחנו חייבים (AP)</b><span>{shekel(ap)}</span></div><div class="tr"><i style="width:{round(min((ap or 0)/max(ar or 1,1),1)*100)}%;background:var(--ink-soft)"></i></div></div>
      <p style="font-size:13px;color:var(--ink-soft);margin-top:10px">מאזן נטו לטובת העסק: {shekel((ar or 0)-(ap or 0))}</p>
    </div>
  </div>
  {ratio_band}
  {reco_section}
  <div class="foot">נוצר אוטומטית מקבצי העסק ״{business}״</div>
</div></body></html>"""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: render_dashboard.py <kpi.json> <out.html> [business]", file=sys.stderr)
        sys.exit(2)
    kpi = json.load(open(sys.argv[1], encoding="utf-8"))
    business = sys.argv[3] if len(sys.argv) > 3 else "העסק"
    open(sys.argv[2], "w", encoding="utf-8").write(render(kpi, business))
    print("dashboard ->", sys.argv[2])
