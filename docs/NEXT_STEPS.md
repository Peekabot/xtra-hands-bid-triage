# Xtra Hands — Smallest Actionable Steps

**Updated: 2026-11-14 (live scrape confirmed)**

Current state: Albany live parser works (4 open bids parsed correctly). Demo pack + sidewalk material list ready. Ledger ingest ready. Priority: lock one real cost + decide on imminent close dates.

## Live Albany bids (confirmed 2026-11-14 via https://www.albanyny.gov/Bids.aspx)

| Bid | Closes | Fit for XtraHands? | Notes |
|-----|--------|--------------------|-------|
| City of Albany Transfer Station | 11/17/2026 11:59 PM | Possible (site/materials) | Needs Plan Holders Form for PDF |
| Snow Management Services - ZONE E | 11/17/2026 11:59 PM | Low (seasonal service) | Closes Monday |
| Street Tree Planting Program | 12/8/2026 11:59 PM | Possible (site prep) | More time |
| RFP 2025-15 Purchase of 96 4th St Bath house NO.2 | 11/27/2026 2:00 PM | Low (property purchase) | — |

Note: Full specs require Plan Holders Form (company name, contact, phone, email).

## Immediate (next 15–30 min)

1. **Decide on the two Monday-closing bids**
   - Open each: Transfer Station (bids.aspx?bidID=780) and Snow ZONE E (bids.aspx?bidID=783)
   - Submit Plan Holders Form if you want the PDF
   - Quick GO/NO-GO: does it match site prep / demo / handyman + surplus potential?

2. **Lock one material cost (sidewalk path still valid)**
   - Use `data/sidewalk_material_list.md` (or any real quantities from a spec)
   - Email or walk to Capital Region HD Pro Desk (Latham #1259 or Schenectady #1239)
   - Request Bid Room / VPP quote
   - Save the confirmation

3. **Run live triage once**
   - `python3 scripts/bid_triage.py --live`
   - Confirm JSON written with real titles + close dates

## This week

4. Update `VPP_DISCOUNT` / `vpp_assumed` with the real Pro Desk number
5. Ingest triage JSON into ledger (`watch_bids.py` in xtra-hands-ledger)
6. For any surplus-heavy lead, note it for surplus-capture skill

## Constants to tune after real quote
- VPP_DISCOUNT
- MARGIN_GO = 0.35
- MARGIN_MARGINAL = 0.20

**Rule remains:** Never submit until cost is locked in writing.
