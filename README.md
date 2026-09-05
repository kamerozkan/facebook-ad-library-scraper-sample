# Facebook Ad Library Scraper & Competitor Monitor Sample

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue?logo=apify)](https://apify.com/kamerozkan/facebook-ad-library-change-monitor)
[![Pricing](https://img.shields.io/badge/Pricing-Pay--Per--Event-brightgreen)](https://apify.com/kamerozkan/facebook-ad-library-change-monitor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Runnable Python and Node.js examples, sanitized outputs, and JSON schema for the [Facebook Ad Library Scraper & Competitor Monitor Apify Actor](https://apify.com/kamerozkan/facebook-ad-library-change-monitor).

Track active ad creatives, copy changes, landing pages, and quiet campaign shutdowns across Facebook and Instagram without API limits.

---

## Key Features

- **Competitor Lifecycle Feeds:** Beyond simple dumps, the Actor emits structured lifecycle events:
  - `NEW_LAUNCH_FEED`: Newly launched ad creatives detected.
  - `VERIFIED_CHANGES`: Verified changes to headline, body text, or destination URL.
  - `STOPPED_ADS`: Ads confirmed halted across repeated observation runs.
- **Canonical Asset Fingerprinting:** Solves the notorious `fbcdn.net` URL-mutation problem (where signed query tokens change on every request). Pure-path and copy hashing prevent false positive alerts.
- **Page ID or Keyword Search:** Monitor exact brand pages or broad industry keywords across any country code (`US`, `GB`, `DE`, etc.).
- **Residential Proxy Routing:** Automatically routes GraphQL requests through dedicated residential proxies to avoid Meta's datacenter IP rate limits.

---

## Quickstart (Python)

Run the competitor monitor using the official `apify-client` Python SDK:

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

# Initialize with your Apify API token
client = ApifyClient("YOUR_APIFY_TOKEN")

# Define target brand or page
run_input = {
    "searchMode": "page",
    "pageId": "40796308305",  # e.g. Coca-Cola
    "countries": ["US"],
    "activeStatus": "ACTIVE",
    "maxAds": 50,
    "feedMode": "DIFF"
}

# Run the Actor and iterate over emitted ad events
run = client.actor("kamerozkan/facebook-ad-library-change-monitor").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"[{item.get('lifecycleEvent')}] Ad {item.get('adArchiveId')} — {item.get('pageName')}")
    print(f"  Title: {item.get('adTitle')}")
    print(f"  CTA: {item.get('callToActionType')} -> {item.get('linkUrl')}")
    print(f"  First Seen: {item.get('firstSeen')} | Last Shown: {item.get('lastShown')}\n")
```

---

## Quickstart (Node.js)

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({
    token: 'YOUR_APIFY_TOKEN',
});

const run = await client.actor('kamerozkan/facebook-ad-library-change-monitor').call({
    searchMode: 'keyword',
    keyword: 'b2b saas',
    countries: ['US', 'GB'],
    maxAds: 25,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Fetched ${items.length} competitor ad creatives:`);
for (const ad of items) {
    console.log(`- [${ad.pageName}] ${ad.adTitle} -> ${ad.linkUrl}`);
}
```

---

## Sample Output Record

```json
{
  "adArchiveId": "104857692014523",
  "pageId": "40796308305",
  "pageName": "The Coca-Cola Company",
  "adTitle": "Taste the Feeling",
  "adBody": "Real Magic happens when we come together. Discover our new summer campaign...",
  "callToActionType": "LEARN_MORE",
  "linkUrl": "https://www.coca-cola.com/us/en",
  "publisherPlatforms": ["FACEBOOK", "INSTAGRAM", "MESSENGER"],
  "mediaType": "VIDEO",
  "videoHdUrl": "https://video.xx.fbcdn.net/v/t42.1790-2/...",
  "imageUrl": "https://scontent.xx.fbcdn.net/v/t39.35426-6/...",
  "canonicalAssetId": "sha256:4a8b79f2e...",
  "firstSeen": "2026-08-20T10:00:00.000Z",
  "lastShown": "2026-09-05T07:30:00.000Z",
  "lifecycleEvent": "VERIFIED_CHANGE",
  "changedFields": ["adBody"]
}
```

---

## Input Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `searchMode` | Enum | `"page"` | Search by `"page"` (specific advertiser) or `"keyword"`. |
| `pageId` | String | `""` | Meta Page ID or profile alias. |
| `keyword` | String | `""` | Search term when in keyword search mode. |
| `countries` | Array | `["US"]` | ISO 2-letter country codes to search. |
| `activeStatus` | Enum | `"ACTIVE"` | `"ACTIVE"`, `"INACTIVE"`, or `"ALL"`. |
| `maxAds` | Integer | `300` | Maximum number of ad creatives to scan per run. |
| `feedMode` | Enum | `"DIFF"` | `"DIFF"` (only emit new/changed/stopped) or `"FULL_SNAPSHOT"`. |

---

## Links

- **Live Apify Actor:** [https://apify.com/kamerozkan/facebook-ad-library-change-monitor](https://apify.com/kamerozkan/facebook-ad-library-change-monitor)
- **Author Profile:** [https://apify.com/kamerozkan](https://apify.com/kamerozkan)
- **Report Issues / Feedback:** [GitHub Issues](https://github.com/kamerozkan/facebook-ad-library-scraper-sample/issues)
