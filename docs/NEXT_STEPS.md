# Xtra Hands — Smallest Actionable Steps

**Updated: 2026-11-18 (post-close check)**

Current state: Albany live parser works. Monday-closing bids (Transfer Station, Snow ZONE E) have closed. Demo pack + sidewalk material list ready. Ledger ingest ready. Priority: evaluate Street Tree Planting + lock one real cost.

## Live Albany bids (confirmed 2026-11-18 via https://www.albanyny.gov/Bids.aspx)

| Bid | Closes | Fit for XtraHands? | Notes |
|-----|--------|--------------------|-------|
| Street Tree Planting Program | 12/8/2026 11:59 PM | Possible (site prep / planting) | Requires Plan Holders Form for PDF (bidID=782) |
| RFP 2025-15 Purchase of 96 4th St Bath house NO.2 | 11/27/2026 2:00 PM | Low (property purchase) | — |
| RFP 2026-18 Comprehensive Plan Update Services | 12/18/2026 2:00 PM | Low (consulting) | — |

Note: Full specs require Plan Holders Form (company name, contact, phone, email).

## Immediate (next 15–30 min)

1. **Evaluate Street Tree Planting Program**
   - Open: https://www.albanyny.gov/bids.aspx?bidID=782
   - Submit Plan Holders Form if you want the full PDF/spec
   - Quick GO/NO-GO: does it match site prep / handyman + any surplus potential? (planting is labor-heavy, materials may be trees/supplies)

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
6. Check Schenectady open bids (RFB-2026-31 Technical Rescue, RFB-2026-30 Waste Removal) for any site/surplus fit
7. For any surplus-heavy lead, note it for surplus-capture skill

## Constants to tune after real quote
- VPP_DISCOUNT
- MARGIN_GO = 0.35
- MARGIN_MARGINAL = 0.20

**Rule remains:** Never submit until cost is locked in writing.
