# Xtra Hands Bid Triage System

Procurement intelligence for Capital Region NY government contracting.

**Two-rail system:**
- **Rail A**: RFP / bid scraping engine
- **Rail B**: HD Pro VPP material cost estimation + margin triage (GO / MARGINAL / NO-GO)

## Setup
```bash
cd xtra-hands-bid-triage
pip install -r requirements.txt
python scripts/bid_triage.py
```

## Structure
- `scripts/` — Core Python tools
- `data/` — Generated triage reports
- `docs/` — Documentation
- `attachments/` — Supporting files (quote calculator, pre-dig reports)

See `docs/CONTEXT.md` for full details.