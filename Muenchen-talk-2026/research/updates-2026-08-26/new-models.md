# New model releases missing from `model-progress/` (as of 2026-08-26)

Data-gathering only. Nothing in `Wuerzburg-talk-2026/model-progress/` was touched.
The existing pipeline's snapshot is dated **2026-07-12**; its last-included release is
**GPT-5.6 Sol/Terra/Luna (2026-07-09)**. Everything below is newer than that.

## Method

`fetch_data.py` pulls `https://epoch.ai/data/benchmark_data.zip` — I re-ran exactly
that GET (fresh pull, `2026-08-26`) and diffed it against
`model-progress/results/models_eci.csv` and `data/epoch/epoch_capabilities_index.csv`.
This is the same source and same schema the pipeline already uses, so these rows can
be appended to `epoch_capabilities_index.csv` (or `results/models_eci.csv` directly)
with no transformation. Where Epoch had not yet computed an ECI score, I searched the
web for vendor-reported or independently-reported benchmark numbers instead, and I
say explicitly, per row, which case it is.

**Important scoping note on "Epoch is current":** Epoch's own bulk export, pulled
fresh today, has **no record at all — scored or not — of anything released after
2026-08-14.** So for the back half of August I'm relying on press/vendor sources only;
there is no independent-evaluator data available yet for that window, for any model.

## Table A — usable ECI score, ready to append (Epoch-measured, matches existing schema exactly)

Columns match `results/models_eci.csv`: `Model name, date, ECI Score, Organization, Model accessibility, open`.

| Model name | date | ECI Score | Organization | Model accessibility | open | Source |
|---|---|---|---|---|---|---|
| Inkling-Small | 2026-07-15 | 150.17 | Thinking Machines | Open weights (unrestricted) | True | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Inkling | 2026-07-15 | 148.77 | Thinking Machines | Open weights (unrestricted) | True | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| **Kimi K3** | 2026-07-16 | 157.49 | Moonshot | Open weights (non-commercial) | True | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Gemini 3.6 Flash | 2026-07-21 | 154.20 | Google DeepMind | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Gemini 3.5 Flash-Lite | 2026-07-21 | 145.11 | Google DeepMind | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Claude Opus 5 | 2026-07-24 | 161.54 | Anthropic | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| DeepSeek V4 Flash 0731 | 2026-07-31 | 154.43 | DeepSeek | Open weights (unrestricted) | True | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Qwen 3.8 Max | 2026-08-02 | 156.43 | Alibaba | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Grok 4.6 | 2026-08-12 | 155.94 | xAI | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |
| Gemini 3.7 Flash | 2026-08-13 | 156.85 | Google DeepMind | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |

Notes on this table:
- **Claude Opus 5 (161.54) is the new closed-weights frontier leader**, edging out
  GPT-5.6 Sol (161.08, already in the dataset). This shifts the closed-frontier
  envelope in fig3/fig5 — worth re-running the linear fit.
- **Kimi K3 (157.49, open weights)** is the standout open-weights point: it sits
  above every other open model currently in `results/models_eci.csv` (the previous
  open-weights record-holder was GLM-5.2 at 151.57), so it should reset the
  open-weights frontier envelope and the open-weight-lag calculation in fig5.
- All ECI Scores above are Epoch's own composite (IRT-style, no ceiling) — directly
  comparable to the existing column, no unit conversion needed.

## Table B — important update to an existing row, not a new model

| Model name | date | ECI Score | Organization | Model accessibility | open | Source |
|---|---|---|---|---|---|---|
| Muse Spark 1.1 | 2026-07-09 | 154.37 | Meta AI | API access | False | [Epoch AI Benchmarking Hub bulk export](https://epoch.ai/data/benchmark_data.zip), pulled 2026-08-26 |

`analyse.py` currently hardcodes Muse Spark 1.1 as an **unscored** rug-mark exception
(`unscored = [("Muse Spark 1.1", "Meta", pd.Timestamp("2026-07-09"))]`, fig3). Epoch
has since scored it at **154.37**. That special-case should be removed and Muse Spark
1.1 plotted normally as a closed-weights point — the "arrived faster than evaluators
could score it" story now applies to *other* models instead (see Table C).

## Table C — released, no Epoch ECI score yet; vendor/press numbers only

### Qwen 3.8 27B — must-have, per your instructions

Epoch's own export (pulled today) **has a row for it but the `ECI Score` field is
empty** — release date 2026-08-14, Alibaba, `Open weights (unrestricted)`. Epoch has
run a few non-ECI benchmarks on it already (ProofBench 0.16, WebDev Arena ~1595–1608,
Surface Evolver Bench 0.45/0.19 pass rate) but none of the six benchmarks the pipeline
uses for ECI (MMLU/MATH-5/GPQA/FrontierMath/HLE/CritPt), so there is no
Epoch-measured, cross-model-comparable number for it yet.

What I found instead is **Alibaba's own self-reported model-card numbers** (August 14
launch), reproduced by third parties but **not independently verified by Epoch or
anyone else** as of this pull:

