#!/usr/bin/env python3
"""Step 1 -- draw a random sample of arXiv submissions per (category, month).

Metadata only, from the official arXiv API (export.arxiv.org), which the API
terms ask us to hit no faster than once every 3 seconds with a descriptive
User-Agent.  We page through EVERY submission in the month for the requested
category, keep only those whose *primary* category is the one we want (so the
sample is "papers submitted to quant-ph", not "papers cross-listed anywhere
near it"), and then draw a reproducible random sample with a fixed seed.

Output: data/listings/<cat>_<YYYY-MM>.json
"""

from __future__ import annotations

import json
import random
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

ROOT = Path(__file__).parent
LIST = ROOT / "data" / "listings"

UA = ("arxiv-ack-survey/1.0 (academic one-off survey of LLM acknowledgments; "
      "contact tobias.j.osborne@gmail.com)")
API = "http://export.arxiv.org/api/query"
DELAY = 3.1          # arXiv API guidance: >= 1 request / 3 s
PAGE = 500
SEED = 20260827

NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

# math-ph and math.MP are the same archive under two names; either may appear
# as the primary category, and both mean "submitted to math-ph".
PRIMARY_OK = {
    "quant-ph": {"quant-ph"},
    "math-ph": {"math-ph", "math.MP"},
}

# Quarterly, Jan 2023 (two months after ChatGPT) through Jul 2026.
MONTHS = [
    (2023, 1), (2023, 4), (2023, 7), (2023, 10),
    (2024, 1), (2024, 4), (2024, 7), (2024, 10),
    (2025, 1), (2025, 4), (2025, 7), (2025, 10),
    (2026, 1), (2026, 4), (2026, 7),
]

TARGET_N = 120       # sampled papers per (category, month)


def month_range(y: int, m: int) -> tuple[str, str]:
    ny, nm = (y + 1, 1) if m == 12 else (y, m + 1)
    return f"{y:04d}{m:02d}010000", f"{ny:04d}{nm:02d}010000"


def api_page(cat: str, lo: str, hi: str, start: int, session: requests.Session):
    q = f"cat:{cat} AND submittedDate:[{lo} TO {hi}]"
    params = {"search_query": q, "start": start, "max_results": PAGE,
              "sortBy": "submittedDate", "sortOrder": "ascending"}
    for attempt in range(6):
        time.sleep(DELAY)
        try:
            r = session.get(API, params=params, timeout=90)
            r.raise_for_status()
            root = ET.fromstring(r.content)
        except Exception as e:                                   # noqa: BLE001
            print(f"    retry {attempt} ({e})", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
            continue
        total = root.find("opensearch:totalResults", {
            "opensearch": "http://a9.com/-/spec/opensearch/1.1/"})
        entries = root.findall("a:entry", NS)
        # The arXiv API intermittently returns an empty page; retry those.
        if not entries and start == 0 and total is not None and int(total.text) > 0:
            time.sleep(6)
            continue
        return entries, (int(total.text) if total is not None else 0)
    return [], 0


def parse(entry) -> dict | None:
    idu = entry.find("a:id", NS).text
    m = re.search(r"abs/([^v]+)v(\d+)", idu)
    if not m:
        return None
    prim = entry.find("arxiv:primary_category", NS)
    return {
        "id": m.group(1),
        "primary": prim.get("term") if prim is not None else "",
        "published": entry.find("a:published", NS).text,
        "title": " ".join((entry.find("a:title", NS).text or "").split()),
        "abstract": " ".join((entry.find("a:summary", NS).text or "").split()),
        "cats": [c.get("term") for c in entry.findall("a:category", NS)],
    }


def main() -> None:
    LIST.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = UA

    for cat in ("quant-ph", "math-ph"):
        for y, mo in MONTHS:
            out = LIST / f"{cat}_{y:04d}-{mo:02d}.json"
            if out.exists():
                print(f"skip {out.name}")
                continue
            lo, hi = month_range(y, mo)
            rows, start, total = [], 0, None
            while True:
                entries, tot = api_page(cat, lo, hi, start, s)
                if total is None:
                    total = tot
                rows += [p for p in map(parse, entries) if p]
                print(f"  {cat} {y}-{mo:02d}: {len(rows)}/{total}")
                if len(entries) < PAGE or (total and start + PAGE >= total):
                    break
                start += PAGE
                if start > 6000:
                    break

            prim = [r for r in rows if r["primary"] in PRIMARY_OK[cat]]
            # Deduplicate (paging can overlap if new papers land mid-crawl).
            seen, uniq = set(), []
            for r in prim:
                if r["id"] not in seen:
                    seen.add(r["id"])
                    uniq.append(r)
            uniq.sort(key=lambda r: r["id"])
            rng = random.Random(f"{SEED}-{cat}-{y}-{mo}")
            sample = rng.sample(uniq, min(TARGET_N, len(uniq)))
            out.write_text(json.dumps({
                "category": cat, "year": y, "month": mo,
                "api_total_incl_crosslist": total,
                "n_primary": len(uniq), "n_sampled": len(sample),
                "seed": SEED, "sample": sample,
            }, indent=1))
            print(f"WROTE {out.name}: primary={len(uniq)} sampled={len(sample)}")


if __name__ == "__main__":
    main()
