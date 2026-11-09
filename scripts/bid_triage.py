#!/usr/bin/env python3
"""Xtra Hands Bid Triage — demo-first.

Default: write a fixed Capital Region demo pack to data/triage_DATE.json.
Pass --live to hit the public pages (still a stub parser).
"""
import json
import os
import sys
from datetime import datetime

VPP_DISCOUNT = {"lumber": 0.15, "concrete": 0.12, "excavation": 0.18}
MARGIN_GO = 0.35
MARGIN_MARGINAL = 0.20

SOURCES = {
    "albany_city": "https://www.albanyny.gov/Bids.aspx",
    "albany_schools": "https://www.albanyschools.org/business/bids",
    "schenectady": "https://www.schenectadycountyny.gov/current-bids",
}

DEMO = [
    {
        "title": "City of Albany — sidewalk restoration, Ward 6",
        "url": "https://www.albanyny.gov/Bids.aspx#demo-sidewalk",
        "source": "albany_city",
        "type": "job",
        "category": "excavation",
        "bid_ceiling": 42000,
        "vpp_assumed": 18000,
        "labor_equip": 12000,
        "surplus": "concrete + rebar",
    },
    {
        "title": "Schenectady County — garage demo + haul, Glenville",
        "url": "https://www.schenectadycountyny.gov/current-bids#demo-garage",
        "source": "schenectady",
        "type": "job",
        "category": "excavation",
        "bid_ceiling": 18500,
        "vpp_assumed": 4000,
        "labor_equip": 7000,
        "surplus": "metal, timber, fill",
    },
    {
        "title": "Albany Schools — epoxy gym floor materials",
        "url": "https://www.albanyschools.org/business/bids#demo-epoxy",
        "source": "albany_schools",
        "type": "product",
        "category": "lumber",
        "bid_ceiling": 15000,
        "vpp_assumed": 10000,
        "labor_equip": 500,
        "surplus": "none",
    },
    {
        "title": "DASNY / OPWDD dental clinic reno — post-bid scrap",
        "url": "https://www.dasny.org/opportunities#demo-opwdd",
        "source": "dasny",
        "type": "job",
        "category": "excavation",
        "bid_ceiling": 8000,
        "vpp_assumed": 500,
        "labor_equip": 2500,
        "surplus": "plumbing, copper, fixtures",
    },
]


def estimate_margin(bid):
    disc = VPP_DISCOUNT.get(bid.get("category", "lumber"), 0.10)
    material = bid.get("vpp_assumed", 10000) * (1 - disc)
    total = material + bid.get("labor_equip", 5000)
    ceiling = bid.get("bid_ceiling", 15000)
    profit = ceiling - total
    margin = profit / ceiling if ceiling else 0
    if margin >= MARGIN_GO:
        decision = "GO"
    elif margin >= MARGIN_MARGINAL:
        decision = "MARGINAL"
    else:
        decision = "NO-GO"
    return {
        "decision": decision,
        "margin": round(margin, 3),
        "vpp_cost": round(material, 2),
        "total_cost": round(total, 2),
        "profit": round(profit, 2),
    }


def scrape_live():
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("live scrape needs requests + bs4; falling back to demo")
        return []
    out = []
    for name, url in SOURCES.items():
        try:
            r = requests.get(url, headers={"User-Agent": "XtraHands-BidTriage/1.0"}, timeout=15)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            if name == "albany_city":
                # Parse CivicEngage bid list
                rows = soup.select("div.listItemsRow.bid")
                for row in rows:
                    title_a = row.select_one("div.bidTitle a")
                    if not title_a:
                        continue
                    title = title_a.get_text(strip=True)
                    href = title_a.get("href", "")
                    full_url = url.split("?")[0].rsplit("/", 1)[0] + "/" + href if href.startswith("bids.aspx") else url
                    status_div = row.select_one("div.bidStatus")
                    closes = "unknown"
                    status = "Open"
                    if status_div:
                        spans = status_div.find_all("span")
                        for i, sp in enumerate(spans):
                            if "Closes:" in sp.get_text() and i + 1 < len(spans):
                                # next sibling block has the date
                                pass
                        # simpler: get all text
                        text = status_div.get_text(" ", strip=True)
                        if "Open" in text:
                            status = "Open"
                        # extract date-like
                        import re
                        m = re.search(r"(\d{1,2}/\d{1,2}/\d{4}.*?PM|AM)", text)
                        if m:
                            closes = m.group(1)
                    out.append({
                        "title": title,
                        "url": full_url,
                        "source": name,
                        "type": "job" if any(k in title.lower() for k in ["snow", "tree", "sidewalk", "demo", "transfer"]) else "product",
                        "category": "excavation" if any(k in title.lower() for k in ["snow", "transfer", "demo"]) else "lumber",
                        "bid_ceiling": 25000,  # placeholder until spec
                        "vpp_assumed": 12000,
                        "labor_equip": 6000,
                        "surplus": "possible fill/debris" if "demo" in title.lower() or "transfer" in title.lower() else "unknown",
                        "closes": closes,
                        "status": status,
                    })
            else:
                # stub for other sources until parser written
                out.append({
                    "title": f"LIVE STUB {name} (parser pending)",
                    "url": url,
                    "source": name,
                    "type": "product",
                    "category": "lumber",
                    "bid_ceiling": 15000,
                    "vpp_assumed": 10000,
                    "labor_equip": 5000,
                    "surplus": "unknown",
                })
        except Exception as e:
            print("scrape fail", name, e)
    return out


def main():
    live = "--live" in sys.argv
    pack = scrape_live() if live else DEMO
    if not pack:
        pack = DEMO
        print("empty live result, using DEMO")
    results = []
    for bid in pack:
        row = {**bid, **estimate_margin(bid)}
        results.append(row)
        print(f"[{row['decision']}] {row['margin']:>5}  {row['title']}")
    os.makedirs("data", exist_ok=True)
    path = f"data/triage_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print("wrote", os.path.abspath(path))


if __name__ == "__main__":
    main()
