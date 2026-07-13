# Model capability vs time — Würzburg Kolloquium

An updated, grounded version of the plot Adam Brown shows in *"Training Sand to
Think"* ([Mw60FH5iflI](https://www.youtube.com/watch?v=Mw60FH5iflI)), extended to
include **every model released in the last five weeks** and **open-weights models**,
with the open-weights lag measured rather than guessed.

**All numbers are real.** Nothing is hand-typed from a press release. Snapshot: **2026-07-12**.

## The three claims, and the evidence for each

| Claim | Figure | Number |
|---|---|---|
| Capability keeps rising, and the old benchmark can no longer see it | fig1, fig2 | GPQA Diamond is at **94.6%** (expert humans: 69.7%) |
| Capability is still ~linear on a scale that cannot saturate | fig3 | frontier gains **+13.0 ECI points/year**, no ceiling in sight |
| Models arrive *more often*, not just better | fig4 | **9 → 18** models/quarter (2023→2026); the record for best-ever model now falls every **49 days** (was 72) |
| Open weights trail the frontier by ~6 months | fig5 | median **5.7 months** since 2025; GLM-5.2 today is **6.9 months** behind |

## Figures

| File | What it shows |
|---|---|
| `fig1_gpqa_dead.pdf` | **Adam Brown's actual plot**, run to today. GPQA Diamond vs release date, with his two reference lines (random guessing 25%, PhD experts 69.7%). The frontier blew through the expert line in early 2025 and is now pinned near the ceiling. His words: *"GPQA is dead."* |
| `fig2_benchmark_ladder.pdf` | The ladder. MMLU → MATH-5 → GPQA → FrontierMath → HLE → CritPt, each one's frontier envelope. Brown's device — each curve is the previous one shifted right — extended past his talk. Only **HLE (52%)** and **CritPt (32%)** are still alive. |
| `fig3_eci_frontier.pdf` | **The headline slide.** Epoch Capabilities Index vs release date, all 179 models since 2023, open vs closed, with this week's releases named: GPT-5.6 Sol/Terra/Luna, Claude Fable 5, Claude Sonnet 5, Grok 4.5, GLM-5.2, Kimi K2.7. |
| `fig4_cadence.pdf` | The *frequency* half of the argument: releases per quarter, and new best-ever models per half-year (1 → 6). |
| `fig5_open_weight_lag.pdf` | The open-weights lag, measured horizontally, in months. |

## Why the Epoch Capabilities Index (ECI) is the y-axis

The honest problem with a "models vs time" plot in 2026 is that **every benchmark
worth plotting has saturated** — that is the content of fig1 and fig2. Plot GPQA and
the last two years look like a plateau, which is an artefact of the ruler, not the models.

ECI is Epoch's IRT-style latent-ability scale fitted across many benchmarks. Like Elo,
it has **no ceiling**: as constituent benchmarks cap out, they stop carrying information
and others take over. It is the only axis on which the 2023→2026 trend can be drawn
without the ruler breaking halfway. It also covers open and closed models under one
methodology, which is what makes the lag estimate meaningful.

For a physics audience, **CritPt** is the benchmark to name out loud: research-level
physics problems, currently topping out at **32.3%** (GPT-5.6 Sol). It is the honest
successor to Brown's "PhD-level questions", and it is nowhere near solved.

## Data

Everything comes from **Epoch AI's Benchmarking Hub** bulk export (`data/epoch/`),
which Epoch run themselves under one methodology across open- and closed-weights models.

```
python fetch_data.py    # re-download the ZIP (it is regenerated continuously)
python analyse.py       # rebuild every figure + results/
```

> Epoch AI, 'AI Benchmarking Hub'. https://epoch.ai/benchmarks — CC-BY.

`results/key_numbers.md`, `results/open_weight_lag.csv`, `results/benchmark_ladder.csv`
and `results/models_eci.csv` hold the derived numbers, so a slide can quote them
without re-running anything.

`sources/harvest_raw.json` is a separate 9-agent web harvest (636 records, **632
independently re-verified** against re-fetched sources) covering Artificial Analysis,
METR, ARC Prize and the vendor announcements. It is *corroboration and provenance*, not
the plotted data — the figures use Epoch only, on purpose.

## Caveats you should know before you present this

1. **Muse Spark 1.1 (Meta, 9 Jul) has no independent score yet.** It is drawn on fig3 as
   a dated marker with **no y-value** rather than a guessed one. This is not a gap in the
   argument — it *is* the argument: models now arrive faster than evaluators can score them.
2. **Meta's frontier model is closed weights.** Both Epoch and Artificial Analysis list
   Muse as "API access". Meta has left the open-weights frontier; the open-weights torch
   has passed to Chinese labs (Z.ai/GLM, Moonshot/Kimi, DeepSeek). Worth saying explicitly.
3. **Benchmark numbers diverge wildly between aggregators.** Epoch scores Claude Fable 5's
   HLE around 46%; a third-party aggregator claimed 64.5%. Artificial Analysis changed
   their Intelligence Index (v4.0 → v4.1) in June 2026, which *lowered* everyone's score —
   never put pre- and post-v4.1 numbers on the same axis. **Do not mix evaluators on one
   plot.** This is why everything here is Epoch-only.
4. **"Models per quarter" is partly a measure of what Epoch chose to score.** It is a
   proxy for release cadence, not a census of every model ever shipped. The frontier-record
   count (fig4, lower) is the more robust of the two.
5. The lag in fig5 is *capability* lag, not a claim about training compute or cost.
6. ECI values are Elo-like: **differences** are meaningful, the absolute number is not.
