# Fact-check: Jacobian conjecture counterexample & elliptic curve rank record
Compiled 2026-08-26 for München colloquium talk. All items via WebSearch/WebFetch; dates as reported by sources (near-future relative to model training — treat with normal skepticism about source reliability, but this is what the live web currently shows).

---

## Q1 — Jacobian conjecture counterexample: verification status

### Timeline (per multiple corroborating sources)
- **19 Jul 2026**: Levent Alpöge (Harvard / Anthropic) posts on X: "hello there the jacobian conjecture is false thanx," an explicit polynomial map C³→C³ with constant Jacobian determinant −2 that is not globally injective (3-to-1 collision on explicit rational points). Problem suggested by Akhil Mathew; found with Claude (Fable 5). Source: [The Conversation](https://theconversation.com/hello-there-the-jacobian-conjecture-is-false-thanx-why-a-tiny-social-media-post-has-mathematicians-rethinking-ai-283883), [kingy.ai](https://kingy.ai/blog/claude-fable-jacobian-conjecture-counterexample/), [arXiv:2608.00222 abstract](https://arxiv.org/abs/2608.00222).
- **20 Jul 2026**: Alexis Gallagher posts an infinite family of counterexamples generalizing the construction. Source: [arXiv:2608.00222 abstract](https://arxiv.org/abs/2608.00222), [Gallagher's own writeup](https://alexisgallagher.com/posts/2026/jacobianfun/).
- **20 Jul 2026**: Paul Lezeau (Imperial College London, GitHub `Paul-Lez`) opens PR #4474 on Google DeepMind's `formal-conjectures` Lean repository, formalizing the disproof. **Merged 26 Jul 2026**, with reviewer approvals from `mo271`, `alreadydone`, `bkim23`, review comments from Kevin Buzzard (`kbuzzard`) and `josephlr`, code refinements from `deancureton`. Source: [github.com/google-deepmind/formal-conjectures PR #4474](https://github.com/google-deepmind/formal-conjectures/pull/4474).
- **21 Jul 2026**: Terence Tao publishes "A digestion of the Jacobian conjecture counterexample" on his blog, reconstructing the algebraic-geometry mechanism (locally-injective, globally-non-injective polynomial map on an affine 3-fold; degrees 1 and 2 homogeneous pieces) "as a digestion exercise to myself," aiming for a proof with minimal "miracles." Source: [terrytao.wordpress.com, 21 Jul 2026](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) (title/date/summary confirmed via search snippets and secondary coverage — direct fetch returned HTTP 403; content summarized here via [Tildes discussion thread](https://tildes.net/~science/1vav/a_digestion_of_the_jacobian_conjecture_counterexample) which quotes Tao directly, and via [Developers Digest recap](https://www.developersdigest.tech/blog/jacobian-conjecture-counterexample-fable)). UNVERIFIED: I could not directly load Tao's full post text (403 error on WebFetch); all quotes/claims about it are second-hand via search snippets and other blogs quoting it. Recommend a manual check of the URL if possible before the talk.
- **23 Jul 2026**: David Speyer posts a geometric explanation ("tangent-sweep" mechanism via duality of plane curves). Source: [arXiv:2608.00222 abstract](https://arxiv.org/abs/2608.00222).
- **~19–26 Jul 2026**: Independent hand/computer verification reported by named mathematicians: Jared Duker Lichtman (Stanford) "publicly walked through the collision"; Qiaochu Yuan described it as "symbolically easy to verify" and produced a verification script; independent Sage and SymPy calculations confirmed the determinant identity and the 3-way collision. Source: [kingy.ai blog](https://kingy.ai/blog/claude-fable-jacobian-conjecture-counterexample/) (timeline/attribution piece, itself secondary — treat named-verifier claims as UNVERIFIED pending a primary source, e.g. the actual Lichtman/Yuan posts).
- **31 Jul 2026**: arXiv paper **2608.00222**, "Counterexamples to the Jacobian conjecture in dimensions greater than two," posted. Gives a self-contained tangent-sweep construction generalizing the June counterexample to every dimension >2, with 5 new explicit maps (dims 3–5, degrees 4/5/10/6/12). Abstract states: "All identities were verified in exact rational arithmetic; an appendix determines exact fiber structures through Gröbner bases... verification scripts are available from the author." Source: [arxiv.org/abs/2608.00222](https://arxiv.org/abs/2608.00222) / [arxiv.org/html/2608.00222](https://arxiv.org/html/2608.00222). UNVERIFIED / CONFLICTING: the WebFetch tool twice returned the sole author as "Shuhong Gao" with an AI-disclosure note that Claude assisted in proofs/writing — this is inconsistent with the narrative (which credits Alpöge/Gallagher/Speyer as the ones who found the original examples, with this paper being a follow-up generalization by a possibly different author). **This author attribution could not be independently cross-checked and may be a summarization artifact of the fetch tool; verify directly against the arXiv abstract page before citing an author name on a slide.**
- Community aggregator **openconjectures.org** entry `kill-jacobian-2026` tracks the claim status as **"pending peer review"** — i.e., not yet formally refereed in a journal, credited to "Claude Fable 5 with Levent Alpöge." Source: found via search snippet referencing [openconjectures.org/c/kill-jacobian-2026] (page not directly fetched — treat as UNVERIFIED, could not load).

### Current verification status — answer
- **Not machine-checked end-to-end in the sense of a single verified Lean proof of the full theorem statement**, but a Lean **formalization of the specific disproof (the counterexample + injectivity failure) has been merged** into DeepMind's `formal-conjectures` repo (PR #4474, merged 26 Jul 2026, multiple mathematician reviewers including Kevin Buzzard). This is real machine-checked confirmation of the core counterexample claim, though scoped to that example rather than a general theorem, and it postdates the original announcement by ~1 week.
- **Independently verified by multiple named humans**: Terence Tao (full geometric digestion/blog post), Paul Lezeau (Lean formalization + reviewers mo271/alreadydone/bkim23/Buzzard), Jared Duker Lichtman and Qiaochu Yuan (reported public verification/scripts — secondary-sourced, recommend independent confirmation), and Alexis Gallagher / David Speyer (independent generalizations building directly on the reconstructed logic, which is itself a strong form of verification).
- **arXiv writeup exists**: 2608.00222 (31 Jul 2026), generalizing to all dimensions >2, with computer-algebra (exact rational arithmetic + Gröbner basis) verification claimed by the authors.
- **No formal journal peer review yet** — openconjectures.org tracker still lists status as "pending peer review" as of the source snippet retrieved.

**Recommendation for the slide**: Upgrade from **T3 ("announced only, no referee")** to **T2 ("named humans verified")** at minimum — Tao, Lichtman, Yuan, Gallagher, Speyer, and the Lean-PR reviewers (Buzzard et al.) constitute clear named-human independent verification, and this happened within days of the original post. You can additionally note that a **Lean-checked formalization of the counterexample itself was merged** (a machine-checked artifact for the specific example, short of "T1" if T1 in your scheme means a full machine-checked general theorem/proof). Suggested slide wording: **"T2+: independently verified by named mathematicians (Tao, Lichtman, Yuan, Speyer, Gallagher) within days; core counterexample also Lean-formalized (DeepMind formal-conjectures PR #4474, merged) — journal referee review still pending."**

### Sources (Q1)
- https://theconversation.com/hello-there-the-jacobian-conjecture-is-false-thanx-why-a-tiny-social-media-post-has-mathematicians-rethinking-ai-283883
- https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/ (blocked by 403 on direct fetch; corroborated via secondary sources below)
- https://tildes.net/~science/1vav/a_digestion_of_the_jacobian_conjecture_counterexample
- https://www.developersdigest.tech/blog/jacobian-conjecture-counterexample-fable
- https://github.com/google-deepmind/formal-conjectures/pull/4474
- https://arxiv.org/abs/2608.00222 / https://arxiv.org/html/2608.00222
- https://kingy.ai/blog/claude-fable-jacobian-conjecture-counterexample/ (secondary aggregator; named-verifier claims not independently confirmed)
- https://alexisgallagher.com/posts/2026/jacobianfun/
- https://www.sciencedaily.com/releases/2026/08/260804034634.htm
- https://elsolitario.org/en/2026/07/22/jacobian-conjecture-ai-chatgpt/
- (attempted, not loaded) openconjectures.org/c/kill-jacobian-2026 — UNVERIFIED, could not fetch directly

---

## Q2 — New elliptic curve of large rank (2026)

### Findings
- A new record elliptic curve over **Q** with **rank ≥ 30** (unconditional) was submitted to the **ICARM Elliptic Curve Rank Leaderboard** (elliptic-rank.icarm.cloud) under the pseudonymous handle **"ranksunbounded"** around **20 Aug 2026**, subsequently attributed to **Claude, working with Levent Alpöge and Ava Howell** (Anthropic-affiliated). Source: [ICARM curve #273](https://elliptic-rank.icarm.cloud/curve/273), [HN thread "An elliptic curve of rank ≥ 30"](https://news.ycombinator.com/item?id=49374873), [Bartosz Naskręcki on X](https://x.com/nasqret/status/2090429815941685491).
- This breaks the prior records: **rank ≥ 28** (Noam Elkies, 2006) and **rank ≥ 29** (Elkies & Zev Klagsbrun, 2024 — the "18-year gap" record covered by [Quanta Magazine, Nov 2024](https://www.quantamagazine.org/new-elliptic-curve-breaks-18-year-old-record-20241111/)).
- **Rank lower bound of 30 is unconditional**: 30 explicit, linearly independent rational points were exhibited as witnesses. Independence was certified via "an exact quadratic-character 2-descent calculation derived from the Cremona–Brumer method," and every point's on-curve membership checked by exact rational arithmetic (per ICARM leaderboard methodology description). Source: [ICARM leaderboard search summary](https://icarm.io/news/new-record-breaking-elliptic-curve-reported/), [ICARM curve #273](https://elliptic-rank.icarm.cloud/curve/273). No explicit mention of mwrank or Magma by name in the sources found — the described method (Cremona–Brumer 2-descent, exact rational arithmetic) is the standard rigorous independence-certification technique also used in mwrank/Magma-based work, but I could not confirm which specific software package was run. Mark **software tool = UNVERIFIED** (method described, specific tool name not confirmed).
- **Upper bound of 31 (analytic rank) proved under GRH** via Bober's analytic-rank method (referencing arXiv:1112.1503 for the technique); combined with a root-number computation showing the sign is +1 (even rank), this pins the rank at **exactly 30 conditional on GRH + BSD**.
- **A further curve of rank ≥ 31** was submitted shortly after, on **23 Aug 2026** by Ava Howell (ICARM curve #302), again credited to "Claude, Levent Alpöge, and Ava Howell," certified to rank exactly 31 under BSD+GRH, unconditional lower bound 31 via 31 explicit independent points. Source: [ICARM curve #302](https://elliptic-rank.icarm.cloud/curve/302), [Alvaro Lozano-Robledo on X](https://x.com/mathandcobb/status/2091618274320552349).
- **AI involvement**: Both curves are explicitly credited to "Claude" (Anthropic's model) as a co-discoverer alongside Alpöge and Howell, per the leaderboard attributions and social-media commentary (Naskręcki, Lozano-Robledo/mathandcobb). Exact mechanics of how Claude was used (search strategy, point-finding, descent computations) are **not detailed** in any source found — UNVERIFIED as to specifics of the AI's role beyond being named as a co-discoverer.
- **No arXiv paper found** for either curve as of the search date (26 Aug 2026) — the result currently exists only as a leaderboard submission + social-media commentary + a "New record breaking elliptic curve reported" news note on icarm.io, not as a formal preprint. This is UNVERIFIED/likely-absent: searches for an Alpöge–Howell arXiv paper on the rank-30/31 curve(s) returned nothing.
- **No Terence Tao blog post found** specifically discussing this elliptic curve result (searches for "Tao elliptic curve rank 30/31 Alpöge Howell" returned no matching blog content) — treat as **not yet covered by Tao's blog**, at least as of this search.

### Answer summary
- **Who**: Claude (Anthropic model), Levent Alpöge, Ava Howell.
- **When**: rank ≥30 curve ~20 Aug 2026; rank ≥31 curve ~23 Aug 2026 (both very recent, days before this talk).
- **Rank / field**: 30 (then 31), over **Q**.
- **AI involvement**: Yes, explicitly credited as co-discoverer ("Claude, with Levent Alpöge and Ava Howell"); mechanism not publicly detailed.
- **Verification**: Lower bound unconditional (explicit independent rational points, exact-arithmetic + descent-based independence certification per ICARM methodology); exact rank (30, then 31) only under **GRH + BSD** via Bober's analytic-rank method. Not yet an arXiv preprint; reported via the ICARM leaderboard and secondary/social coverage only.

### Sources (Q2)
- https://elliptic-rank.icarm.cloud/curve/273
- https://elliptic-rank.icarm.cloud/curve/302
- https://icarm.io/news/new-record-breaking-elliptic-curve-reported/
- https://news.ycombinator.com/item?id=49374873
- https://x.com/nasqret/status/2090429815941685491
- https://x.com/nasqret/status/2090524721360097594
- https://x.com/mathandcobb/status/2091618274320552349
- https://www.quantamagazine.org/new-elliptic-curve-breaks-18-year-old-record-20241111/ (background: prior rank-29 record, Elkies & Klagsbrun 2024)
- https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html (rank-record history page)

---

## Open items to double-check before the talk (flagged UNVERIFIED above)
1. Direct text of Tao's 21 Jul 2026 blog post (403 on fetch) — worth opening manually in a browser.
2. Author name on arXiv:2608.00222 (tool returned "Shuhong Gao" both times, which sits oddly with the Alpöge/Gallagher/Speyer narrative in its own abstract) — check the abstract page directly.
3. openconjectures.org tracker page for Jacobian conjecture (could not load directly).
4. Exact computational tool (mwrank/Magma/other) used to certify independence of the 30/31 rational points on the record elliptic curves.
5. Whether an arXiv preprint for the rank-30/31 curves has appeared between now and the talk (worth a same-day re-check, since these are days-old results as of 26 Aug 2026).
