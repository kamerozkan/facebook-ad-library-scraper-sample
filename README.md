# Facebook Ad Library Scraper - Competitor Ad Monitor: Samples

Facebook Ad Library scraper and competitor ad monitor for exact Meta Pages. Collect active Facebook and Instagram ads without login or an API key. Export ad copy, links, media and platforms, with verified new, stopped, resumed and asset-change events across runs.

[Run Facebook Ad Library Scraper - Competitor Ad Monitor on Apify](https://apify.com/kamerozkan/facebook-ad-library-change-monitor)

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

## Saved API starter on October 4, 2026

[example_run_input.json](example_run_input.json) is the exact saved API example: one public Page ID from the deployed schema prefill, country `US`, mode `AUTO`, at most ten ads and output mode `ALL_CHECKED`, with baseline inclusion enabled. It replaces an unrelated `helloWorld` placeholder. [Saved/schema evidence](maintenance-verification-2026-10-04.json). No new source run was performed; this does not prove that the public Page currently yields ads.

Use this current file for the examples below. `input.sample.json` and `run_monitor.py` preserve older parameter names and are historical files, not the current quickstart. The output fixture below is also retained as a contract illustration, not relabeled as a fresh result.

## Quickstart (Python)

Install Python client 3.x, set `APIFY_TOKEN` in your environment, then explicitly start a potentially billable run:

```bash
pip install 'apify-client>=3,<4'
```

```python
import json
import os
from datetime import timedelta
from decimal import Decimal
from pathlib import Path
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = json.loads(Path("example_run_input.json").read_text())
run = client.actor("kamerozkan/facebook-ad-library-change-monitor").call(
    run_input=run_input,
    run_timeout=timedelta(seconds=300),
    max_total_charge_usd=Decimal("0.10"),
    logger=None,
)
if not run or run.status != "SUCCEEDED":
    raise RuntimeError("Inspect the run and OUTPUT in Apify Console.")
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item)
```

## Quickstart (Node.js)

```bash
npm install apify-client
```

```javascript
import { readFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = JSON.parse(await readFile('example_run_input.json', 'utf8'));
const run = await client.actor('kamerozkan/facebook-ad-library-change-monitor').call(input, {
    timeout: 300,
    maxTotalChargeUsd: 0.10,
});
if (!run || run.status !== 'SUCCEEDED') throw new Error('Inspect the run and OUTPUT in Apify Console.');
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Choose one client. Each execution starts a separate potentially billable run. The snippets set a paid-event limit, which does not cap all compute/proxy costs. Ten ads is a workload cap. Check `OUTPUT`, actual returned rows and source warnings before treating a result as a complete snapshot or a verified change. These snippets were not executed during the metadata repair.

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
| `pageIds` | Array | Public schema prefill | Exact Meta Page IDs; starter has one. |
| `country` | String | `US` in starter | Country scope for collection. |
| `mode` | Enum | `AUTO` in starter | Collection mode from the deployed input schema. |
| `maxAdsPerPage` | Integer | `10` in starter | Workload cap per requested Page. |
| `outputMode` | Enum | `ALL_CHECKED` in starter | Preserve checked-row output for inspection. |
| `includeBaseline` | Boolean | `true` in starter | Include baseline observations; not a new/change guarantee. |

---

## Links

- **Live Apify Actor:** [https://apify.com/kamerozkan/facebook-ad-library-change-monitor](https://apify.com/kamerozkan/facebook-ad-library-change-monitor)
- **Author Profile:** [https://apify.com/kamerozkan](https://apify.com/kamerozkan)
- **Report Issues / Feedback:** [GitHub Issues](https://github.com/kamerozkan/facebook-ad-library-scraper-sample/issues)
