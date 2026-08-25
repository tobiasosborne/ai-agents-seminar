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
