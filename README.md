# Xtra Hands Bid Triage

Demo-first. Writes `data/triage_YYYY-MM-DD.json`.

```bash
cd /root/xtra-hands-bid-triage
git pull
python3 scripts/bid_triage.py          # four demo bids, no network
python3 scripts/bid_triage.py --live   # stub hits public pages, falls back

cd /root/xtra-hands-ledger
python3 watch_bids.py
```
