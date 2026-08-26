"""Download the ground-truth data. Run this to refresh; everything else reads data/.

Primary source: Epoch AI's Benchmarking Hub bulk export. Epoch run these evals
themselves under one methodology across open- and closed-weights models, which
is the only way to make a cross-vendor plot that is not apples-to-oranges.

    Epoch AI, 'AI Benchmarking Hub'. https://epoch.ai/benchmarks
    CC-BY. See data/epoch/README.md for the full citation.

Note the ZIP is regenerated continuously (it was stamped "Updated Jul. 12, 2026"
when we pulled it), so re-running this will move the numbers. The figures record
the snapshot date.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import requests

DATA = Path(__file__).parent / "data"
EPOCH_ZIP = "https://epoch.ai/data/benchmark_data.zip"


def main() -> None:
    DATA.mkdir(exist_ok=True)
    print(f"GET {EPOCH_ZIP}")
    r = requests.get(EPOCH_ZIP, timeout=120)
    r.raise_for_status()
    (DATA / "benchmark_data.zip").write_bytes(r.content)

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        z.extractall(DATA / "epoch")
    n = len(list((DATA / "epoch").glob("*.csv")))
    print(f"unpacked {n} benchmark CSVs -> {DATA / 'epoch'}")


if __name__ == "__main__":
    main()
