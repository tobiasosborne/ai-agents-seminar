#!/usr/bin/env python3
"""Step 2 -- get the FULL TEXT of each sampled paper and cache it.

Source: the official arXiv bulk dataset mirrored on Google Cloud Storage
(gs://arxiv-dataset, public, free, maintained by arXiv+Google for exactly this
kind of use).  We deliberately do NOT scrape arxiv.org/e-print, which
arxiv.org/robots.txt disallows -- the GCS bucket is the sanctioned bulk route
and it also lets us parallelise without hammering anyone.

We always take **v1**, the version as originally submitted.  That keeps the
x-axis honest: the measurement is "what the authors wrote when they submitted
in month M", not "what survived refereeing", which would bias old months upward
(they have had years to accumulate revisions) -- or downward (journal AI
disclosure policies only appeared in 2023-24).

PDF -> text via poppler's pdftotext.  Text is cached gzipped; the PDF is
discarded immediately so the cache stays small.
"""

from __future__ import annotations

import gzip
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

ROOT = Path(__file__).parent
LIST = ROOT / "data" / "listings"
TEXT = ROOT / "data" / "text"
STATUS = ROOT / "data" / "fetch_status.json"

UA = ("arxiv-ack-survey/1.0 (academic one-off survey of LLM acknowledgments; "
      "contact tobias.j.osborne@gmail.com)")
GCS = "https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf"
MAX_BYTES = 40 * 1024 * 1024
WORKERS = 32

_local = None


def session() -> requests.Session:
    global _local
    import threading
    if _local is None:
        _local = threading.local()
    if not hasattr(_local, "s"):
        _local.s = requests.Session()
        _local.s.headers["User-Agent"] = UA
    return _local.s


def gcs_pdf(arxiv_id: str) -> bytes | None:
    """v1 if we can get it; fall back to the next few versions."""
    yymm = arxiv_id.split(".")[0]
    s = session()
    for v in (1, 2, 3, 4):
        url = f"{GCS}/{yymm}/{arxiv_id}v{v}.pdf"
        try:
            r = s.get(url, timeout=120, stream=True)
        except Exception:                                        # noqa: BLE001
            continue
        if r.status_code == 404:
            r.close()
            continue
        if r.status_code != 200:
            r.close()
            return None
        buf = bytearray()
        for chunk in r.iter_content(1 << 16):
            buf += chunk
            if len(buf) > MAX_BYTES:
                r.close()
                return None
        r.close()
        return bytes(buf)
    return None


def pdf_to_text(pdf: bytes) -> str | None:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(pdf)
        f.flush()
        try:
            out = subprocess.run(
                ["pdftotext", "-q", "-enc", "UTF-8", f.name, "-"],
                capture_output=True, timeout=180)
        except subprocess.TimeoutExpired:
            return None
    txt = out.stdout.decode("utf-8", "replace")
    return txt if len(txt) > 500 else None


def one(arxiv_id: str) -> tuple[str, str]:
    dest = TEXT / f"{arxiv_id}.txt.gz"
    if dest.exists():
        return arxiv_id, "cached"
    pdf = gcs_pdf(arxiv_id)
    if pdf is None:
        return arxiv_id, "no_pdf"
    txt = pdf_to_text(pdf)
    if txt is None:
        return arxiv_id, "no_text"
    with gzip.open(dest, "wt", encoding="utf-8") as fh:
        fh.write(txt)
    return arxiv_id, "ok"


def main() -> None:
    TEXT.mkdir(parents=True, exist_ok=True)
    ids = []
    for f in sorted(LIST.glob("*.json")):
        for r in json.loads(f.read_text())["sample"]:
            ids.append(r["id"])
    ids = sorted(set(ids))
    # Shuffle (fixed seed) so that if we run out of time the coverage that we
    # DO have is spread evenly over every month, rather than being complete for
    # early months and empty for late ones -- which would wreck the trend.
    import random
    random.Random(20260827).shuffle(ids)
    print(f"{len(ids)} unique sampled papers", flush=True)

    status, done = {}, 0
    with ThreadPoolExecutor(WORKERS) as ex:
        for aid, st in ex.map(one, ids):
            status[aid] = st
            done += 1
            if done % 100 == 0:
                n_ok = sum(1 for v in status.values() if v in ("ok", "cached"))
                print(f"  {done}/{len(ids)}  ok={n_ok}", flush=True)
    STATUS.write_text(json.dumps(status, indent=0))
    from collections import Counter
    print(Counter(status.values()))


if __name__ == "__main__":
    sys.exit(main())
