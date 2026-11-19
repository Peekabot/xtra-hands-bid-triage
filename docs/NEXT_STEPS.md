# Xtra Hands — Smallest Actionable Steps

**Updated: 2026-11-19 (live triage + Street Tree evaluation)**

Current state: Albany live parser works (confirmed). Live triage run produced `data/triage_2026-11-19.json`. Street Tree Planting Program evaluated. Priority: lock one real material cost + decide GO/NO-GO on Street Tree labor fit.

## Live Albany bids (confirmed 2026-11-19 via https://www.albanyny.gov/Bids.aspx)

| Bid | Closes | Fit for XtraHands? | Notes |
|-----|--------|--------------------|-------|
| Street Tree Planting Program | 12/8/2026 11:59 PM | Marginal (labor/site prep for planting) | Trees: Amur Maackia, Bur Oak, Canada Red Chokecherry, Catalpa. NAICS forestry/landscaping. Full specs require Plan Holders Form (bidID=782). Low surplus. |
| RFP 2025-15 Purchase of 96 4th St Bath house NO.2 | 11/27/2026 2:00 PM | Low (property purchase) | — |
| RFP 2026-18 Comprehensive Plan Update Services | 12/18/2026 2:00 PM | Low (consulting) | — |

Note: Full specs require Plan Holders Form (company name, contact, phone, email).

## Immediate (next 15–30 min)

1. **Street Tree Planting — decision**
   - Public summary: contractor for planting listed species. Labor-heavy site prep possible; materials are trees (not HD Pro sweet spot).
   - Action: If interested in labor/sub, submit Plan Holders Form at https://www.albanyny.gov/Bids/PlanHolders/782 to get full PDF/spec + quantities. Otherwise mark NO-GO and move on.
   - Surplus: negligible.

2. **Lock one material cost (sidewalk path still valid)**
   - Use `data/sidewalk_material_list.md` (5-line core list ready).
   - Email or walk to Capital Region HD Pro Desk (Latham #1259 or Schenectady #1239).
   - Request Bid Room / VPP quote on the list.
   - Save the confirmation (this unlocks real VPP_DISCOUNT).

3. **Live triage confirmed**
   - `python3 scripts/bid_triage.py --live` ran successfully on 2026-11-19.
   - Albany parser extracted real titles + close dates. Placeholders used for costs until specs locked.
   - JSON written with decisions (placeholders = all GO until real numbers).

## This week

4. Update `VPP_DISCOUNT` / `vpp_assumed` with the real Pro Desk number once quote arrives.
5. Ingest triage JSON into ledger (`watch_bids.py` in xtra-hands-ledger).
6. Check Schenectady open bids (RFB-2026-31 Technical Rescue, RFB-2026-30 Waste Removal) for any site/surplus fit. Improve Schenectady parser.
7. For any surplus-heavy lead, note it for surplus-capture skill.

## Constants to tune after real quote
- VPP_DISCOUNT
- MARGIN_GO = 0.35
- MARGIN_MARGINAL = 0.20

**Rule remains:** Never submit until cost is locked in writing.