| Model name | date | Organization | Model accessibility | open | Benchmark | Score (self-reported) | Source |
|---|---|---|---|---|---|---|---|
| Qwen 3.8 27B | 2026-08-14 | Alibaba | Open weights (unrestricted) | True | GPQA Diamond | 89.2% | [Qwen3.8-27B: Specs, Benchmarks & Verdict — kingy.ai](https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/) |
| Qwen 3.8 27B | 2026-08-14 | Alibaba | Open weights (unrestricted) | True | Humanity's Last Exam | 30.8% | [Qwen3.8-27B: Specs, Benchmarks & Verdict — kingy.ai](https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/) |
| Qwen 3.8 27B | 2026-08-14 | Alibaba | Open weights (unrestricted) | True | LiveCodeBench v6 | 90.3% | [Qwen3.8-27B: Specs, Benchmarks & Verdict — kingy.ai](https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/) |
| Qwen 3.8 27B | 2026-08-14 | Alibaba | Open weights (unrestricted) | True | SWE-bench Pro | 61.7% | [Qwen3.8-27B: Specs, Benchmarks & Verdict — kingy.ai](https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/) |

Corroborated by a second, independent write-up: [Qwen3.8-27B Benchmarks — orcarouter.ai](https://www.orcarouter.ai/blog/qwen-3-8-27b-benchmarks). GPQA Diamond and HLE are the
two columns that overlap with the pipeline's own `BENCHMARKS` dict, so if the other
agent wants a stand-in ECI-adjacent point for fig1/fig2 specifically, GPQA (89.2%) and
HLE (30.8%) are the least-bad options — but both are vendor self-reported, "in-house,
corrected or modified" per one write-up's characterization, and **not from the Epoch
pipeline**. **I did not estimate or back out an ECI value from them — do not treat
89.2%/30.8% as ECI-equivalent without saying so on the slide.**

### Other released-but-unscored models (Epoch has a row, no ECI value)

| Model name | date | Organization | Model accessibility | open | What I found |
|---|---|---|---|---|---|
| GLM-5.3 | 2026-08-14 | Z.ai (Zhipu AI) | API access | False | Epoch has rows in FrontierSWE, DeepSWE, ALE-bench, vending-bench-2 but none of the pipeline's six ECI-input benchmarks, and no ECI score. I could not find a vendor GPQA/HLE/MMLU number in the sources I checked — **no comparable score found**. |
| Qwen3.7 Flash | 2026-07-27 | Alibaba | API access (per Epoch row) | False | Epoch row exists, ECI blank. No benchmark scores found anywhere in the fresh Epoch pull or in web search. **No score found.** |
| Muse Spark 1.2 | 2026-08-05 | Meta AI | API access | False | Epoch row exists (appears in `gdp_pdf_external.csv`), ECI blank. **No score found.** |
| DeepSeek V4 Pro 0813 | 2026-08-13 | DeepSeek | Open weights (unrestricted) | True | Epoch has ARC-AGI / ARC-AGI-2 rows but no ECI score and none of the six pipeline benchmarks. **No score found.** |

## No score found at all (not even in Epoch's raw benchmark CSVs)

- **GLM-5.3**, **Qwen3.7 Flash**, **Muse Spark 1.2**, **DeepSeek V4 Pro 0813** — see Table C above; listed here again for the "no usable number" bucket the task asked for.

## Checked and deliberately excluded

- **"Llama 5" (Meta, ~600B, open weights, claimed 2026-04-08).** Multiple SEO/content-farm
  sites (ragyfied.com, chroniclejournal.com market-wire syndication, startuphub.ai) describe
  this as released; a more careful source (orcarouter.ai's "Llama 5 Leak" piece) and my own
  broader search conclude **Meta has not confirmed any such model — no official
  announcement, no weights, no independently-run benchmark**. This is consistent with
  `model-progress`'s own README caveat that Meta's frontier model (Muse Spark) is closed and
  Meta has left the open-weights frontier to Chinese labs. I'm treating "Llama 5" as
  unconfirmed rumor/speculation and have **not** added it anywhere above. Flagging it in case
  you've seen it cited elsewhere — I would not put it on a slide without Meta's own
  announcement or an Epoch/Artificial-Analysis score.
- **ByteDance Seed 2.1 Turbo, Seedance 2.5, Grok Imagine Image 2.0** (all released
  Aug 8–10, 2026) — image/video generation models, not text-capability models Epoch
  scores for ECI. Out of scope for this frontier/lag plot.
- **GLM-5.2 Turbo** (Z.ai, 2026-08-17) and a teased-but-not-yet-released Mistral
  open-weight frontier model (entered "early access" July 2026, broader release
  "later this summer," per [Tech Times](https://www.techtimes.com/articles/319798/20260706/mistral-ai-targets-frontier-gap-open-weight-model-entering-july-early-access.htm)) —
  found in passing; neither has an Epoch record or a vendor benchmark table I could
  verify, and the Mistral model isn't confirmed shipped yet. Not included.

## Sources consulted

- Epoch AI, Benchmarking Hub bulk export, https://epoch.ai/data/benchmark_data.zip (fresh pull, 2026-08-26) — primary source for Table A/B and the "Epoch has a row but no score" entries in Table C.
- https://epoch.ai/eci and https://epoch.ai/data/ai-models — JS-rendered leaderboard pages; confirmed to exist but the underlying data isn't in static HTML, so the ZIP export above was used instead (same source the pipeline itself uses).
- https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/ — Qwen 3.8 27B vendor benchmark table.
- https://www.orcarouter.ai/blog/qwen-3-8-27b-benchmarks — corroborating Qwen 3.8 27B numbers.
- https://simonwillison.net/2026/Aug/16/qwen-38-27b/ — release commentary, confirms Aug 14 release date and Apache 2.0 license, no independent numbers yet.
- https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation and https://fortune.com/2026/07/16/moonshots-kimi-k3-pushes-chinese-ai-into-fable-level-territory/ — Kimi K3 release context (2.8T params, July 16/27 2026, custom license).
- https://www.orcarouter.ai/blog/llama-5-leak and general search — used to rule out "Llama 5" as confirmed.
