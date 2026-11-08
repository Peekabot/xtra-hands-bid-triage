# Xtra Hands — Smallest Actionable Steps

Current state: demo-first triage with stub live scraper. Ledger ingest works. Next priority is real VPP quotes and one live bid.

## Immediate (today / next 30 min)

1. **Register on BidNet (free tier)**
   - Open https://www.bidnetdirect.com/new-york
   - Click Register / Create Account
   - Use business email for Couch Potato Holdings LLC / Xtra Hands
   - Confirm email
   - Fill company profile (Albany/Schenectady NY, site prep / demo / handyman)
   - Save login

2. **Check one current Albany bid page**
   - Open https://www.albanyny.gov/Bids.aspx
   - Note open bids: Snow Management Services - ZONE E (closes 11/17/2026), Street Tree Planting Program (closes 12/8/2026)
   - Click into Snow Management or Tree Planting and download the PDF/spec if available
   - Save PDF locally as `data/specs/`

3. **Pick the sidewalk restoration demo as first real test**
   - From DEMO in scripts/bid_triage.py: City of Albany sidewalk restoration, Ward 6
   - Or use real quantities from 2026 Contract 1 (DocumentCenter/View/13942) — temporary sidewalk restoration, concrete sidewalks
   - Build a 5-line material list (concrete, rebar, forms, gravel, etc.)

## Next (this week)

4. **Get one real Pro Desk Bid Room quote**
   - Print or email the material list to Home Depot Pro Desk (Capital Region)
   - Request Bid Room / VPP quote
   - Save the confirmation email
   - Update VPP_DISCOUNT or replace `vpp_assumed` with real numbers in bid_triage.py

5. **Improve live scraper (smallest code step)**
   - In scripts/bid_triage.py `scrape_live()`, parse actual title + close date from the Albany CivicEngage table instead of returning stub
   - Test with `python3 scripts/bid_triage.py --live`

6. **Ingest into ledger**
   - Run triage → `python3 watch_bids.py` in ledger repo
   - Confirm new project + tasks (site-walk, bid, haul, surplus log) appear in projects.db

## Later

7. Decide GO/NO-GO on the first real bid using locked cost
8. Submit interest or bid only after written quote
9. For surplus-heavy jobs (demo), log via surplus-capture skill

## Constants to tune after real quote
- VPP_DISCOUNT
- MARGIN_GO = 0.35
- MARGIN_MARGINAL = 0.20
