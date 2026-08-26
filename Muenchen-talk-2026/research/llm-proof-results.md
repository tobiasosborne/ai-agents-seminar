# LLM-assisted proofs and conjecture resolutions, 2024 → August 2026

Compiled 24 August 2026 for *"Large Language Models: A Physicist's Perspective"*, MCQST München, 27 Aug 2026.

**Purpose of this file:** the flurry is real, but it is *heterogeneous in how well checked it is*. The
verification-status column is the point. A slide that lists ten results without tiers is propaganda;
a slide that lists ten results with tiers is a physics talk.

---

## Verification tiers (used throughout)

| Tier | Meaning |
|---|---|
| **T1** | Machine-checked (Lean 4 or equivalent) **or** peer-reviewed and published. Strongest bar. |
| **T2** | arXiv preprint with **named human mathematicians** who verified/digested/rewrote the argument. Not yet refereed. |
| **T3** | Announced only — blog post, X/Twitter thread, company blog, shared chat transcript. Unreviewed at time of announcement. |
| **T4** | Claimed but **disputed, corrected, or retracted**. |

Two honest caveats that apply to *every* T1 row:
1. A Lean certificate attests to **formal derivability from the formal statement**, not to the
   faithfulness of the formalisation — i.e. not that the Lean theorem says what the English
   theorem says. This is the standard objection and it has not gone away.
2. "Not peer reviewed" is true of essentially everything from 2026. The refereeing pipeline has
   not caught up.

---

## Master table

Ordered chronologically. "Model" = the system credited by the source. Aggregator-only sources are
marked *(secondary)*.

