# Niche research framework — what should THIS business's dashboard show?

A great dashboard isn't a fixed set of cards. A clinic owner, a litigator, and a
SaaS founder make different decisions, so they need different numbers. This is the
**method** for figuring out what matters for whatever niche is in front of you —
so you never need a closed list of industries. Apply it to the niche the user
confirmed in step 3.

**Start from decisions, not metrics.** The mistake is to ask "what can I measure?"
and show all of it. Instead ask "what does the owner of this kind of business
*decide*, and what number would change that decision?" That number earns a place
on the dashboard; everything else is noise. This is the same decision-backward
logic as [financial-analysis.md](financial-analysis.md) — read that for how the
universal ratio families map to decisions; this file is about the niche-specific
layer on top.

Answer from your own business knowledge first. Use `WebSearch` only to fill a gap
or sanity-check the standard metrics of an unfamiliar niche (e.g. "key KPIs for a
veterinary clinic", "SaaS dashboard metrics benchmarks"). Keep research light —
two or three questions answered well beats a survey.

## The five questions (ask these about any niche)

1. **What does the owner decide, and what informs it?** Start here. The recurring
   decisions — chase this balance, drop that service, hire, restock, raise prices
   — are the spine. Each one points to a metric. Those metrics are your headline
   cards. Work backward from the decision to the number, not forward from the data.
2. **What is the value engine?** How does this business actually make money — per
   visit/service, billable hours, product sales, recurring subscriptions, projects?
   This decides whether revenue should be shown per-visit, per-matter, per-SKU, or
   as MRR.
3. **What are the key risks and levers?** Where does money leak or growth come
   from in this niche — no-shows, churn, idle capacity, dead stock, write-offs?
   These are the early-warning metrics the owner acts on before it hurts.
4. **What are the standard health metrics for this niche?** What would an
   experienced operator or an industry benchmark report track? (e.g. utilization,
   retention, turnover, churn.) Use benchmarks to flag outliers, not to grade.
5. **What's NOT worth showing here?** A good dashboard omits. If a metric doesn't
   inform a decision for this niche, leave it out rather than pad the page.

## Turning answers into the dashboard

- The decisions + the numbers that inform them (Q1) → headline KPI cards, capped
  at ~5–8 so each stays salient.
- The value engine (Q2) → how revenue is broken down (by service / matter / SKU /
  plan / month).
- The risks/levers (Q3) → the `niche_kpis` section (e.g. no-show rate, churn,
  utilization), **only if the files contain the data to compute them faithfully**.
- The health metrics (Q4) → ratios worth surfacing, and the benchmark to compare
  against (lightly — "lower than typical", never a grade).
- Each finding that points to an action → a grounded entry in `recommendations`
  (see the contract in [financial-analysis.md](financial-analysis.md): cite the
  metric, be specific, mark as advice, never invent the trigger).
- Q5 → what you deliberately leave off.

Always keep the universal financial core (cash, revenue, profit, AR, AP) — every
business has it. The niche work decides what to add and emphasize around it.

## Illustrations (the method, not a menu)

These show the *same five questions* producing different dashboards. They are
examples to learn the method from — not a list to pick from. A real niche may be
none of these, and you research it the same way.

- **Aesthetics/wellness clinic:** decisions = chase unpaid balances, drop/keep a
  treatment, fill idle chair time; value engine = paid treatments + product sales;
  risks = no-shows and cancellations, idle time; health metrics = average ticket,
  treatment mix, rebooking/repeat rate. Omit: inventory turnover (minor).
- **Law / accounting firm:** decisions = bill unbilled time, chase slow payers,
  staff matters; value engine = billable hours + retainers; risks = unbilled WIP,
  slow collections; metrics = utilization, realization rate, AR aging. Omit:
  product margins (none).
- **E-commerce / retail:** decisions = restock/clear, reprice, cut returns; value
  engine = product sales; risks = dead stock, returns; metrics = AOV, inventory
  turnover, product margin, repeat-purchase.
- **SaaS / subscriptions:** decisions = where to spend on retention vs
  acquisition; value engine = recurring revenue; risks = churn; metrics = MRR/ARR,
  churn, net revenue retention, CAC/LTV. Omit: per-unit COGS.
- **Marketing / creative agency:** decisions = staff vs pipeline, fire/keep a
  client; value engine = retainers + project fees; risks = scope creep, client
  concentration; metrics = billable utilization, project margin, pipeline.
  Separate pass-through ad spend from agency fees.

If the business is a vet, a gym, a restaurant, a freelancer, a manufacturer —
anything — you don't look it up first. You ask the five questions, research lightly
if needed, and compose accordingly.

## Faithfulness still rules

A niche metric only goes on the dashboard if the files support computing it.
Wanting to show "churn" doesn't conjure churn data. If it isn't there, say so and
leave it out — an honest niche-aware dashboard beats an impressive fabricated one.
And a recommendation only exists if the metric behind it does (see the contract in
[financial-analysis.md](financial-analysis.md)).
