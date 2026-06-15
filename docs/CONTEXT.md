# Xtra Hands — Bid Triage System
## Claude Code Upload Context

### Who / What
- **Entity:** Xtra Hands DBA of Couch Potato Holdings LLC (Albany/Schenectady NY)
- **Operator:** Pro associate at Home Depot Capital Region
- **Core edge:** HD Pro VPP pricing + OMNIA Partners public sector contracts

### What this codebase does
Two-rail procurement intelligence system:
1. **Rail A (RFP Engine):** Scrapes public Albany-area bid pages, filters by NIGP trade codes
2. **Rail B (Cost Engine):** Estimates VPP-adjusted material cost, outputs GO/MARGINAL/NO-GO

### Files
```
scripts/
  bid_triage.py     # Main scraper + margin estimator. Run this.
  test_suite.py     # Historical bid test cases. Run to validate.
data/
  triage_YYYY-MM-DD.json   # Auto-generated on each run
docs/
  CONTEXT.md        # This file
```

### Key constants to tune
In `bid_triage.py`:
- `VPP_DISCOUNT` dict — update with real Pro Desk quotes per category
- `MARGIN_GO = 0.35` — raise or lower based on your risk tolerance
- `MARGIN_MARGINAL = 0.20` — floor before walking away
- `SOURCES` dict — add new bid pages as you find them

### Live bid sources (no auth)
| Source | URL |
|---|---|
| Albany City Gov | https://www.albanyny.gov/Bids.aspx |
| Albany City Schools | https://www.albanyschools.org/business/bids |
| Schenectady County | https://www.schenectadycountyny.gov/current-bids |
| BidNet (requires free registration) | https://www.bidnetdirect.com/new-york |

### Two bid types
| Type | Risk | Lock cost via |
|---|---|---|
| Jobs (labor/services) | Time estimate wrong → lose margin | Written sub quotes |
| Product (materials) | Material price wrong → lose margin | HD Pro Bid Room email |

**Rule:** Never submit a bid until cost is locked in writing.

### Bid formula
```
Job bid   = labor + materials + equipment + overhead + margin
Product bid = VPP cost × qty + delivery + margin
Profit    = bid price − your cost
```

### VPP flow
1. Build material list from SOW
2. Bring list to Pro Desk → request Bid Room quote
3. Get email confirmation of price
4. Use that as your cost floor in the bid
5. If bid ceiling > VPP cost + target margin → submit

### OMNIA Partners
- Link USC code to Pro Xtra account
- Unlocks public-sector tier pricing + tax-exempt sync
- Satisfies FAR "reasonable cost" audit requirement automatically

### Next actions
- [ ] BidNet free tier registration
- [ ] Pull one live spec (sidewalk restoration or epoxy flooring)
- [ ] Run actual material list through Pro Desk Bid Room
- [ ] Replace `material_cost_assumption` with real Pro Desk quote
- [ ] Submit first bid

### Dependencies
```
pip install requests beautifulsoup4
```