| Date | Problem / result (field) | Model(s) | Humans | Tier | Source |
|---|---|---|---|---|---|
| 25 Jul 2024 | IMO 2024, silver-medal standard (28/42) | AlphaProof + AlphaGeometry 2 (DeepMind) | DeepMind team; official IMO graders | **T1** (graded by IMO judges; Lean-based) | [DeepMind blog, 25 Jul 2024](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) |
| 21 Jul 2025 | IMO 2025, gold-medal standard (35/42), natural language | Gemini Deep Think; separately an OpenAI experimental reasoning model | DeepMind / OpenAI teams; IMO graders (DeepMind's run was officially graded) | **T1/T2** (DeepMind officially graded; OpenAI self-graded → weaker) | [DeepMind blog, 21 Jul 2025](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) |
| May 2025 | 4×4 complex matrix multiplication in **48** scalar multiplications (first improvement on the Strassen-derived 49 in 56 years); kissing number in 11 dimensions 592 → **593**; improvements on ~20% of ~50 open problems in analysis/geometry/combinatorics/number theory | AlphaEvolve (Gemini-powered evolutionary coding agent) | DeepMind team | **T1** (explicit constructions, machine-checkable by direct computation) | [DeepMind AlphaEvolve blog, May 2025](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) |
| Nov 2025 | AlphaEvolve at scale: 67 problems across analysis, combinatorics, geometry, number theory | AlphaEvolve | DeepMind + external mathematicians | **T2** | [arXiv:2511.02864](https://arxiv.org/abs/2511.02864) |
| **Oct 2025** | **Claim:** GPT-5 "solved ten previously unsolved Erdős problems". **Reality:** the model performed a literature search and surfaced *existing* solutions. Retracted; publicly criticised by Demis Hassabis and Yann LeCun. | GPT-5 | Kevin Weil (OpenAI) | **T4 — retracted** | Widely reported; see [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) and [The Decoder, 16 Jan 2026](https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/) |
| Dec 2025 | Erdős problem **#333** (set sums) | GPT-5.2 | Kevin Barreto, Ben Price | **T2/T3** | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| 4 Jan 2026 | Erdős problem **#728** — first Erdős problem resolved essentially autonomously by AI. GPT-5.2 Pro produced the informal argument; Harmonic's *Aristotle* produced a Lean proof. | GPT-5.2 Pro + Aristotle (Harmonic) | Kevin Barreto (announcer); N. Sothanaphan (human write-up); Terence Tao (commentary) | **T1** (Lean) + **T2** (arXiv write-up) | [arXiv:2601.07421](https://arxiv.org/abs/2601.07421); [erdosproblems.com](https://www.erdosproblems.com/) |
| 16 Jan 2026 | Tao's caution on #728: the win "says more about speed than difficulty" — the problem was tractable, the model was fast | — | Terence Tao | commentary | [The Decoder, 16 Jan 2026](https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/) |
| Jan 2026 | DeepMind: 4 Erdős problems solved; forgotten literature solutions found for 9 more | Gemini | DeepMind team | **T2** | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/); [arXiv:2601.22401](https://arxiv.org/abs/2601.22401) |
| Jan 2026 | Erdős problems #729, #397 also credited to GPT-5.2 | GPT-5.2 | community contributors | **T3** (tracker entries) | [erdosproblems wiki, AI contributions](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) |
| 5 Feb 2026 | **First Proof** benchmark launched: ten *unpublished* research problems contributed by eleven working mathematicians, solutions never posted online | multiple systems | Mohammed Abouzaid, Nikhil Srivastava et al. | **T1** (refereed grading by the problem authors) | [1stproof.org](https://1stproof.org/); [arXiv:2606.18119](https://arxiv.org/abs/2606.18119) |
| Feb 2026 | Aletheia solves **6/10** First Proof problems fully autonomously | Aletheia (advanced Gemini Deep Think) | DeepMind | **T2** | [arXiv:2602.21201](https://arxiv.org/abs/2602.21201) |
| **Feb 2026** | **"Single-minus gluon tree amplitudes are nonzero"** — new closed-form result in gauge-theory scattering amplitudes. GPT-5.2 conjectured the formula, then derived a proof over ~12 hours. ⚠️ **This is amplitudes / QFT, not string theory** — correct the deck if it says "string theory". | GPT-5.2 | Alfredo Guevara (Harvard), Alex Lupsasca (Vanderbilt), David Skinner (Cambridge), Andrew Strominger (Harvard), Kevin Weil (OpenAI) | **T2** (arXiv, five named physicists as authors/verifiers) | [arXiv:2602.12176](https://arxiv.org/abs/2602.12176); [OpenAI announcement](https://openai.com/index/new-result-theoretical-physics/) |
| 13 Mar 2026 | **Aletheia** announced: autonomous math research agent (Generator → Verifier → Reviser harness). ~91.9% on IMO-ProofBench Advanced. Produced an AI-authored research paper computing "eigenweights" in arithmetic geometry with no human intervention. Semi-autonomous sweep of ~700 problems in Bloom's Erdős database → 4 autonomous solutions. | Aletheia (Gemini Deep Think) | DeepMind | **T2** | [DeepMind blog](https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/); [MarkTechPost, 13 Mar 2026](https://www.marktechpost.com/2026/03/13/google-deepmind-introduces-aletheia-the-ai-agent-moving-from-math-competitions-to-fully-autonomous-professional-research-discoveries/) *(secondary)* |
| Mar 2026 | New bounds on multicolour Ramsey numbers via reinforced generation of combinatorial structures | LLM + RL search | DeepMind-affiliated authors | **T2** | [arXiv:2603.09172](https://arxiv.org/abs/2603.09172) |
| **31 Mar 2026** | **Bethe Ansatz for three integrable spin chains, two of them new Hamiltonians.** The third is solved by a nested Bethe Ansatz whose nesting level has a free-fermionic, non-U(1)-invariant structure — a structure *found by the model*. Results cross-checked against exact diagonalisation. | ChatGPT 5.2 Pro and 5.4 Pro | Balázs Pozsgay, István Vona | **T2** (arXiv; independently checked numerically and by the authors) | [arXiv:2603.29932](https://arxiv.org/abs/2603.29932) |
| May 2026 | New bounds for Zarankiewicz numbers via reinforced LLM evolutionary search | LLM evolutionary search | named authors | **T2** | [arXiv:2605.01120](https://arxiv.org/abs/2605.01120) |
| May 2026 | Erdős problem **#1196** (primitive sets) | multiple models | Terence Tao, Jared Duker Lichtman (co-authors) | **T2** | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| May 2026 | Erdős **#1102**, Tao + van Doorn collaboration mediated by AI | AI-assisted | Terence Tao, Wouter van Doorn | **T2** | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| **20 May 2026** | **Disproof of the Erdős unit-distance conjecture** (planar unit-distance problem, open since 1946 — ~80 years). AI constructed a high-dimensional lattice from algebraic integers (high-degree CM fields, infinite class field towers) and projected to the plane. Model succeeded ~50% of the time at maximum compute. | OpenAI internal model | Human digest + verification: **Noga Alon, Thomas Bloom, W. T. Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, Melanie Matchett Wood.** Sawin subsequently derived explicit bounds. | **T2** — strongest T2 on this list | [arXiv:2605.20695](https://arxiv.org/abs/2605.20695); [OpenAI announcement, 20 May 2026]; [phys.org, May 2026](https://phys.org/news/2026-05-ai-major-breakthrough-math-problem.html) |
| 20 May 2026 | Gowers on the above: *"if it had been submitted to the Annals of Mathematics, I would have recommended acceptance without any hesitation. No previous AI-generated proof has come close."* Tsimerman: *"a really impressive piece of work… definitely an intimidating construction."* Gowers also reports **relief** on learning it was a *dis*proof rather than a proof — the techniques were not wholly novel. | — | Gowers, Tsimerman | commentary | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/); [Understanding AI](https://www.understandingai.org/p/openais-milestone-math-breakthrough) |
| May 2026 | **Deflationary note on the above:** researcher Xiao Ma reports GPT-5.5 could also produce the disproof given minimal hints — suggesting the result was closer to the reachable frontier than headlines implied. | GPT-5.5 | Xiao Ma | **T3** (report) | [Understanding AI](https://www.understandingai.org/p/openais-milestone-math-breakthrough) |
| **21 May 2026** | **AlphaProof Nexus**: 9 of 353 formalised open Erdős problems resolved (two open 56 years); 44 previously unproven OEIS conjectures; a 15-year-old open question in algebraic geometry; an improved convergence bound in convex optimisation via a novel parameter schedule. Cost: a few hundred dollars per problem. | Gemini 3.1 Pro + Lean compiler loop | DeepMind team | **T1** (Lean 4 certificates, verifiable in seconds) | [arXiv:2605.22763](https://arxiv.org/abs/2605.22763); [The Decoder](https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/) |
| May 2026 | Logical Intelligence (co-founded by Yann LeCun; Mike Freedman involved) autoformalised a ChatGPT-generated paper in Lean — a counterexample built on Golod–Shafarevich | ChatGPT + autoformaliser | Mike Freedman et al. | **T2/T3** | [Xena blog, 20 Jul 2026](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) *(fetch blocked 403; via search index)* |
| 10 Jun 2026 | **First Proof, second batch**: ten new unpublished research problems; **7 of 10 received at least one passing grade** (essentially flawless, or minor revisions only) from at least one system. Systems: ChatGPT 5.5 Pro plus academic harnesses from ETH Zürich/Aarhus, UCLA, Princeton. Testing 28 May–1 Jun 2026; grading 4–8 Jun 2026. | GPT-5.5 Pro + academic harnesses | Abouzaid, Srivastava, + 9 contributors | **T1** (expert refereeing for correctness *and* exposition) | [arXiv:2606.18119](https://arxiv.org/abs/2606.18119); [1stproof.org report](https://1stproof.org/assets/docs/report.pdf) |
| Jun 2026 | New lower bounds for the degree/diameter problem, obtained by interaction with a browser-accessible LLM | consumer-grade LLM | named author(s) | **T2** | [arXiv:2606.15860](https://arxiv.org/abs/2606.15860) |
| Jul 2026 | IMO 2026 (Shanghai): **first perfect 42/42 by AI under the IMO's own official grading** — Xiaohongshu/RedNote *dots-note 3.0*, and Huawei *Celia*. Notably neither OpenAI nor DeepMind. | dots-note 3.0; Celia | IMO official graders | **T1** (official grading) — but see caveat below | [SCMP](https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote) *(single-source; verify before using on a slide)* |
| 20 Jul 2026 | Kevin Buzzard, *"Human mathematicians are being outcounterexampled"* — the framing essay on this whole phenomenon: AI is disproportionately good at *finding objects* in large search spaces, which is exactly what counterexamples are | — | Kevin Buzzard | commentary | [Xena blog, 20 Jul 2026](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) |
| **~20–22 Jul 2026** | **Counterexample to the Jacobian conjecture in dimension 3** (hence false in all dimensions ≥ 3; the 2-dimensional case, stated 1939, remains open). An explicit polynomial map with constant Jacobian determinant −2 that is not injective. **Announced in a single post on X** — "hello there the jacobian conjecture is false thanx". Short enough that other mathematicians verified it directly; several independent confirmations followed. | Claude Fable 5 | Levent Alpöge (Anthropic / Harvard); problem suggested by Akhil Mathew | **T3 → T2** (announced on X, then independently verified by several mathematicians; no formal certificate reported) | [The Conversation, 22 Jul 2026](https://theconversation.com/hello-there-the-jacobian-conjecture-is-false-thanx-why-a-tiny-social-media-post-has-mathematicians-rethinking-ai-283883); [Smithsonian](https://www.smithsonianmag.com/smart-news/ai-disproves-a-decades-old-mathematical-idea-the-biggest-conjecture-that-the-tech-has-played-a-role-in-yet-180989189/); [ScienceDaily, 4 Aug 2026](https://sciencedaily.com/releases/2026/08/260804034634.htm) |
| **22 Jul 2026** | **Counterexample to the Dinitz–Garg–Goemans conjecture** (unsplittable flow / combinatorial optimisation, open ~30 years since ~1999). A graph with fractional flow cost 58 where every unsplittable flow with capacity violation ≤ 15 costs ≥ 60. Found from **four prompts totalling under 60 words**; the full chat transcript was published. | GPT-5.6 Pro | Dmitry Rybin | **T3** — announced on X only; Rybin himself flags it as not independently verified. The object is a finite graph, so it *is* checkable by direct computation. | [Rybin on X, 22 Jul 2026](https://x.com/DmitryRybin1/status/2079904005652893709); [DataCamp writeup](https://www.datacamp.com/blog/gpt-5-6-dinitz-garg-goemans-conjecture) *(secondary)* |
| 24 Jul 2026 | Tao, ICM 2026 plenary lecture *"Mathematics in the age of AI"* — frames the moment as *"a crisis in the foundations of mathematical values and practices"*, not a capability crisis | — | Terence Tao | **T1** (ICM Proceedings) | [arXiv:2608.16753](https://arxiv.org/abs/2608.16753); [slides](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf) |
| **1 Aug 2026** | **OpenAI, "Ten advances in mathematics and theoretical computer science."** Ten problems with no progress on the main result for ≥ 10 years, several much longer. Reported list includes: sphere-packing upper bounds down to the Cohn–Elkies threshold; exponentially improved bounds on binary and spherical codes; **existence of non-sofic groups**; **disproof of Connes's rigidity conjecture**; arithmetic circuit lower bounds for the permanent (Ω(n² log log n) gates, Ω(n⁴/log n) formula leaves); **exponential parallel repetition for all finite two-player entangled games**; n^(1/400) hardness for the Euclidean closest vector problem via direct 3SAT reduction; Ehrhart's volume conjecture; multicolour Ramsey numbers; plus 3 further Erdős problems. Under **$2,000 per problem** at GPT-5.6 Sol token prices. | "Astra" (OpenAI internal next-generation model) | OpenAI; no external referees at announcement | **T1 (Lean 4 certificates)** but **not peer reviewed**, and the certificates attest to formal derivability, not faithful formalisation | [OpenAI, 1 Aug 2026](https://openai.com/index/ten-advances-in-mathematics/); [PDF](https://cdn.openai.com/pdf/ten-proofs-oai.pdf); [github.com/openai/ten-proofs](https://github.com/openai/ten-proofs); [Simon Willison, 1 Aug 2026](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/) |
| Aug 2026 | Six Erdős problems solved in five days by one person (46% success rate over 13 attempts) | GPT-5.6 Sol + Codex | Shouqiao Wang | **T3** | [36kr report](https://eu.36kr.com/en/p/3908956256605577) *(secondary; low-confidence — verify before quoting)* |
| Aug 2026 | Kirwin Hampshire, *"The Dark Night of Mathematics"* — the field's grief essay; "a profound spiritual crisis" | — | Kirwin Hampshire | commentary | [Substack](https://kirwinhampshire.substack.com/p/the-dark-night-of-mathematics); [critique](https://mathgames.substack.com/p/a-critique-of-the-dark-night-of-mathematics) |

---

## The tracker: the honest denominator

The single most useful object for this talk is **Terence Tao's `erdosproblems` wiki page,
"AI contributions to Erdős problems"** —
<https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erdős-problems>

It classifies contributions into:

- **1(a) AI standalone** — no comparable prior literature. ~56 entries, Jan–Jun 2026.
- **1(b) AI alongside literature** — comparable literature found *afterwards*. ~25 entries.
- **1(c) AI building on literature** — ~36 entries.
- **1(d) AI collaborating with humans** — 141+ entries.
- **Secondary contributions** — hundreds: literature search, Lean formalisation, proof rewriting, computation.

And — this is the load-bearing detail — it carries **four status markers**:

> 🟢 full resolution 🟡 partial progress 🔴 **incorrect work** ⚪ **unverified**

Both 🔴 and ⚪ are populated. Contra the press coverage, the community's own tracker *already*
distinguishes checked from unchecked, and a non-trivial fraction of AI "solutions" is either wrong
or has never been read by a human. Thomas Bloom, who curates erdosproblems.com:

> "A big problem is AI is being used a lot by people who aren't mathematicians… no human has read it."
> — [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)

Context: erdosproblems.com holds **1,217 problems, of which 565 (46%) are marked solved** — so the
AI contributions, dramatic as they are, sit inside a much larger human corpus.

Corroborating institutional signal: **arXiv now bans authors for one year** for submissions with
incontrovertible evidence of unvetted LLM output (policy announced ~May 2026), after suspicious
submissions ran at **1 in 277** in the first seven weeks of 2026
([Science](https://www.science.org/content/article/arxiv-preprint-server-clamps-down-ai-slop)).

---

## What I could not verify

- **OpenAI's 20 May 2026 unit-distance announcement page** — the arXiv digest (2605.20695) is solid
  and directly verified; I did not fetch OpenAI's own announcement URL.
- **The Xena blog post** returned HTTP 403 to direct fetch; its content is summarised here from the
  search index and from the corroborating Conversation/Smithsonian coverage. Treat the
  Freedman/Logical Intelligence row as the weakest on the list.
- **IMO 2026 perfect scores** rest on a single strong outlet (SCMP) plus aggregators. Verify before
  putting "42/42" on a slide.
- **Shouqiao Wang's six-in-five-days** and the exact composition of OpenAI's ten problems come from
  secondary aggregators; the OpenAI PDF is the primary source for the latter and should be read
  directly if any specific problem is named on a slide.
- **The Wuerzburg deck labels arXiv:2602.12176 the "OpenAI string-theory paper."** It is
  *"Single-minus gluon tree amplitudes are nonzero"* — tree-level gauge-theory scattering
  amplitudes. Strominger and Skinner are on it, which is presumably where "string theory" came
  from, but the result is a QFT amplitudes result. **Recommend relabelling** to
  "gauge-theory scattering amplitudes" or "a new result in theoretical physics".

---

## Slide-ready distillation — "the flurry, and how much of it is checked"

Eight strongest items, one line each, with tier. Designed so the tier column is the punchline.

| # | Item | Tier |
|---|---|---|
| 1 | **Jul 2025** — IMO gold, natural language, officially graded (DeepMind) | **T1** |
| 2 | **Jan 2026** — Erdős #728, first autonomous solve; Lean certificate | **T1** |
| 3 | **Feb 2026** — new amplitudes result, 5 named physicists, arXiv:2602.12176 | **T2** |
| 4 | **Mar 2026** — Bethe ansatz for two *new* integrable chains, checked vs exact diagonalisation | **T2** |
| 5 | **May 2026** — unit-distance conjecture disproved; 9 mathematicians digested it; Gowers: "would have recommended Annals acceptance" | **T2** |
| 6 | **May 2026** — AlphaProof Nexus: 9 Erdős + 44 OEIS, Lean-certified, few hundred $ each | **T1** |
| 7 | **Jul 2026** — Jacobian conjecture false in dim ≥ 3 — **announced in one post on X** | **T3→T2** |
| 8 | **Aug 2026** — OpenAI "Astra": ten decade-open problems, Lean certificates, < $2k each — **zero referees** | **T1 formal / unreviewed** |

**The counterpoint line for the same slide** (this is what makes it a physics talk and not a press
release): the community's own tracker, Tao's `erdosproblems` wiki, marks entries 🔴 *incorrect* and
⚪ *unverified* alongside 🟢 — and Bloom's warning that *"no human has read it"* applies to a real
fraction. Meanwhile arXiv is banning authors for unchecked LLM output at a rate of roughly
1 suspicious submission in 277.

**The one-sentence summary:** *the generation of mathematics has been automated faster than the
verification of mathematics, and the gap is the whole story.*

---

## Deck updates 26 Aug

Content-integration pass on `slides-web/talk.html` for the 27 Aug talk. Two slides now open the
flood section: `s-flurry` (reworked in place, 10 tiered result rows) and `s-floodstats` (new,
inserted immediately after it). Everything below is what went **on a slide**, with its tier and
its source, so the deck stays auditable.

### New rows added to `s-flurry`

| Date | Row text on the slide | Tier used | Source |
|---|---|---|---|
| Jun 2026 | Jamming exponents, a 12-year-old identity: Parisi (Nobel) and Zamponi, with Claude, over forty rounds of dialogue. Peer reviewed, *J. Stat. Mech.* | **T2+** (new badge: refereed journal) | [arXiv:2606.03300](https://arxiv.org/abs/2606.03300); *J. Stat. Mech.* (2026) 073301, [doi:10.1088/1742-5468/ae7bd7](https://doi.org/10.1088/1742-5468/ae7bd7); [phys.org, 1 Jul 2026](https://phys.org/news/2026-06-physicists-ai-claude-collaborate-year.html); [Physics World](https://physicsworld.com/a/ai-model-helps-physics-nobel-laureate-out-of-a-decade-old-mathematical-jam/); [Zenodo transcript](https://zenodo.org/records/20633432) |
| Jul 2026 | Complex structure on S⁶, open since 1947: 108 pages, self-hosted, no arXiv | **T3** | [alpo.ge/s6.pdf](https://alpo.ge/s6.pdf) (108 pp, no author printed, no AI disclosure inside); [vibemathed entry](https://vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6); [officechai](https://officechai.com/ai/anthropic-researcher-says-claude-helped-build-a-complex-structure-on-s%E2%81%B6-taking-aim-at-the-unsolved-hopf-problem/); [X announcement thread](https://x.com/mark_k/status/2091964029283573913) |
| Aug 2026 | Schiffer and Pompeiu conjectures disproved, Lean-verified counterexample | **T1** | [aimath.robertj1.com](https://aimath.robertj1.com/) (entry dated 5 Aug 2026; registry lists GPT-5.6 / Claude) |
| Aug 2026 | Elliptic curve rank record over Q broken twice in a week: ≥ 30, then ≥ 31 | **T3** | [ICARM curve #273 (rank ≥ 30, ~20 Aug)](https://elliptic-rank.icarm.cloud/curve/273); [ICARM curve #302 (rank ≥ 31, 23 Aug)](https://elliptic-rank.icarm.cloud/curve/302); [icarm.io news note](https://icarm.io/news/new-record-breaking-elliptic-curve-reported/); [Quanta on the prior Elkies–Klagsbrun 29 record, 2024](https://www.quantamagazine.org/new-elliptic-curve-breaks-18-year-old-record-20241111/) |

Also added, in the Jacobian quote box, a second caption line: *"The same author's 108-page S⁶
paper: self-hosted, no arXiv, and reportedly written out by Claude."* The AI-authorship claim
exists **only** in the social/press layer ([X](https://x.com/mark_k/status/2091964029283573913),
officechai, huggingnews). The PDF itself contains no author, no acknowledgments and zero mentions
of Claude/AI in 108 pages. "Reportedly" is load-bearing; do not drop it.

**New tier badge.** A refereed journal paper exceeds T2 (named humans read it) but is not T1 as the
deck defines T1 (machine-checked or officially graded). Rather than mislabel it, the legend now
carries a fourth chip, **T2+ = refereed journal**, medblue like T2. Only the Parisi–Zamponi row uses
it. The Jacobian row stays **T2** (Tao's digestion, Lichtman, Yuan, Speyer, Gallagher, plus the
merged Lean PR; see the Q1 section of `updates-2026-08-26/jacobian-elliptic.md`).

### Rows dropped from `s-flurry` (for space, at 10 rows)

- **Jul 2025, IMO gold, officially graded (T1).** Reprised two slides later on `s-mathslag` with
  fuller context. Dropping it also makes every row on the slide fall inside the last eight months,
  and the row cadence (Jan 1, Feb 1, Mar 1, May 1, Jun 1, Jul 2, Aug 3) now *shows* the acceleration.
- **May 2026, AlphaProof Nexus, 9 Erdős + 44 OEIS (T1).** Redundant against the Aug 2026 "Astra"
  row, which carries the same "industrial scale, Lean, cheap" point more recently and with the
  "zero referees" punch.

### `s-floodstats` (new slide, "Now somebody has to count it")

All figures exactly as sourced; each panel carries its own date stamp on the slide.

| Figure on the slide | Value | Source |
|---|---|---|
| Claimed AI-solved results in one registry | **506** (253 proved, 116 disproved, 7 both, 130 unclassified) | [aimath.robertj1.com](https://aimath.robertj1.com/), page last updated 21 Aug 2026 |
| Monthly split, drawn as one proportion bar | **239** before July, **166** in July, **101** 1–21 Aug → **267 of 506 in the last eight weeks** | same; the 239 is 506 − 166 − 101 |
| Problems tracked / resolved / Lean-verified | **630 / 445 / 98**, i.e. 22% of the resolved | [vibemathed.com](https://vibemathed.com/) |
| Weekly inflow | **35** new entries in the last week, down 24% on the week before | vibemathed.com |
| Open problems catalogued, no verification tags | **74,382** | [mathdb.com](https://mathdb.com/) |
| Problems reviewed / solved, MCP endpoints for agents | **1,801** / 31 | [theoremdb.org](https://theoremdb.org/) |
| Research workspaces, read-only beta | **208** | [proofatlas.ai](https://www.proofatlas.ai/advances/) |
| Palomar launch; its editorial stage uses an LLM to check the formal statement against the informal claim | **18 Aug 2026** | [Tao's blog, 18 Aug 2026](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/); [palomar-registry.org](https://palomar-registry.org/) |
| Published claims / verified-core on the strictest registry | **10 / 0** | [openproblem.ai Mathematical Discovery Ledger](https://openproblem.ai/mathematical-discovery-ledger/) |
| "Nine independent registries, none older than seven months" | aimath, Lax, lemma.ing, Palomar, proofatlas, openproblem.ai, mathdb, theoremdb, vibemathed | `updates-2026-08-26/trackers-A.md` and `trackers-B.md` |

Two of the nine (laxarchive.org, lemma.ing) are counted in the kicker but not shown as cards; the
slide says "five more of them" for the card strip, so the arithmetic is honest if anyone asks.

**Correction to the brief.** The August figure is **101 entries in 1–21 Aug**, not "101 in 26 days":
`aimath.robertj1.com` was last updated 21 Aug 2026, so the August bar covers three weeks, and the
slide labels it "1–21 Aug". Per-day, August (≈4.8/day) is therefore *not* faster than July
(≈5.35/day); the honest acceleration claim, and the one the slide makes, is that **267 of the 506
entries arrived in the last eight weeks**.

### Deliberately left off both slides

- **Yau–Tian–Donaldson (CSCK) disproof claim, 19 Aug**: six other AI systems failed to reproduce it
  in 12 hours; tracker's own note says the mathematics was not checked.
- **Sendov's conjecture**: proofatlas lists a Lean-checked claim (5 Aug, "Lech Mazur + AI agents"),
  while trackers-A reads Tao's Palomar submission as a formalisation *demo*, not a resolution.
  Conflicting; not slide-safe.
- **IMO 2026 "42/42"**: only two systems (Huawei Celia, Xiaohongshu dots-note 3.0) were officially
  graded; the other four self-graded. Too much caveat for one row.
- **Matrix-multiplication exponent < 2.371177 (17 Aug, AlphaEvolve + Alman + Vassilevska Williams,
  T2)**, **Crouzeix (4 Aug)**, **Kourovka batch (20 Jul)**, **Carathéodory C^∞ (19 Aug)**,
  **Bethe-ansatz-adjacent registry items**: all real, all cut purely for row budget. The
  matrix-multiplication item is the strongest reserve if a row ever frees up.
- Anything a research file marks UNVERIFIED, including every `aimath.robertj1.com` row that has not
  been cross-checked against arXiv (the Schiffer/Pompeiu row is the one exception admitted, on the
  strength of it being explicitly labelled Lean-verified by the registry).

### Other deck change

`s-errorcorr` closing line, which after the reorder now sits *inside* the agent section rather than
after it: "The agent toolbox from the last section is exactly the cure" → **"Every cure on the right
is a tool the agent loop already gives us."**

### Pending

An HTML comment marker `<!-- ARXIV-ACK-FIGURE-HERE -->` sits immediately after `s-floodstats`,
reserving the position for the arXiv acknowledgment figure (fraction of quant-ph and math-ph
submissions whose acknowledgments name an LLM, over time; produced by
`arxiv-acknowledgments/analyse.py`). It is intended to become its own full-bleed figure slide
`s-arxivack`, built like `s-hookB`. Adding it takes the deck from 66 slides to 67.
