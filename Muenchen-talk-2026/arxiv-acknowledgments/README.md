# LLM acknowledgments in arXiv quant-ph and math-ph, 2023–2026

Measured for the MCQST München colloquium, 27 August 2026. Everything here is
our own measurement on our own sample; §5 puts it next to the published
literature, which measures a *different and much larger* quantity.

**Figure for the slide: `figures/ack_trend.png` (and `.pdf`).**

---

## 1. Headline numbers

<!--HEADLINE-->

Sample: **3,405 arXiv papers** (3,410 drawn, 100% full text retrieved) across 15 quarterly months, Jan 2023 – Jul 2026. Every one of the **93** papers the screen flagged was read by hand.

**quant-ph** — papers acknowledging LLM assistance, pooled by year:

| year | count | rate | 95% CI |
|---|---|---|---|
| 2023 | 0/480 | **0.0%** | [0.0, 0.8] |
| 2024 | 1/477 | **0.2%** | [0.0, 1.2] |
| 2025 | 3/479 | **0.6%** | [0.2, 1.8] |
| 2026 | 29/359 | **8.1%** | [5.7, 11.4] |

**math-ph** — papers acknowledging LLM assistance, pooled by year:

| year | count | rate | 95% CI |
|---|---|---|---|
| 2023 | 0/408 | **0.0%** | [0.0, 0.9] |
| 2024 | 0/433 | **0.0%** | [0.0, 0.9] |
| 2025 | 2/417 | **0.5%** | [0.1, 1.7] |
| 2026 | 24/352 | **6.8%** | [4.6, 9.9] |

Latest measured month (2026-07), **math-ph**: 13/120 = **10.8%** [6.4, 17.7].
Latest measured month (2026-07), **quant-ph**: 17/119 = **14.3%** [9.1, 21.7].

Full per-month table: `results/rates_by_month.csv`.

### What the LLM was acknowledged *for*

Read off the disclosure sentence by hand (`results/ack_purpose.json`); a paper claiming several is filed under the highest.

| used for | 2024 | 2025 | 2026 | total |
|---|---|---|---|---|
| language / copy-editing / LaTeX | 0 | 5 | 28 | 33 |
| code, scripts, figures | 1 | 0 | 9 | 10 |
| **research content** — proofs, derivations, literature, brainstorming | 0 | 0 | 16 | 16 |

All 16 of the 'research content' acknowledgments are from 2026 — the shift is not just more disclosure, it is disclosure of a different kind of use.

---

## 2. What is being counted

Three things get confused in this area, and the whole exercise is worthless if
they are not kept apart:

| | |
|---|---|
| **(a) acknowledges LLM assistance** | the authors say *they* used an LLM — to polish the writing, to write a script, to suggest a lemma. **This is what the plot shows.** |
| **(b) the paper is about LLMs** | "Quantum Large Language Model Fine-Tuning". Screened from title+abstract (`n_about_llm` in `results/rates_by_month.csv`), confirmed by hand, and **excluded from the numerator**. |
| **(c) the paper denies using an LLM** | "no generative AI was used in preparing this manuscript". Flagged (`negation_nearby`) and **not** counted as (a). |

(a) is a *disclosure* rate, not a *usage* rate. It is a lower bound on usage by
an unknown and certainly large factor — see §5.

## 3. Method

**Sampling.** Quarterly months, Jan 2023 → Jul 2026 (15 months × 2 categories =
30 cells). For each cell we page the official arXiv API over the whole month
(`cat:<c> AND submittedDate:[...]`), keep only submissions whose *primary*
category is the target (so "quant-ph" means submitted to quant-ph, not merely
cross-listed near it; `math-ph` and `math.MP` are the same archive and both
count), and draw a random sample of up to 120 with a fixed seed. Sanity check:
0 of the sampled papers has a `published` date outside its target month.

**Full text.** The arXiv API is metadata-only, so acknowledgments require full
text. We take it from the **official arXiv bulk dataset on Google Cloud
Storage** (`gs://arxiv-dataset`, public and free, maintained by arXiv with
Google). We deliberately do **not** scrape `arxiv.org/e-print`, which
`arxiv.org/robots.txt` disallows; the GCS bucket is the sanctioned bulk route
and it also lets us parallelise without hammering anyone. PDFs go through
poppler's `pdftotext`; the PDF is discarded and only the gzipped text is cached.

We always take **v1, the version as submitted**. That keeps the x-axis honest:
each point is "what the authors wrote when they submitted in month *M*", not
"what survived refereeing", which would bias early months (years of accumulated
revisions) against late ones.

