# Tracker mining, Source Set B — 26 Aug 2026

Sources: proofatlas.ai/collaboration/ (+/advances/), openproblem.ai/mathematical-discovery-ledger/,
mathdb.com, theoremdb.org, vibemathed.com. Fetched via WebFetch on 26 Aug 2026. Cross-check against
the known-33 list in `research/llm-proof-results.md` before using on a slide — several names below
(Levent Alpöge, Claude Fable 5) already recur there for the Jacobian conjecture, which suggests these
sites may be tracking the same small set of active groups rather than independent phenomena.

---

## New results (table)

Only items not already on the known-33 list. All are recent (Aug 2026) and **none has more than
preliminary human review** — that is itself the finding (see Registry stats / Notable quotes below).

| Date | Result | Model(s) | Verification | Source URL |
|---|---|---|---|---|
| 19 Aug 2026 | **Disproof claim: Yau–Tian–Donaldson conjecture (CSCK case)** — "a polarized manifold carries a canonical Kähler metric in its polarization class exactly when it is K-polystable" claimed false, via explicit counterexample. Major result in Kähler geometry *if it holds up*. | Claude Code (Fable 5) + GPT-5.6-sol (OpenAI Codex) + Danus (FrenzyMath/AI4M@PKU) — three systems, no single vendor | **T3 (UNVERIFIED)** — site's own note: *"The mathematics was NOT checked here and is beyond quick verification."* Six other AI systems failed to reproduce the proof in 12 hours. | [arXiv:2608.19301](https://arxiv.org/abs/2608.19301); [vibemathed.com entry](https://vibemathed.com/problem/yau-tian-donaldson-conjecture-csck); [github.com/frenzymath/Danus](https://github.com/frenzymath/Danus) |
| 19 Aug 2026 | **Disproof: Carathéodory conjecture, C^∞ (smooth) case** — a closed convex C^∞ surface in ℝ³ with fewer than two umbilic points. Distinct from Hamburger's 1940s theorem for *real-analytic* surfaces, which stands untouched — so this is a genuinely new (smooth-only) counterexample to a ~100-year-old conjecture, not a full resolution of "the" Carathéodory conjecture. | Claude (Anthropic) + Codex (OpenAI) | **T2/T3 ("candidate, review pending")** — Lean code written but *unmerged/uncompiled* (formal proof read, not machine-checked yet); construction independently checked by named humans John-Paul Smith; announcement/curation by Levent Alpöge and Rasmus Lindahl | [X: @__alpoge__](https://x.com/__alpoge__/status/2089971359921156203); [Lean draft, GitHub pinned commit](https://github.com/google-deepmind/formal-conjectures/blob/7aa855bb344450777d9b19fe1cf11f2f5f9fae09/FormalConjectures/Other/CaratheodoryLoewnerCounterexample.lean); [vibemathed.com entry](https://vibemathed.com/problem/mathbb-c-infty-caratheodory-conjecture) |
| 23 Aug 2026 | **New elliptic-curve rank record: rank ≥ 31** over ℚ (previous records: ≥28 in 2006, ≥29 in 2024, ≥30 on 20 Aug 2026) — 31 explicit rational points found and verified on-curve. Progression from 30→31 took only 3 days, illustrating the "flood" pace. | Claude (Anthropic), with Levent Alpöge and Ava Howell | **T2/UNVERIFIED-partial** — the 31 points were checked to satisfy the curve equation and be pairwise distinct, but their *independence* (i.e. true rank 31, not less) was **not independently reconfirmed**; rank exactly 31 is conditional on GRH + BSD | [Elliptic Curve Rank Leaderboard, curve #302](https://elliptic-rank.icarm.cloud/curve/302); [Dujella's rank record history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html); [vibemathed.com entry](https://vibemathed.com/problem/elliptic-curve-rank-record-thirty-one) |
| 25 Aug 2026 | Model-theory result: three notions of definable Keisler measure (frequency-interpretation, generically-stable-random-extension, self-averaging) proved equivalent, with the reverse implications obtained specifically "through the use of AI models" per the authors | ChatGPT 5.5 (initial proof), Kimi K3 + Claude Fable 5 (independent cross-checks), ChatGPT 5.6 Sol (refinement) — three vendors (OpenAI, Moonshot AI, Anthropic) | **T3 (structural check only, no math verification)** — arXiv preprint by named logicians (Gabriel Conant, Kyle Gannon, James E. Hanson) who "heavily reorganized and rewrote" the AI output | [arXiv:2608.24605](https://arxiv.org/abs/2608.24605) (math.LO); [vibemathed.com entry](https://vibemathed.com/problem/equivalence-of-generic-stability-notions-for-keisler-measures) |
| 22 Aug 2026 | Erdős problem #270, affine case: transcendence result — announced, not yet reviewed | GPT-5.6 Sol | **T3** (announced) | [vibemathed.com entry](https://vibemathed.com/problem/transcendence-in-the-affine-case-of-erdos-problem-270) |
| 24 Aug 2026 | Claimed exotic/modular complex structure on S⁶ ("modular family of 2-tori as a complex structure on S⁶") — would bear on the famous open problem of whether S⁶ admits a complex structure | Claude | **T3, explicitly UNVERIFIED** — site's own note: *"Posted hours before this entry, with no independent check, no formalisation, and no refutation yet in any venue found."* | [vibemathed.com entry](https://vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6) |
| 5 Aug 2026 | **Sendov's conjecture** (open since 1958: every zero of a degree-≥2 complex polynomial with all roots in the unit disk lies within distance 1 of some critical point) — full manuscript + Lean formalisation submitted claiming a proof | credited to human "Lech Mazur, developed with AI agents" (specific model not named on the page) | **T1-partial** — "Lean formalisation checked; acceptance review open" — machine-checked but **not yet accepted/refereed** by the platform's own review process | [proofatlas.ai/advances/](https://www.proofatlas.ai/advances/) |
| 16 Aug 2026 | Bondy's minimum-degree longest-cycle conjecture (graph theory) — claimed formalised proof, 204-module Lean package | Lech Mazur + AI agents (unnamed model) | **T1-partial** — "Lean formalisation checked; acceptance review open" | [proofatlas.ai/advances/](https://www.proofatlas.ai/advances/) |
| 14 Aug 2026 | Counterexample to a conjectured temperature ceiling in Domineering (combinatorial game theory): explicit position with temperature 33/16 > 2 | Lech Mazur + AI agents | **T1-partial**, "Lean-checked, unverified manuscript with adversarial audit" | [proofatlas.ai/advances/](https://www.proofatlas.ai/advances/) |
| 2026 (undated on page) | Counterexample to a Hamilton-decomposition conjecture: explicit regular orientation of K6,6 on 12 vertices with no Hamilton decomposition | Lech Mazur + AI agents | **T1**, "Lean-checked counterexample, accepted" | [proofatlas.ai/advances/](https://www.proofatlas.ai/advances/) |

**UNVERIFIED overall caveat:** every entry above comes from a single tracker's own page copy; none has been
cross-checked against a second independent outlet the way the known-33 list's items were. The YTD and
Carathéodory items in particular would be *very* big if they held up (YTD is a major structural conjecture
in Kähler geometry linking algebraic and differential-geometric stability notions) — but the source site
itself flags both as unverified/uncompiled. Treat as "flood" evidence, not as slide claims about specific
theorems, unless independently corroborated before 27 Aug.

---

## Registry stats

Five separate tracker sites now exist, all launched or substantially populated within the last
~1–7 months (rough proxy for "the trickle becoming a flood"):

| Site | Scale | Verification model | Notes |
|---|---|---|---|
| **proofatlas.ai** | 208 research workspaces, 680,286 "investigation lines" logged, 1,325 cited sources. Status breakdown: 169 open, 14 "recent claim monitored", 22 partially resolved, 1 "finite check remains", 2 solved. | Read-only beta; explicit Lean-checked / accepted vs. "review open" distinction on individual advances | Targets Millennium Prize problems (Riemann, P vs NP, Navier–Stokes, Hodge, BSD, Yang–Mills) plus Hilbert/Erdős/named conjectures as persistent "workspaces" so multiple AI agents don't duplicate work |
| **openproblem.ai / Mathematical Discovery Ledger** | 5,780 canonical problems catalogued; only 10 "published claims" total; 0 verified-core, 1 partial/variant, 1 formalization/rediscovery, 0 disputed | "Evidence Passport": intake → normalization → verification → append-only publication; explicit disclaimer "none implies OpenProblem.ai endorsement" | Still in **"Gate B invited staging," not public production**; loaded from fixtures dated 28 Jul 2026 — i.e. this registry is brand new and admits it is pre-launch |
| **mathdb.com** | **74,382** open problems catalogued (by far the largest raw count of the five) | None visible on scanned pages — no model credit, no verification tags, no per-entry review status | Self-describes as "a community database of open problems in mathematics, designed to keep track of the rapid growth of AI-assisted mathematical breakthroughs" — i.e. exists *because of* the flood, not to referee it |
| **theoremdb.org** | 1,801 reviewed problems (1,770 open / 31 solved); 81 community members; MCP server endpoints for AI agents (Orient / check_plan / record_result) | Four-stage ladder: Reported → Supported → Review pending → Established; example entry status "Resolved. A Lean formalization is attached. Signed verification is pending." | Explicitly built for **machine agents as first-class users** (ChatGPT-integrated "Problem Creator" and "Researcher" agents, MCP protocol) — a tracker designed to be read and written by AI, not just about AI |
| **vibemathed.com** | 630 problems tracked, 445 "fully resolved," only ~22% (~98) Lean-verified; 316 community members, 8,731 combined years-open-before-resolution | Explicit status tags: Proved / Disproved / Under review / Partial / Independent-of-ZFC; per-entry "significance" score and voting | **35 new entries in the last week alone (down 24% w/w — i.e. even faster before)**. Vendor breakdown across 445 solved: OpenAI 357, Anthropic 89, agent/other systems 51, Harmonic (Aristotle) 38, DeepMind 35, xAI 3, open-weights 1. **99% of solutions used closed-source models; only 1% open-weights.** By outcome: proved 278 (63%), disproved 166 (37%), 1 independent-of-axioms. By AI role: AI-discovered 219, AI co-developed 155, AI-assisted only 70 |

**Flood framing for the slide:** five independently-run tracker sites, none older than a few months in
their current form, collectively cataloguing on the order of **tens of thousands of open problems** and
**hundreds of claimed AI resolutions**, with **fewer than 25% Lean-verified** on the one site that reports
that number (vibemathed) and as few as **10 total published claims** on the most rigorous one
(openproblem.ai, which is not even public yet). The generation-vs-verification gap from the known-33 list
holds at the ecosystem level too.

---

## Notable quotes

- **vibemathed.com**, on the S⁶ complex-structure claim: *"Posted hours before this entry, with no
  independent check, no formalisation, and no refutation yet in any venue found."*
- **vibemathed.com**, on the YTD disproof: *"The mathematics was NOT checked here and is beyond quick
  verification."* — also notes six other AI systems failed to reproduce the proof in 12 hours.
- **vibemathed.com**, on the Carathéodory disproof, distinguishing scope from the classical result:
  *"The smooth case falls. Hamburger's real-analytic theorem is untouched."*
- **openproblem.ai**, disclaimer on its own claims ledger: *"[none] implies OpenProblem.ai endorsement."*
- **proofatlas.ai**, on its own beta status: *"Read-only beta: inspect the mathematics now; task, agent,
  and submission controls remain visible but unavailable."*
- **mathdb.com**, self-description: *"a community database of open problems in mathematics, designed to
  keep track of the rapid growth of AI-assisted mathematical breakthroughs."* — the tracker's stated
  reason for existing is the flood itself.
- **theoremdb.org**, example entry status line (Fibonacci-sum indicator determinant conjecture):
  *"Resolved. A Lean formalization is attached. Signed verification is pending."* — a template phrase
  that basically summarises the whole ecosystem's current state.
- **arXiv:2608.24605** authors (Conant, Gannon, Hanson), on their own AI-assisted proof: *"The primary
  focus of this paper is the reverse implications (iii)⇒(ii)⇒(i), which we obtain through the use of AI
  models."* — a rare case of named professional mathematicians stating outright that AI supplied part of
  a published argument, in their own words rather than a tracker's paraphrase.

---

## What I could not verify

- None of the four Aug 2026 "big" claims (YTD disproof, Carathéodory disproof, S⁶ complex structure,
  Sendov's conjecture proof) were checked against a second, independent outlet (e.g. Quanta, a named
  mathematician's blog, or a second tracker). All come from a single tracker's own page. Given how young
  and self-reported these sites are, treat every row in the New Results table as provisional pending
  independent confirmation — this is explicitly weaker sourcing than the known-33 list.
- Could not locate the exact ProofAtlas workspace URL for Sendov's conjecture (guessed slug 404'd);
  detail comes from the `/advances/` summary page only.
- MathDB's specific AI-model attributions were not visible on the pages scanned — its 74,382-entry count
  is a raw open-problem catalogue size, not a count of AI-attributed results; do not conflate the two on
  the slide.
- The recurrence of "Levent Alpöge" and "Claude Fable 5" across both the known Jacobian-conjecture result
  and several of these new vibemathed.com entries may indicate a small number of very active
  human+AI teams rather than a broad-based phenomenon — worth a caveat if citing volume as "many
  independent groups."
