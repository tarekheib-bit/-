# Financial analysis — from numbers to decisions

Read this when you've normalized the files into facts and now have to decide
**what the dashboard should say** — not just which figures exist, but what they
mean for the person running the business. A dashboard that lists numbers is a
report. A dashboard that surfaces *the decision the numbers are pointing to* is
worth building. This guide is the analyst's lens for getting there.

It is a way of reasoning, not a formula sheet. Every ratio below is here because
it answers a **decision question** an owner actually faces. If a ratio doesn't
change a decision for the business in front of you, leave it off — see
[niche-research.md](niche-research.md) for choosing what matters per niche.

## Work backward from the decision

The instinct is to compute every ratio you can and show them all. Resist it.
Start from the other end: **what does the owner of this business decide, and what
would make them decide differently?** A clinic owner decides whether to chase
unpaid balances, whether to drop an underperforming treatment, whether they can
afford another therapist. Each decision is informed by one or two numbers. Those
numbers are your dashboard; the rest is noise.

So the chain runs: *owner's recurring decisions → the metric that informs each →
is that metric derivable from the files?* If yes, it's a headline. If the files
can't support it, say so and move on — never fabricate a number to fill a slot.

This is also why the dashboard caps at roughly **five to eight headline figures**.
Beyond that, nothing is salient and every number competes with every other. A
focused dashboard is a design choice, not a limitation.

## The ratio families (each tied to a decision)

For each family: what it measures, the **decision question** it answers, and the
**recommendation pattern** when it comes out wrong. The recommendation is always
advisory and always anchored to the specific figure that triggered it — never a
generic platitude.

### 1. Liquidity — "can the business pay what's due soon?"
- **Measures:** short-term solvency. Current ratio = current assets / current
  liabilities; quick ratio excludes inventory.
- **Decision question:** do I have enough cash and near-cash to cover what I owe
  in the next stretch, or do I need to slow payments / chase receivables / hold a
  buffer?
- **Recommendation pattern when off:** a thin cash position next to a large
  payables balance → "מזומן (₪X) מכסה רק חלק מההתחייבויות הקרובות (₪Y); שקול
  להאיץ גבייה מחייבים או לפרוס תשלום לספקים." Anchor to the two real figures.

### 2. Profitability — "is the work actually making money?"
- **Measures:** gross margin = (revenue − COGS) / revenue; net margin after all
  expenses; return on assets where assets are known.
- **Decision question:** which products/services/clients earn their keep, and
  where is effort going into low-margin work?
- **Recommendation pattern when off:** a low or falling gross margin, or one
  service dragging the mix → "המרווח הגולמי (X%) נמוך מהצפוי לנישה; הטיפול/מוצר
  Z תורם נפח אך מרווח נמוך — שקול תמחור מחדש או מיקוד בשירותים רווחיים." Name the
  service and cite its share.

### 3. Efficiency — "is capital tied up where it shouldn't be?"
- **Measures:** how fast assets convert to cash. AR turnover and **DSO** (days
  sales outstanding ≈ AR / revenue × period-days); inventory turnover and days on
  hand; asset utilization.
- **Decision question:** is money sitting in unpaid invoices or dead stock instead
  of in the bank?
- **Recommendation pattern when off:** high DSO or a large AR balance relative to
  revenue → "חייבים (₪X) שווים ל-N ימי מכירות; הידוק תנאי גבייה ישחרר מזומן."
  For stock: "מלאי בשווי ₪X מסתובב לאט; שקול לצמצם הזמנות של פריטים תקועים."

### 4. Leverage — "how exposed is the business to its debts?"
- **Measures:** debt / equity; interest coverage; DSCR (operating cash / debt
  service).
- **Decision question:** can the business safely take on (or must it pay down)
  debt, and can it service what it already owes?
- **Recommendation pattern when off:** coverage below comfort → "תזרים התפעולי
  מכסה את שירות החוב פי X בלבד; היזהר מהתחייבויות נוספות עד שהכיסוי משתפר."
  For most small service businesses leverage data simply isn't in the files —
  then this family is "אין נתון", not a guess.

### 5. Cash flow — "where is cash coming from and going to?"
- **Measures:** operating cash trend, the gap between profit and cash, seasonality
  of inflows.
- **Decision question:** is the business converting profit into cash, and can it
  fund the next slow month?
- **Recommendation pattern when off:** profit healthy but cash flat (money stuck
  in AR/stock), or a clear seasonal trough → "ההכנסות חזקות אך המזומן לא גדל
  בהתאם — הפער יושב בחייבים; ראה המלצת הגבייה." Tie cash advice back to the
  efficiency finding rather than repeating it.

## How a recommendation must be built (the contract)

A recommendation that isn't grounded is worse than no recommendation — it sounds
authoritative and may be wrong. So each one must:

1. **Cite the metric that triggered it** — the reader can see *why* you're saying
   it (e.g. "gross margin 77%", "AR = 65 days of sales").
2. **Be specific to this business** — name the treatment, the client, the month.
   "Improve margins" helps no one; "treatment Z is 22% of volume at a thin
   margin" does.
3. **Be marked as advice, not fact** — it's a suggested action ("שקול", "כדאי
   לבחון"), distinct from the audited numbers. The numbers are certain; the
   recommendation is judgment.
4. **Never invent the trigger.** If the data can't compute the ratio, there's no
   recommendation. You don't recommend tightening collections if there's no AR
   data — you say AR is "אין נתון".

Aim for **two to four** recommendations, the ones that would genuinely change a
decision. A wall of advice dilutes the one thing that matters.

## Benchmarks: use as a sniff test, not a verdict

You may know, or look up, that a niche typically runs a certain margin or DSO.
Use that to *flag* an outlier worth a recommendation — not to assert the business
is "doing badly". Benchmarks vary by size, region, and model. Frame as "lower than
typical for this niche, worth examining", never as a graded score. When you pull a
benchmark from research, the niche-research framework already covers how light to
keep it.

## The faithfulness contract still rules

Every ratio is computed from cited figures; every figure traces to source rows. A
ratio you can't compute faithfully is "אין נתון" and the recommendation that would
have rested on it simply isn't made. An honest, partial analysis beats an
impressive, fabricated one — the whole value of the dashboard is that the owner
can trust it enough to act on it.