**Detection — screen, then read every hit by hand.** The regex screen
(`detect.py`) is deliberately over-inclusive. It normalises pdftotext artefacts
(letter-spaced `A c k n o w l e d g m e n t s`), locates acknowledgment /
funding / AI-disclosure regions including REVTeX `V. ACKNOWLEDGMENTS` headings
and run-in `Acknowledgements.–The authors thank…` forms, and then scans the
**whole text** for ~30 LLM patterns, accepting a match if it sits in an
acknowledgment region *or* within ~400 characters of an acknowledgment cue.
Reference lists are excluded (a bibliography is where "Language models are
few-shot learners" lives). Physics homonyms are vetoed explicitly: **GPT** =
generalised probabilistic theory, **anthropic** = the anthropic principle,
**Claude** = a French first name, **Gemini/Llama/Mistral** likewise.

Then the part that actually buys precision: **every paper the screen flags is
read by a human**, together with any paper containing an unambiguous LLM string
anywhere in its text. That union is ~2% of the corpus — small enough to
adjudicate exhaustively. The verdicts are in `results/manual_overrides.json`;
the snippets they were made from are in `results/hits.jsonl`, so every count in
the plot is auditable back to a sentence.

The manual pass matters. About a third of flagged papers are rejected on
reading — citations, the `anthropic` principle, `GPT` as generalised
probabilistic theory, `L_lm` as a matrix element, `[LLM+ 23]` as a citation key,
body prose about LLMs. It also *adds* papers the context rule missed: two
disclosures living in figure captions, "Figure 1 (generated by ChatGPT 4o)" and
"Image generated using AI (ChatGPT, 2025)".

The `about_llm` title/abstract heuristic is only a screen: where a human has
read the paper, the human wins. That matters in both directions — a paper on
LLM-generated compilers is not acknowledging assistance, while a paper whose
abstract says "GPT-5.6 assisted with literature search" trips the heuristic
while being exactly the thing we are counting.

**Statistics.** Per cell, the fraction of *successfully retrieved* sampled
papers adjudicated as (a). Intervals are 95% **Wilson** score intervals — not
Wald, which goes negative at the *n* ≈ 120, *p* ≈ 0 that most of this plot lives
at.

## 4. Caveats — read these before quoting the number

1. **This is a disclosure rate, not a usage rate.** Every published estimate of
   actual LLM involvement is far higher — a factor of a few against the
   physics-adjacent stylometric numbers, three orders of magnitude against
   Gray's cross-field disclosure count (§5). The plot measures a norm changing
   at least as much as a behaviour changing.
2. **Small cells.** Up to 120 papers per category-month. A 5% rate on *n* = 120
   has a 95% interval of roughly [2%, 11%]. The bands on the figure are the
   honest width; do not read a single quarter's wiggle as a trend.
3. **The 2026 rise rests on tens of papers, not thousands.** It is large enough
   to clear its own error bars, but it is one sample.
4. **Retrieval.** 3,405 of the 3,410 sampled papers yielded usable full text.
   The 5 that did not (no PDF in the bucket, over the 40 MB cap, or no
   extractable text) are dropped from numerator and denominator alike; at that
   size they cannot move anything. Per-cell counts are in
   `results/rates_by_month.csv` (`n_sampled` vs `n_with_text`).
5. **v1 only.** Papers that added an AI-disclosure statement at referee request
   are counted as non-disclosing. This makes recent numbers *conservative*.
6. **Quarterly sampling.** Jan/Apr/Jul/Oct only; the intervening months are not
   measured and month-to-month seasonality is invisible.
7. **Detection is not perfect.** Precision is protected by reading every hit;
   recall is not fully known. The recall audit (papers with an LLM string
   anywhere but not flagged as an acknowledgment) is reported in
   `results/rates_by_month.csv` as `k_llm_term_anywhere`, and every one of those
   was also read by hand — but a disclosure phrased without any of our ~30
   patterns would still be missed.
8. **`math-ph` is small.** Some months have fewer than 120 primary math-ph
   submissions in total, so those cells sample the whole month.

## 5. How this compares with the literature

Our numbers are *acknowledgment* rates. The well-known large numbers in this
area are *stylometric estimates of LLM-modified text*, which is a different
quantity measured a different way. The gap between them is the interesting part.

**Acknowledgment / disclosure rates (comparable to ours):**

- Gray, *Estimating the prevalence of LLM-assisted text in scholarly writing*,
  [arXiv:2512.01560](https://arxiv.org/abs/2512.01560) — 1,551 Web-of-Science
  2024 articles carry a visible LLM disclosure out of ~2.6 M, i.e. **≈0.06%**,
  against his own stylometric estimate of >10% actual involvement. Disclosing
  papers grew ~4× in the year to Aug 2025.
- *How is ChatGPT acknowledged in academic publications?*, *Scientometrics*
  (2024), [doi:10.1007/s11192-024-05193-y](https://doi.org/10.1007/s11192-024-05193-y)
  — of papers that *do* acknowledge ChatGPT, **80%** cite text editing /
  proofreading, 5.3% coding, 3.5% drafting, 1.6% figures. A composition study,
  not a rate study — but it says what the acknowledgments we count are *for*,
  and our 2026 quant-ph hits are notably *not* all copy-editing.
- Springer Nature author survey (2025): **about half** of all LLM use went
  undisclosed; over three quarters among early-career authors.

**Stylometric estimates of LLM-modified text (a much larger, different number):**

- Liang et al., *Mapping the Increasing Use of LLMs in Scientific Papers*,
  [arXiv:2404.01268](https://arxiv.org/abs/2404.01268), Nature Human Behaviour
  (2025) — 950,965 arXiv/bioRxiv/Nature papers. By Feb 2024: **CS ~17.5%,
  Mathematics ~6.3%** of sentences LLM-modified.
- Kobak et al., *Delving into LLM-assisted writing…*, Science Advances (2025),
  [doi:10.1126/sciadv.adt3813](https://doi.org/10.1126/sciadv.adt3813) —
  ≥13.5% of 2024 PubMed abstracts, by excess vocabulary; explicitly a lower
  bound. Holzwarth, González-Márquez & Kobak,
  [arXiv:2608.10715](https://arxiv.org/abs/2608.10715) (Aug 2026) push this to
  **89% of December 2025 biomedical papers** with an unbiased estimator.
- Siler, *The diffusion of large language models in published academic
  articles*, PNAS 123(22) (2026),
  [doi:10.1073/pnas.2605754123](https://doi.org/10.1073/pnas.2605754123) —
  7.3 M articles; **>50% show LLM influence by 2025**.
- Elazar & Antoniak, [arXiv:2601.17036](https://arxiv.org/abs/2601.17036)
  (Jan 2026) — arXiv-native. CS non-review papers **6.2% (2023) → 18.9%
  (2025)** AI-generated; reports substantial increases in physics and
  mathematics too.
- unslop.run, *Over 30% of papers submitted on arXiv read as AI-written*
  ([blog](https://unslop.run/blog/measuring-ai-writing-on-arxiv), through Jul
  2026; in-house classifier, not peer-reviewed) — by field, latest period:
  CS **65%**, applied physics **34%**, cond-mat **24%**, hep **14%**,
  astro-ph **11%**, mathematics **0.7%**. quant-ph is not broken out.

**The reading for the talk.** Three things, and the third is the interesting one.

1. **Usage ≫ disclosure, everywhere.** Gray's 0.06% disclosure rate against his
   own >10% stylometric estimate is the same gap we are looking at from the
   other end. Our numbers are the floor, not the quantity.
2. **Physics and maths are the late adopters.** Every stylometric study puts
   them last — mathematics at 0.7% where CS is at 65%. Our own series says the
   same thing about disclosure: flat at zero through 2023 and 2024, while CS was
   already at 6–13%.
3. **But the composition of what is disclosed has changed, and recently.** Every
   acknowledgment before 2026 in our sample is copy-editing, LaTeX, or a
   plotting script. From 2026 a third category appears and immediately accounts
   for a fifth of all disclosures: the LLM is credited with *mathematics*.
   In our sample, verbatim:
   - "ChatGPT 5.5 Pro was used as a research assistant to help explore the
     analysis of the product test" (quant-ph, Jul 2026)
   - "GPT-5.6 Pro suggested Lemma 4.6" (quant-ph, Jul 2026)
   - "ChatGPT 5.6 produced a candidate proof of the conjecture" (quant-ph,
     Jul 2026)
   - "GPT-5.6 assisted with literature search, the development of technical
     arguments, and manuscript preparation" (math-ph, Jul 2026)
   - "This paper, with the exception of the abstract and introduction, was
     written entirely by Claude Opus 4.8 and Fable 5" (math-ph, Jul 2026)
   - "This manuscript was generated in its entirety using the ChatGPT-5.2 Pro
     large language model" (math-ph, Jan 2026)

   That is a different claim from "I used it to fix my English", and it is what
   makes the 2026 numbers worth a slide.

Context worth a sentence: arXiv restricted unpublished CS review papers in
Oct 2025, and in May 2026 introduced a one-year submission ban for papers with
unchecked AI generation.

## 6. Reproducing

```bash
python3 fetch_listings.py   # arXiv API -> data/listings/*.json   (~10 min, rate-limited)
python3 fetch_texts.py      # GCS bulk PDFs -> data/text/*.txt.gz (~45 min, resumable)
python3 detect.py           # regex screen -> results/papers.csv, results/hits.jsonl
#   ... read results/hits.jsonl, record verdicts in results/manual_overrides.json ...
python3 analyse.py          # -> results/rates_by_month.csv, figures/ack_trend.{png,pdf}
```

Needs `requests`, `pandas`, `matplotlib`, and `pdftotext` (poppler-utils).
`fetch_texts.py` is resumable and shuffles its work list with a fixed seed, so a
partial run still covers every month evenly.

### Files

| Path | What it is |
|---|---|
| `data/listings/*.json` | the sampled paper IDs per category-month, with title/abstract |
| `data/text/*.txt.gz` | cached extracted full text, one file per paper |
| `results/papers.csv` | one row per sampled paper: verdict, patterns, flags |
| `results/hits.jsonl` | every flagged paper **with the snippet it was judged on** |
| `results/manual_overrides.json` | the hand adjudication — the authoritative labels |
| `results/rates_by_month.csv` | per-cell counts, rates and Wilson intervals (table view) |
| `results/headline.txt` | the numbers quoted above |
| `figures/ack_trend.png/.pdf` | the slide figure |
