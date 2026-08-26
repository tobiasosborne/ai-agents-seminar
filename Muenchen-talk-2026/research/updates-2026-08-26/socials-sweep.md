# Socials/news sweep for LLM-mathematics & physics results, ~June–26 Aug 2026

Compiled 26 August 2026. Cross-checked against
`/home/tobias/Projects/ai-agents-seminar/Muenchen-talk-2026/research/llm-proof-results.md`
(the "known results" file, compiled 24 Aug 2026). Only items **not already in that file**, or
that materially **update/resolve a caveat already flagged there**, are listed below.

Same verification tiers as the source file: **T1** machine-checked/peer-reviewed,
**T2** arXiv + named human verifiers (not refereed), **T3** announced only, **T4** disputed/retracted.

---

## New items (not in the known-results file)

| Date | Result | Model/system | Verification | Source |
|---|---|---|---|---|
| **2 Jun 2026** (arXiv); journal pub. ~1 Jul 2026 | **Proof of the "a+b=1" identity for the critical exponents of jamming** — a 12-year-old conjecture in the statistical physics of granular/jamming transitions (Parisi–Zamponi 2014). Claude produced the core proof idea in early rounds; contained errors, fixed over ~40 rounds of dialogue with the human authors. | Claude Sonnet 4.6, then Opus 4.7 (Anthropic) | **T1** — published in *J. Stat. Mech.* (2026) 073301, DOI 10.1088/1742-5468/ae7bd7, arXiv:2606.03300. Peer-reviewed. Authors: **Giorgio Parisi (2021 Physics Nobel laureate)** and Francesco Zamponi. | [arXiv:2606.03300](https://arxiv.org/abs/2606.03300); [phys.org, 1 Jul 2026](https://phys.org/news/2026-06-physicists-ai-claude-collaborate-year.html); [Physics World](https://physicsworld.com/a/ai-model-helps-physics-nobel-laureate-out-of-a-decade-old-mathematical-jam/); [Live Science](https://www.livescience.com/physics-mathematics/mathematics/nobel-prize-winning-physicist-and-team-use-claude-ai-to-solve-decades-old-math-puzzle); [Zenodo — full chat transcript](https://zenodo.org/records/20633432) |
| **17 Aug 2026** | **Matrix multiplication exponent improved to ω < 2.371177** (from the prior best 2.371339) via a pipeline that reformulates the optimisation problem, uses an ML-designed algorithm, and refines it with AlphaEvolve. Continuation of the long-running record chase (Alman–Vassilevska Williams et al.); distinct from, and later than, the 4×4-complex-matrix "48 multiplications" AlphaEvolve result already in the known-results file. | AlphaEvolve (Gemini-powered, DeepMind) + human optimisation reformulation | **T2** — short arXiv note, co-authored by **Josh Alman and Virginia Vassilevska Williams**, the field's leading experts and authors of the previous record. Not yet refereed but authorship carries weight. | [arXiv:2608.16884](https://arxiv.org/abs/2608.16884); [AI Weekly](https://aiweekly.co/editors-blog/found-first-alphaevolve-pushes-matrix-multiplication-exponent-to-2-371177) |
| **18 Aug 2026** | **Palomar** — a registry of Lean-verified mathematics launched by Terence Tao with the Lean FRO and ICARM, explicitly built to referee the flood of AI-generated Lean proofs. Requires a machine-readable "challenge file" (formal statement), a solution module, and a `formalization.yaml` describing the claim in natural language with metadata; records exact source versions and Lean-checks them. Not itself a result — it's **infrastructure for the verification gap** this whole talk is about. | — (registry, not a model) | N/A — institutional response | [Tao's blog, 18 Aug 2026](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/); [palomar-registry.org](https://palomar-registry.org/); [Hacker News discussion](https://news.ycombinator.com/item?id=49355968) |

---

## Updates to items/caveats already in the known-results file

| Item | What's new | Status |
|---|---|---|
| **IMO 2026 "42/42"** (flagged in the known-results file as single-source/SCMP-only, "verify before slide") | Now **corroborated by multiple outlets**: **two AI systems received an officially IMO-graded 42/42** — Huawei's *Celia* and Xiaohongshu (RedNote)'s *dots-note 3.0*. Separately, **four more self-reported 42/42 claims** circulated (Claude Fable 5, GPT-5.6 Sol, Kimi K3, Axiom Math) from one VC's independent testing (Deedy Das, on X) — these were **self-administered and graded by a Claude-based agent, not IMO officials**, so treat as unverified/weaker evidence, explicitly distinct from the two officially-graded scores. | Resolves the file's caveat: **T1 for the two officially-graded systems; T3 for the other four.** Neither DeepMind nor OpenAI is among the officially-graded winners — worth keeping on the slide as-is. | [SCMP](https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote); [Digital Applied, "Four AIs Scored a Perfect 42/42. So What?"](https://www.digitalapplied.com/blog/imo-2026-perfect-scores-ai-benchmark-saturation); [Tech Insider](https://tech-insider.org/ai-imo-2026-perfect-score-odds-hit-96-percent/); [Deedy Das on X](https://x.com/deedydas/status/2079409461874332066) |
| **Jacobian conjecture disproof** (Claude Fable 5, Alpöge) | No correction/retraction found; coverage has broadened (Fortune, IBM Think, ScienceDaily) but no new substantive development beyond what's in the file. Confirms the file's T3→T2 tier is stable. | No change — file entry stands. | [Fortune](https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/); [IBM Think](https://www.ibm.com/think/news/ai-cracked-jacobian-conjecture-humans-called-play) |
| **erdosproblems.com AI tracker** | Notable institutional/labour-market signal: **Jacob Tsimerman** (Fields Medalist, one of the human verifiers of the OpenAI unit-distance disproof already in the file) **left academia for OpenAI**, announced the same day he received the Fields Medal (reported ~Jul 2026). Not a math result, but a striking data point for "the flurry is real" framing. | Commentary/context, not a result | [teorth/erdosproblems wiki](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems); referenced via search aggregation, primary announcement not independently re-verified here — **flag as UNVERIFIED single-mention, corroborate before quoting on a slide.** |

---

## Checked and found NOT to contain new major items

- **Quanta Magazine, Aug 2026 tag pages** — no new AI-mathematics headline beyond what's already sourced (Erdős piece, 3 Aug, already in file). The "Using AI, Mathematicians Find Hidden Glitches in Fluid Equations" piece that appeared in search results is dated **9 Jan 2026** (URL slug `-20260109`), not a new August piece — outside window, not included. No confusion with the unrelated Aug 2026 fractal/uncertainty-principle piece (human-only result, no AI).
- **Physics: hep-th / quantum gravity** — no new major LLM-produced result found beyond the already-listed gluon-amplitudes paper (arXiv:2602.12176). Field commentary (e.g. "Pre-Strings 2026" lectures on neural-network field theory) is methodological, not a new solved-problem headline.
- **Condensed matter theory** — aside from the Parisi–Zamponi jamming proof above, only benchmark/tooling papers found (e.g. "CMT-Benchmark" for LLM condensed-matter research assistants) — no new solved open problem.
- **Quantum information theory** — only a survey paper (arXiv:2607.00365, "When AI meets quantum information") and vendor/marketing material (quantum-LLM hybrids); no new proved theorem.
- **Ramanujan Machine** — ongoing project, minor 2026 output (a continued-fraction conjecture for Franel numbers); no major new result in the window, and nothing rising to "slide-worthy" next to the items already in the file.
- **erdosproblems.com direct browsing** — could not fetch the live AI-contributions wiki table for problems solved specifically in Jul–Aug 2026 beyond what Quanta's 3 Aug piece already digests (which is already the primary source cited repeatedly in the known-results file for that period). No standalone new problem number worth adding beyond what's there.
- **mathstodon.xyz / Tao's posts** — nothing beyond the ICM lecture (already in file) and the Palomar launch (added above).

---

## Hype/unverified flags (explicit)

1. **IMO 2026 "42/42 by four more AI systems"** (Claude Fable 5, GPT-5.6 Sol, Kimi K3, Axiom Math) — self-administered, Claude-graded, **not** IMO-official. Keep clearly separated from the two officially-graded scores (Huawei Celia, Xiaohongshu dots-note 3.0) if used on a slide.
2. **Jacob Tsimerman leaving academia for OpenAI** — reported via secondary aggregation (36kr-style summary chain), not independently confirmed against a primary announcement in this sweep. Treat as **UNVERIFIED** until a primary source (OpenAI announcement, Tsimerman's own statement) is checked.
3. No new "AI solves a Millennium Problem" or similarly outsized claim was found anywhere in the sweep — the absence itself is worth noting: the biggest confirmed items this period remain incremental-but-real (a 12-year-old jamming identity, a matrix-multiplication exponent shaved by ~0.0002, a Lean verification registry), not a headline "grand unsolved problem falls."

---

## Slide-ready distillation — top new items for the deck

| # | Item | Tier |
|---|---|---|
| 1 | **Jun 2026** — Parisi (Nobel laureate) + Zamponi + Claude prove 12-year-old jamming identity; peer-reviewed, *J. Stat. Mech.* | **T1** |
| 2 | **17 Aug 2026** — AlphaEvolve + Alman/Vassilevska Williams push matrix-mult exponent to ω < 2.371177 | **T2** |
| 3 | **18 Aug 2026** — Tao launches Palomar, a Lean-proof registry, explicitly to referee the AI-proof flood | infrastructure |
| 4 | **Jul 2026, resolved** — IMO 2026: only 2 systems (Huawei Celia, Xiaohongshu dots-note 3.0) have *official* 42/42; 4 more are self-graded claims | **T1 (2 systems) / T3 (4 systems)** |
