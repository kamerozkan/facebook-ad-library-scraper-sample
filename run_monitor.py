#!/usr/bin/env python3
"""
Quickstart script to run Facebook Ad Library Scraper & Competitor Monitor on Apify.
Requires: pip install apify-client
"""
import os
import sys
from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
if not APIFY_TOKEN:
    print("Error: Please set APIFY_TOKEN environment variable.")
    print("Example: export APIFY_TOKEN=your_token_here")
    sys.exit(1)

client = ApifyClient(APIFY_TOKEN)

# Example: Monitor Coca-Cola (Page ID 40796308305) in US
run_input = {
    "searchMode": "page",
    "pageId": "40796308305",
    "countries": ["US"],
    "activeStatus": "ACTIVE",
    "maxAds": 25,
    "feedMode": "DIFF"
}

print(f"Starting Facebook Ad Library Monitor for Page '{run_input['pageId']}'...")
run = client.actor("kamerozkan/facebook-ad-library-change-monitor").call(run_input=run_input)

print(f"Run completed with status: {run['status']}")
dataset = client.dataset(run["defaultDatasetId"])

items = list(dataset.iterate_items())
print(f"Captured {len(items)} competitor ad events:\n")

for i, ad in enumerate(items, 1):
    event = ad.get("lifecycleEvent", "SNAPSHOT")
    print(f"[{i}] [{event}] {ad.get('adTitle')} ({ad.get('pageName')})")
    print(f"    CTA: {ad.get('callToActionType')} -> {ad.get('linkUrl')}")
    print(f"    First seen: {ad.get('firstSeen')} | Last shown: {ad.get('lastShown')}\n")
