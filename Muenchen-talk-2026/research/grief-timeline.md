# The grief timeline: AI and the disruption of software engineering (2021 → Aug 2026), and the beginning of the same process in mathematics and theoretical physics

Research file for *"Large Language Models: A Physicist's Perspective"*, MCQST München, 27 August 2026.
Compiled 24 August 2026.

Companion file: `llm-proof-results.md` (the proof/conjecture ledger, with verification tiers).

---

## How to read this file

**Grounding key.** Every row carries a date and a source. Sources are typed:

- **[web]** — verified this session by search/fetch against a named outlet, arXiv id, or primary blog.
- **[repo]** — taken from source material in this repository (file named in the row).
- **[mk]** — from model knowledge, pre-2026, no live verification. Treat as "well-known but unchecked".

**Epistemic key.** Three different kinds of statement appear here and must not be conflated on a slide:

- **EVENT** — a verifiable public event: a release, a paper, a study, a measured number.
- **CLAIM** — a contested or predictive assertion by a named person. The *utterance* is the event; the *content* may be false.
- **FRAME** — the talk-owner's interpretation. Not a fact. Flagged explicitly.

**Grief stages** used throughout: *shock/denial → anger & dramatic proclamations → bargaining → depression/existential angst → acceptance/recalibration*. The stages overlap and run concurrently in different sub-populations; the labels mark the *dominant public register* at that moment, which is itself a FRAME.

---

## 1. Master chronological table

| Date | Event | Arc | Stage | Significance (one line) | Source |
|---|---|---|---|---|---|
| 29 Jun 2021 | GitHub Copilot technical preview | SWE | pre-shock | Autocomplete becomes statistical; first mass exposure of programmers to a model writing their code | GitHub blog **[mk]** |
| 21 Jun 2022 | Copilot generally available | SWE | pre-shock | Paid product; "AI writes some of my code" becomes a normal sentence | GitHub blog **[mk]** |
| **30 Nov 2022** | **ChatGPT launches** | models | **shock** | The interface, not the model, is the event; everyone can now try it | OpenAI **[mk]**; also cited in `Wuerzburg-talk-2026/slides/talk.tex` "Four moments" **[repo]** |
| 14 Mar 2023 | GPT-4 released; API at $30/M input tokens | models | shock | First model whose coding output is plausible to a professional; anchor for the later cost collapse | OpenAI **[mk]**; pricing **[web]** |
| 12 Feb 2024 | Jensen Huang, World Government Summit: *"It is our job to create computing technology such that nobody has to program… the programming language is human"*; advises children to study biology/chemistry/finance rather than coding | SWE | **anger / proclamation** | The canonical "learning to code is over" utterance, from the person selling the shovels | **CLAIM** — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-advises-against-learning-to-code-leave-it-up-to-ai); [TechRadar](https://www.techradar.com/pro/nvidia-ceo-predicts-the-death-of-coding-jensen-huang-says-ai-will-do-the-work-so-kids-dont-need-to-learn) **[web]** |
| Mar 2024 | Cognition launches **Devin**, "the first AI software engineer" | SWE | anger / proclamation | Peak agent hype; valuation and fear both spike | **CLAIM** — [Codemotion](https://www.codemotion.com/magazine/ai-ml/is-devin-fake/) **[web]** |
| Apr 2024 | **Devin debunked**: Carl Brown (Internet of Bugs) shows the Upwork demo was misrepresented — Devin was fed only the first sentence of the request and the task was cherry-picked. Independent testing: fails ~85% of assigned tasks | SWE | **bargaining begins** | First mass demonstration that a slick agent demo ≠ a working engineer. Immensely reassuring to engineers — and, in hindsight, only *temporarily* correct | [80.lv](https://80.lv/articles/first-ai-software-engineer-creators-are-accused-of-lying); [HN thread](https://news.ycombinator.com/item?id=40008109); [TweakTown](https://www.tweaktown.com/news/102761/worlds-first-ai-software-engineer-fails-85-of-its-assigned-tasks/index.html) **[web]** |
| **25 Jul 2024** | **DeepMind AlphaProof + AlphaGeometry 2: IMO silver-medal standard (28/42)** | maths | **shock (maths arc begins)** | First time a machine performs at elite-competition level on unseen mathematics; graded by IMO judges | DeepMind blog, 25 Jul 2024 — cited as `\bibitem{deepmind2024silver}` in `/home/tobias/Projects/slop-cannon-paper/structured-proofs.tex` **[repo]** + **[web]** |
| **10 Jan 2025** | Zuckerberg (Joe Rogan podcast): AI will do the work of **mid-level engineers** at Meta "this year" | SWE | anger / proclamation | The largest employer of software engineers says the middle of the career ladder is going away | **CLAIM** — [Forbes, 26 Jan 2025](https://www.forbes.com/sites/quickerbettertech/2025/01/26/business-tech-news-zuckerberg-says-ai-will-replace-mid-level-engineers-soon/); [IT Pro](https://www.itpro.com/software/development/a-sign-of-things-to-come-in-software-development-mark-zuckerberg-says-ai-will-be-doing-the-work-of-mid-level-engineers-this-year-and-hes-not-the-only-big-tech-exec-predicting-the-end-of-the-profession) **[web]** |
| **2 Feb 2025** | Karpathy coins **"vibe coding"**: *"you fully give in to the vibes, embrace exponentials, and forget that the code even exists"* — a self-described "shower of thoughts throwaway tweet", 4.5M+ views | SWE | shock → practice | Names the new practice; becomes the year's defining word and, later, its defining insult | [CodeRabbit semantic history](https://www.coderabbit.ai/blog/a-semantic-history-how-the-term-vibe-coding-went-from-a-tweet-to-prod) **[web]** |
| Feb 2025 | Marc Benioff: Salesforce will hire **no new software engineers in 2025**, citing Agentforce productivity | SWE | anger / proclamation | An enterprise CEO converts the prediction into a hiring policy | **CLAIM** — [levels.fyi thread](https://www.levels.fyi/community/thread/9k5IbI/salesforce-will-hire-no-more-software-engineers-in-2025-marc-benioff-says) **[web]** |
| **24 Feb 2025** | **Claude Code** ships as research preview (with Claude 3.7 Sonnet) | SWE / models | **the turn** | Agentic coding leaves the demo and enters the terminal. This is the moment engineers date their "oh f***" to | [Claude Code statistics](https://aibusinessweekly.net/p/claude-code-statistics) **[web]**; "Q1 2025 — Claude Code, Cursor, Copilot" is moment 2 of the Four Moments slide in `Wuerzburg-talk-2026/slides/talk.tex` **[repo]** |
| **10 Mar 2025** | **Dario Amodei** (Council on Foreign Relations): *"I think we'll be there in three to six months, where AI is writing 90 percent of the code. And then in twelve months, we may be in a world where AI is writing essentially all of the code."* He adds the caveat everyone forgot: *"The programmer still needs to specify what are the conditions of what you're doing, what is the overall app…"* | SWE | **peak proclamation** | The single most-quoted, most-mocked prediction of the disruption. The caveat turned out to be the durable part | **CLAIM** — [Yahoo Finance](https://finance.yahoo.com/news/anthropic-ceo-says-ai-could-193020957.html); analysis: [LessWrong](https://www.lesswrong.com/posts/prSnGGAgfWtZexYLp/is-90-of-code-at-anthropic-being-written-by-ais) **[web]** |
| Apr 2025 | Duolingo goes **"AI-first"**: CEO Luis von Ahn's memo — stop using contractors for work AI can do; 10% of workforce already cut. Von Ahn later: *"AI is a better teacher than humans"* | SWE-adjacent | anger / proclamation | The "AI-first" corporate genre reaches its purest form | **CLAIM** — [Inc.](https://www.inc.com/robin-landa/duolingos-ai-first-backlash-a-lesson-in-trust-for-marketers/91228672) **[web]** |
| Apr–May 2025 | **Duolingo backlash**: thousands unfollow on TikTok; von Ahn clarifies "we're still hiring" (23 May 2025). Revenue and stock unaffected (+~30%) | SWE-adjacent | bargaining | Reputational cost is real; financial cost is not. The market did not punish AI-first | [Marketbeat, 23 May 2025](https://www.marketbeat.com/articles/continuing-to-hire-duolingos-ceo-clarifies-ai-stance-after-backlash--read-the-memo-2025-05-23); [TechCrunch, 7 Aug 2025](https://techcrunch.com/2025/08/07/the-backlash-against-duolingo-going-ai-first-didnt-even-matter/) **[web]** |
| **18 May 2025** | **Klarna reverses**: rehires human customer-service agents after replacing ~700 with an OpenAI-built assistant in 2023. CEO Siemiatkowski: *"focused too much on efficiency and cost… the result was lower quality, and that's not sustainable."* Settles into a hybrid: AI front line, humans for escalation and complex cases | SWE-adjacent | **first walk-back** | The canonical "we went too far" data point — but note the nuance: Klarna did **not** remove AI from the high-volume tier | [Forbes, 18 May 2025](https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/) **[web]** |
| May 2025 | Claude Code generally available; Cursor's growth becomes the fastest in SaaS history (0 → $2B ARR in <24 months; $1B ARR and $29.3B valuation by Dec 2025) | SWE | turbulence | The tooling stops being optional. Two-thirds of the Fortune 500 become Cursor customers | [The New Stack](https://thenewstack.io/ai-coding-tool-stack/) **[web]** |
| **May 2025** | **AlphaEvolve**: 4×4 complex matrix multiplication in **48** scalar multiplications (first improvement in 56 years); kissing number in 11 dimensions 592→593; improvements on ~20% of ~50 open problems | maths | shock | First time an AI system *improves a named record in pure mathematics*. Largely ignored outside the field at the time | [DeepMind](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/); [IEEE Spectrum](https://spectrum.ieee.org/deepmind-alphaevolve) **[web]** |
| **10 Jul 2025** | **METR randomised controlled trial**: 16 experienced open-source developers, 246 tasks on mature repos they own. With early-2025 AI tools (mostly Cursor Pro + Claude 3.5/3.7) they were **19% SLOWER** — while estimating afterwards that AI had made them **20% faster** | SWE | **bargaining / the great comfort** | The most-cited counter-evidence of the whole disruption. A 39-point gap between perceived and measured productivity | [METR, 10 Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [arXiv:2507.09089](https://arxiv.org/abs/2507.09089) **[web]** |
| **21 Jul 2025** | **IMO 2025 gold-medal standard (35/42)** — Gemini Deep Think (officially graded) and an OpenAI experimental reasoning model, both in natural language, both missing only problem 6 | maths | **shock deepens** | One year from silver to gold. The maths community's "Devin moment" — except this one was real | DeepMind blog, 21 Jul 2025 — `\bibitem{deepmind2025gold}` in `slop-cannon-paper/structured-proofs.tex` **[repo]** + **[web]** |
| Sep–Oct 2025 | **DORA State of AI-assisted Software Development**: 90% of technology professionals use AI at work; >80% report productivity gains; **and** higher AI adoption correlates with higher software delivery *instability* as well as throughput | SWE | bargaining | The first large-N result that is neither triumphalist nor dismissive: AI raises generation rate faster than review/deploy capacity absorbs it | [dora.dev](https://dora.dev/insights/balancing-ai-tensions/); [RedMonk](https://redmonk.com/rstephens/2025/12/18/dora2025/) **[web]** |
| **Oct 2025** | **Kevin Weil (OpenAI) claims GPT-5 "solved ten previously unsolved Erdős problems."** It had performed a literature search and surfaced *existing* solutions. Retracted; publicly criticised by Demis Hassabis and Yann LeCun | maths | **anger / debunking** | Maths' exact analogue of the Devin debunking (Apr 2024) — and it arrived 18 months later, almost to the month | **CLAIM → retracted** — [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) **[web]** |
| 28 Oct 2025 | Amazon announces 14,000 corporate job cuts (reports of up to 30,000) while accelerating AI capex. CEO Jassy: *"not really financially driven, and it's not even really AI-driven, not right now at least"* | SWE | depression | The layoffs are real; the *attribution* to AI is contested even by the company doing them | **EVENT + contested CLAIM** — [CNBC, 28 Oct 2025](https://www.cnbc.com/2025/10/28/amazon-layoffs-corporate-workers-ai.html); [CNN](https://www.cnn.com/2025/10/27/business/amazon-corporate-layoffs) **[web]** |
| 18 Nov 2025 | Gemini 3 Pro | models | — | Frontier record; ECI 149+ (the reference point for the open-weights lag as of mid-2026) | `Wuerzburg-talk-2026/model-progress/results/key_numbers.md` **[repo]** |
| **25 Nov 2025** | **Claude Opus 4.5: 80.9% on SWE-bench Verified** — first model over 80% | SWE / models | **the threshold** | The benchmark that defined "can it do real engineering work" is effectively saturated | [Vertu comparison](https://vertu.com/lifestyle/claude-opus-4-5-vs-gpt-5-2-codex-head-to-head-coding-benchmark-comparison) **[web]**; "Q4 2025 — Opus 4.5, GPT-5.2 cross a threshold" is moment 3 of the Four Moments slide, `Wuerzburg-talk-2026/slides/talk.tex` **[repo]** |
| 11 Dec 2025 | GPT-5.2: 80.0% SWE-bench Verified (GPT-5.2 Codex, 19 Dec 2025) | models | the threshold | Two labs cross the line within three weeks. It is now an industry property, not one company's | [Vellum](https://www.vellum.ai/blog/gpt-5-2-benchmarks) **[web]** |
| Dec 2025 | **Stack Overflow question volume down 78% year-on-year** — 3,862 questions in Dec 2025. (By Jul 2026: **1,304/month**, against 207,000 in Mar 2014) | SWE | **depression / it's real** | The most legible single number in the whole disruption: an entire institution of the profession evaporating | [Techzine](https://www.techzine.eu/news/devops/137686/stack-overflow-in-freefall-78-percent-drop-in-number-of-questions/); [devclass, 5 Jan 2026](https://www.devclass.com/ai-ml/2026/01/05/dramatic-drop-in-stack-overflow-questions-as-devs-look-elsewhere-for-help/4079575) **[web]** |
| 29 Dec 2025 | **Stack Overflow Developer Survey 2025** (n=49,009, 166 countries, fielded 29 May–23 Jun 2025): **84%** use or plan to use AI tools (up from 76%); trust in AI accuracy down to **29%** (from 40%); **46% actively distrust** vs 33% trust; only **3% highly trust**; the #1 frustration (45%) is *"AI solutions that are almost right, but not quite"*; **66%** report spending more time fixing almost-right AI code | SWE | **acceptance forming** | Adoption and trust move in *opposite* directions. This is the empirical signature of a mature, disillusioned, still-using workforce | [Stack Overflow, 29 Dec 2025](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/); [survey](https://survey.stackoverflow.co/2025/) **[web]** |
| **4 Jan 2026** | **Erdős problem #728 resolved essentially autonomously**: GPT-5.2 Pro produced the informal argument, Harmonic's *Aristotle* produced a Lean proof. Human write-up: N. Sothanaphan | maths | **the turn (maths)** | Maths' "Claude Code moment": the tooling loop (model → formal verifier → human digest) closes for the first time | [arXiv:2601.07421](https://arxiv.org/abs/2601.07421) — `\bibitem{sothanaphan2026erdos}` in `slop-cannon-paper/structured-proofs.tex` **[repo]** + **[web]** |
| 16 Jan 2026 | **Tao's calibration**: GPT-5.2 Pro's Erdős win *"says more about speed than difficulty"* | maths | bargaining | The field's most credible voice immediately supplies the deflator. Note: he does *not* deny it | [The Decoder, 16 Jan 2026](https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/) — `\bibitem{decoder2026tao}` **[repo]** + **[web]** |
| Jan 2026 | DeepMind: Gemini solves 4 Erdős problems and recovers forgotten literature solutions for 9 more | maths | turbulence | Industrial-scale attack on an open-problem list begins | [arXiv:2601.22401](https://arxiv.org/abs/2601.22401) **[web]** |
| 28 Jan 2026 | Amazon cuts a further ~16,000 corporate roles | SWE | depression | The cuts continue regardless of the attribution debate | [CNBC, 28 Jan 2026](https://www.cnbc.com/2026/01/28/amazon-layoffs-anti-bureaucracy-ai.html) **[web]** |
| 29 Jan 2026 | **METR Time Horizon 1.1**: the 50%-reliability task length has doubled every ~7 months for 6 years; over 2024–2025 the doubling time is ~**4 months**. Claude 3.7 Sonnet ≈ 50 min; o3 ≈ 2 h; Opus 4.6 ≈ **12 h** | models | — | The single best quantitative object for "this is not a plateau" | [METR TH1.1, 29 Jan 2026](https://metr.org/blog/2026-1-29-time-horizon-1-1/); [AI Digest](https://theaidigest.org/time-horizons) **[web]** |
| **5 Feb 2026** | **First Proof** launches: 11 working mathematicians contribute 10 *unpublished* research problems from their own work, solutions never posted online | maths | acceptance-machinery | The field builds its own uncontaminated ruler — the maths equivalent of SWE-bench Verified | [1stproof.org](https://1stproof.org/) **[web]** |
| **Feb 2026** | **arXiv:2602.12176, "Single-minus gluon tree amplitudes are nonzero."** GPT-5.2 conjectured the closed-form result and derived a proof over ~12 hours. Authors: Guevara (Harvard), Lupsasca (Vanderbilt), Skinner (Cambridge), Strominger (Harvard), Weil (OpenAI). ⚠️ **This is gauge-theory amplitudes, not string theory** — the Würzburg deck's label should be corrected | physics | **shock (physics arc begins)** | The first result where a model contributed to the *core discovery* in theoretical physics, with senior physicists signing their names | [arXiv:2602.12176](https://arxiv.org/abs/2602.12176); [OpenAI](https://openai.com/index/new-result-theoretical-physics/); [phys.org](https://phys.org/news/2026-02-chatbot-author-ai-stalled-gluon.html) **[web]**; referenced as Hook B in `Wuerzburg-talk-2026/slides/talk.tex` **[repo]** |
| Feb 2026 | Aletheia solves **6/10** First Proof problems fully autonomously | maths | turbulence | The clean benchmark is 60% solved within weeks of being built | [arXiv:2602.21201](https://arxiv.org/abs/2602.21201) **[web]** |
| **24 Feb 2026** | **METR abandons its own experimental design.** Follow-up cohorts: original participants −18% speedup (CI −38% to +9%), new recruits −4% (CI −15% to +9%) — but the design has broken. Developers now **refuse to work without AI even at $50/hour**, and 30–50% of participants avoid submitting tasks they expect AI to accelerate. METR's own conclusion: true speedup is *likely higher* than their data shows | SWE | **acceptance / the comfort expires** | The most important, least-quoted event of the SWE arc. The famous "AI makes devs slower" result has been retired **by its own authors**, and the reason is that AI has become non-optional | [METR, 24 Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/) **[web]** |
| 13 Mar 2026 | **Aletheia** (DeepMind): autonomous math research agent, Generator→Verifier→Reviser. ~91.9% IMO-ProofBench Advanced. Produces an **AI-authored research paper** on eigenweights in arithmetic geometry with no human intervention | maths | turbulence | Not a solver: a researcher. The authorship question becomes concrete | [DeepMind](https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/) **[web]** |
| **31 Mar 2026** | **Bethe Ansatz with an LLM** (Pozsgay & Vona): GPT-5.2/5.4 Pro solves three integrable spin chains — two of them *new* Hamiltonians — semi-autonomously; one solved by a nested Bethe Ansatz with a free-fermionic non-U(1)-invariant nesting level that the model found. Checked against exact diagonalisation | physics | turbulence | The most directly relevant item for a **quantum-many-body / MCQST audience**: this is their field, their methods, their journals | [arXiv:2603.29932](https://arxiv.org/abs/2603.29932) **[web]** |
| Apr 2026 | Gemini 3.1 Flash at **$0.10 / M input tokens** — against GPT-4's $30 / M in Mar 2023: a **~99.7%** price fall in three years for equal-or-better capability | models | — | Cost collapse. The reason "run it a hundred times and check" is now a strategy | [TokenCost AI Price Index](https://tokencost.app/blog/ai-price-index) **[web]** |
| **May 2026** | **arXiv one-year ban policy** for submissions with incontrovertible evidence of unvetted LLM output (hallucinated references, leftover prompts). Suspicious submissions ran at **1 in 277** in the first seven weeks of 2026. Follows Oct 2025 (no unreviewed CS review/position papers) and Dec 2025 (endorsement requirement trialled **in the maths section**) | maths | **depression / institutional strain** | The scholarly infrastructure visibly buckling. Note that maths was the *trial* section | [Science](https://www.science.org/content/article/arxiv-preprint-server-clamps-down-ai-slop); [The Decoder](https://the-decoder.com/arxiv-tightens-moderation-for-computer-science-papers-amid-flood-of-ai-generated-review-articles/) **[web]** |
| **20 May 2026** | **Disproof of the Erdős unit-distance conjecture** (open since 1946). OpenAI internal model; human digest and verification by **Alon, Bloom, Gowers, Litt, Sawin, Shankar, Tsimerman, Wang, Matchett Wood**. Gowers: *"if it had been submitted to the Annals of Mathematics, I would have recommended acceptance without any hesitation. No previous AI-generated proof has come close."* | maths | **the "oh f***" moment (maths)** | The exact analogue of an engineer's first Claude Code session: not "impressive for a machine" but "better than I would have done" | [arXiv:2605.20695](https://arxiv.org/abs/2605.20695) **[repo: Hook A, `Wuerzburg-talk-2026/slides/talk.tex`]** + **[web]**; [Quanta](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| May 2026 | **Deflator on the above**: Gowers reports *relief* that it was a *dis*proof (no wholly novel technique required); Xiao Ma reports GPT-5.5 could also find it given minimal hints; the model succeeded only ~50% of the time at max compute | maths | bargaining | Every genuine shock is followed within days by a competent deflation. This is healthy and should be shown | [Understanding AI](https://www.understandingai.org/p/openais-milestone-math-breakthrough) **[web]** |
| 21 May 2026 | **AlphaProof Nexus**: 9 of 353 formalised open Erdős problems (two open 56 years), 44 OEIS conjectures, a 15-year-old algebraic-geometry question, an improved convex-optimisation bound — all Lean-certified, a few hundred dollars each | maths | turbulence | Verified, cheap, industrial. The cost line is the frightening one | [arXiv:2605.22763](https://arxiv.org/abs/2605.22763) **[web]** |
| 12 May 2026 | Tao announces *"a more restrictive policy"* on publicly digesting new proofs in real time | maths | depression | The field's most generous explainer rate-limits himself. A capacity signal, not a mood signal | [Tao, AI views compilation](https://teorth.github.io/tao-web/ai-views.html) **[web]** |
| 10 Jun 2026 | **First Proof, second batch**: **7 of 10** unpublished research problems receive at least one passing grade (flawless, or minor revisions only) from at least one system. Testing 28 May–1 Jun; expert grading 4–8 Jun | maths | **acceptance-evidence** | The cleanest number in the maths arc: ~70% of genuine, unpublished, research-level problems, refereed by their own authors | [arXiv:2606.18119](https://arxiv.org/abs/2606.18119); [report PDF](https://1stproof.org/assets/docs/report.pdf) **[web]** |
| 21 Jun 2026 | Tao: *"long proofs now easier than short ones"*; *"faster generation has not produced faster progress"* | maths | **acceptance / recalibration** | The bottleneck has moved from generation to digestion — the identical move SWE made in 2025→26 | [Tao AI views](https://teorth.github.io/tao-web/ai-views.html) **[web]** |
| Q2 2026 | Claude Fable 5, GPT-5.6, GLM-5.2 | models | — | Frontier record now falls every **49 days** (was 72); 17.5 models/quarter (was 9.25 in 2023); open weights **6.9 months** behind | `Wuerzburg-talk-2026/model-progress/results/key_numbers.md` **[repo]**; Four Moments slide, moment 4 **[repo]** |
| Jul 2026 | **IMO 2026 (Shanghai): first perfect 42/42 by AI under official grading** — RedNote/Xiaohongshu *dots-note 3.0* and Huawei *Celia*. Neither OpenAI nor DeepMind | maths | — | Two years from silver to perfect; and the frontier moved to labs nobody was watching. ⚠️ single-source, verify | [SCMP](https://www.scmp.com/tech/article/3361482/worlds-first-ai-model-earn-perfect-score-maths-olympiad-comes-chinas-rednote) **[web, low confidence]** |
| 20 Jul 2026 | Kevin Buzzard, *"Human mathematicians are being outcounterexampled"* | maths | acceptance-framing | The correct diagnosis: models excel at *finding objects in large search spaces*, and a counterexample is exactly such an object | [Xena blog](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) **[web, fetch 403 — via index]** |
| **~20–22 Jul 2026** | **Jacobian conjecture false in dimensions ≥ 3.** Levent Alpöge (Anthropic/Harvard) + **Claude Fable 5**, problem suggested by Akhil Mathew. Announced in **one post on X**: *"hello there the jacobian conjecture is false thanx"*. Short enough to verify by hand; several independent confirmations followed | maths | turbulence | Publication itself is disrupted: an 87-year-old conjecture dies in a tweet. Serious epistemic consequences for the record of mathematics | [The Conversation, 22 Jul 2026](https://theconversation.com/hello-there-the-jacobian-conjecture-is-false-thanx-why-a-tiny-social-media-post-has-mathematicians-rethinking-ai-283883) **[web]** |
| 22 Jul 2026 | **Dinitz–Garg–Goemans conjecture** (unsplittable flow, open ~30 years) disproved by an explicit graph. GPT-5.6 Pro, **four prompts, <60 words total**, full chat transcript published. Rybin himself flags: not independently verified | maths/TCS | turbulence | The cost of a 30-year conjecture is now four prompts. Still: **T3, unverified** | [Rybin on X](https://x.com/DmitryRybin1/status/2079904005652893709) **[web]** |
| **24 Jul 2026** | **Tao, ICM 2026 plenary, "Mathematics in the age of AI."** Frames the moment as *"a crisis in the foundations of mathematical values and practices"* — explicitly **not** a capability crisis. Names five stages of mathematical work: proof **generation, verification, exposition, publication, canonicalisation** — AI is strong at the first, improving at the second, and the field's prestige system rewards only the first. Proposes disclosure + verification standards and moving prestige to **digestion** | maths | **ACCEPTANCE — the pivot** | The single most important document of the maths arc. It is, almost line for line, what SWE concluded a year earlier about specification and review | [arXiv:2608.16753](https://arxiv.org/abs/2608.16753); [slides](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf); [Simons Foundation, 13 Aug 2026](https://www.simonsfoundation.org/2026/08/13/fields-medalist-terence-tao-on-artificial-intelligence-and-why-we-do-math/) **[web]** |
| Jul 2026 | Jacob Tsimerman (Toronto) leaves academia for OpenAI. Noga Alon stops working on Erdős problems: *"Once AI started to solve them, there is no point anymore"* — while also saying AI is *"changing dramatically the way mathematical research is being done"* and that *"many and maybe most good mathematicians will use AI"* | maths | **depression / existential angst** | Elite talent both withdrawing *and* migrating. Both are grief responses | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) **[web]** |
| Jul 2026 | **Tech layoffs 2026: 205,832 across 264 firms in the first seven months** — exceeding all of 2025 (123,941) before summer ended. AI named in **87,714** announced cuts through May 2026 (~22% of the year's total), vs 54,836 for all of 2025 | SWE | depression | The pain is real and increasing; the causal attribution to AI is rising but still a minority of cases | [TechCrunch AI-layoff tracker](https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) **[web]** |
| Jul 2026 | **The review bottleneck, quantified.** Faros AI telemetry across ~22,000 developers: task throughput **+33.7%**, median **code review time +441.5%**. Other 2026 measurements: developers using AI complete ~21% more tasks and merge ~98% more PRs, while PR review time rises ~91% | SWE | **ACCEPTANCE — the synthesis** | The bottleneck did not disappear; it *moved*, from writing code to deciding what should be merged. This is the empirical core of "engineers do more than emit code" | [FlowVerify](https://www.flowverify.co/blog/ai-code-review-bottleneck-2026-data); [CIO](https://www.cio.com/article/4207438/the-code-review-crisis-and-how-you-should-rebuild-review-models.html) **[web, aggregator-reported]** |
| Jul 2026 | **Pragmatic Engineer, "State of the software engineering job market in 2026"**: top tech companies hiring ~20% more than a year ago; Apple +10% headcount, Google +5%, Microsoft −1.1%, Amazon −1.3%. Google posting 62% more engineering roles. Many large companies list **50–100% more AI-engineering roles** than a year ago, while general SWE postings remain ~49% below pre-pandemic baseline. Base salaries 15–25% below 2022 peaks. New grads and entry level hit hardest | SWE | **ACCEPTANCE — where it landed** | Not replacement: **bifurcation**. The job exists, is being hired for, pays less, demands more, and has been redefined around AI | [Pragmatic Engineer, 2026](https://newsletter.pragmaticengineer.com/p/state-of-the-job-market-2026); [SignalFire State of Talent 2026](https://www.signalfire.com/blog/signalfire-state-of-talent-report-2026) **[web]** |
| 26 Jul – 4 Aug 2026 | **Kirwin Hampshire, "The Dark Night of Mathematics"** — "a profound spiritual crisis"; *"seeking new math is one of the ways humans touch the ineffable."* Prompted by LLMs disproving multiple long-standing conjectures **in a single week**. Immediate published critiques follow | maths | **DEPRESSION — the named stage** | The field's grief made explicit and public, in the same month as the biggest capability announcement. Perfect slide material | [Substack](https://kirwinhampshire.substack.com/p/the-dark-night-of-mathematics); [critique, Aug 2026](https://mathgames.substack.com/p/a-critique-of-the-dark-night-of-mathematics) **[web]** |
| **1 Aug 2026** | **OpenAI: "Ten advances in mathematics and theoretical computer science."** Internal model **"Astra"**. Ten problems with no progress on the main result for ≥10 years: sphere-packing bounds to the Cohn–Elkies threshold; exponentially improved binary/spherical code bounds; existence of **non-sofic groups**; **disproof of Connes's rigidity conjecture**; arithmetic circuit lower bounds for the permanent; **exponential parallel repetition for all finite two-player entangled games**; n^(1/400) hardness for Euclidean CVP; Ehrhart's volume conjecture; multicolour Ramsey. **Lean 4 certificates for every result**, under **$2,000 per problem**. Not peer reviewed | maths / physics | **THE TRIGGER EVENT** | This is the maths/physics arc's *Claude Code moment* and its *Amodei-90% moment* fused into one, and it happened three weeks before this talk. Note the entangled-games result: it is a **quantum information** theorem | [OpenAI, 1 Aug 2026](https://openai.com/index/ten-advances-in-mathematics/); [PDF](https://cdn.openai.com/pdf/ten-proofs-oai.pdf); [github.com/openai/ten-proofs](https://github.com/openai/ten-proofs); [Simon Willison](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/) — `\bibitem{openai2026ten}` in `slop-cannon-paper/structured-proofs.tex` **[repo]** + **[web]** |
| 3 Aug 2026 | Quanta, *"Why the Legendary Erdős Problems Are Falling to AI"*. Thomas Bloom (curator, erdosproblems.com): *"A big problem is AI is being used a lot by people who aren't mathematicians… no human has read it."* | maths | acceptance / triage | The verification gap becomes the field's stated central problem | [Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) **[web]** |
| 4–19 Aug 2026 | Tao proposes concrete norms: authors claiming credit should commit to developing a proof *"to at least publication stage"* (4 Aug); priority should go to *"the first to explain a result"*, not the first to generate it (6 Aug); a formal mechanism to put proofs *"up for adoption"* when the finder cannot finish them (6 Aug); proofs are *"living beings"* and authors are *"parents"* responsible for raising them to canonical status (19 Aug) | maths | **ACCEPTANCE — new professional norms** | Within three weeks of Astra, the field is already writing its post-disruption professional ethics. This is fast — SWE took ~18 months to get here | [Tao AI views](https://teorth.github.io/tao-web/ai-views.html) **[web]** |
| **27 Aug 2026** | *This talk.* | — | — | SWE: disrupted, not replaced. Maths/physics: roughly where SWE was in mid-2025, and moving faster | **FRAME** |

---

## 2. Where SWE landed — the synthesis

Two claims, each with its strongest evidence. These are the load-bearing conclusions the maths/physics
extrapolation rests on.

### (a) Engineers do more than emit code — and that is now measurable, not sentimental

The 2022–2024 argument "but engineers also do requirements, architecture, taste, and responsibility"
was correct, and was also unfalsifiable and therefore easy to dismiss as cope. In 2026 it became a
number.

- **The bottleneck moved rather than vanished.** Faros AI's 2026 telemetry across ~22,000 developers:
  task throughput **+33.7%**, median **code review time +441.5%**. Independent 2026 measurements:
  ~21% more tasks completed and ~98% more PRs merged, with PR review time up ~91%.
  ([FlowVerify](https://www.flowverify.co/blog/ai-code-review-bottleneck-2026-data),
  [CIO](https://www.cio.com/article/4207438/the-code-review-crisis-and-how-you-should-rebuild-review-models.html))
  The scarce resource is no longer *production of code* but *the judgment that decides what gets merged*.
- **DORA 2025** had already found the mechanism: 90% adoption, >80% self-reported productivity gains,
  **and** a positive association between AI adoption and software delivery *instability* alongside
  throughput. AI raises the generation rate faster than review and deployment capacity can absorb it.
  ([dora.dev](https://dora.dev/insights/balancing-ai-tensions/))
- **Stack Overflow 2025 (n=49,009)**: 84% adoption, 29% trust in accuracy, 46% active distrust, 3%
  high trust; #1 frustration (45%) is *"almost right, but not quite"*; 66% spend more time fixing
  almost-right AI code.
  ([Stack Overflow](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/))
  A workforce that uses a tool constantly and trusts it at 3% is a workforce whose job has become
  *verification*.
- **The market prices this.** Pragmatic Engineer 2026: top tech companies hiring ~20% more than a year
  ago; **50–100% more AI-engineering roles**; general SWE postings still ~49% below pre-pandemic
  baseline; salaries 15–25% below 2022 peaks; entry level worst hit. Not replacement — **bifurcation**,
  around exactly the skill of directing and checking machines.
  ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/state-of-the-job-market-2026))

The verdict: **the job was not eliminated; the part of it that was scarce changed.** Specification,
architecture, review, taste and accountability were always the expensive parts — they were merely
hidden behind the cost of typing.

### (b) Automation has a long tail — and the comfort ran out

- **The strongest "AI doesn't help" result was retired by its own authors.** METR's July 2025 RCT
  (19% slower, 20% perceived faster) was the profession's favourite reassurance for eighteen months.
  On **24 Feb 2026 METR announced it was abandoning the design**: developers now refuse to work without
  AI even at $50/hour, 30–50% of participants avoid submitting tasks they expect AI to accelerate, and
  METR's own reading is that **true speedup is likely higher** than their data shows. The honest
  summary is not "AI slows developers down"; it is "**we no longer have a clean way to measure it,
  because the counterfactual is gone**".
  ([METR Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
  [METR Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/))
- **The dramatic predictions were wrong in their timing and roughly right in their direction.**
  Amodei's March 2025 "90% in 3–6 months" did not happen on schedule; but the caveat he attached in
  the same breath — *"the programmer still needs to specify what are the conditions of what you're
  doing"* — is precisely the world of August 2026.
- **The walk-backs are real but partial.** Klarna rehired humans (May 2025) — into a *hybrid* model,
  with AI still the front line for the bulk of chats. Duolingo took a reputational hit and no financial
  one. The lesson is not "AI-first failed"; it is "**AI-first with no human tier failed**".
- **The institutional damage is permanent even where the jobs survived.** Stack Overflow: 207,000
  questions/month (Mar 2014) → 3,862 (Dec 2025) → **1,304 (Jul 2026)**. A profession's shared memory
  moved into private chat logs. This is the kind of second-order loss nobody predicted and nobody has
  a plan for.

**Where it stands, August 2026:** disrupted, not replaced. Fewer entry-level slots, more senior
leverage, lower pay, higher bar, and a job description reorganised around **specification,
verification, and judgment** — with the review queue as the new critical path.

---

## 3. Mathematics and theoretical physics is here

### The mapping

| SWE event | Date | ↔ | Maths/physics analogue | Date | Offset |
|---|---|---|---|---|---|
| Copilot preview — a machine writes plausible code | Jun 2021 | ↔ | AlphaProof/AlphaGeometry IMO silver — a machine does plausible mathematics | Jul 2024 | **~3 yr** |
| ChatGPT — everyone can try it | Nov 2022 | ↔ | IMO gold in natural language; every mathematician tries the same models | Jul 2025 | **~2 yr 8 mo** |
| Devin: "the first AI software engineer" | Mar 2024 | ↔ | Kevin Weil: "GPT-5 solved ten Erdős problems" | Oct 2025 | **~19 mo** |
| Devin debunked (Internet of Bugs; fails ~85%) | Apr 2024 | ↔ | The Weil claim retracted — it was a literature search; Hassabis and LeCun object | Oct 2025 | **~18 mo** |
| Claude Code ships; agentic coding enters daily practice | Feb 2025 | ↔ | Erdős #728: model → Lean verifier → human write-up loop closes | Jan 2026 | **~11 mo** |
| Amodei: "90% of code in 3–6 months" | Mar 2025 | ↔ | OpenAI "Astra": ten decade-open problems, Lean-certified, <$2k each | **1 Aug 2026** | **~17 mo** |
| The "oh f***" moment: it is better than I expected at *my* job | ~Q2 2025 | ↔ | Unit-distance disproof; Gowers: "would have recommended *Annals* acceptance without hesitation" | 20 May 2026 | **~12 mo** |
| METR RCT: the comforting counter-evidence | Jul 2025 | ↔ | Tao: "says more about speed than difficulty"; Gowers' relief that it was a *dis*proof; Xiao Ma's GPT-5.5 replication | Jan–May 2026 | **~7 mo** |
| Stack Overflow collapses; institutions strain | 2025–26 | ↔ | arXiv bans unchecked-LLM authors; endorsement trialled **in maths**; 1-in-277 suspicious | Oct 2025 – May 2026 | **~0–6 mo** |
| Layoffs, existential angst, "was my career a mistake" | 2025–26 | ↔ | *"The Dark Night of Mathematics"*; Alon quits Erdős problems; Tsimerman leaves academia for OpenAI | Jul–Aug 2026 | **~12 mo** |
| DORA/Faros: the bottleneck moved to review | 2025–26 | ↔ | Tao: *"faster generation has not produced faster progress"*; prestige must move to **digestion** | Jun–Jul 2026 | **~9 mo** |
| Job redefined: specification, verification, judgment | 2026 | ↔ | Tao's five stages: generation, **verification, exposition, publication, canonicalisation** | Jul 2026 | **~6 mo** |

### The offset, and why it is shrinking

Measured on the earliest anchors the offset is about **three years** (Copilot 2021 → AlphaProof 2024).
Measured on the most recent it is **six to twelve months** (SWE's 2026 review-bottleneck synthesis ↔
Tao's July 2026 ICM framing). **The gap is closing at roughly a year per year.**

The mechanism is not mysterious and should be stated plainly in the talk: mathematics did not have to
build the tooling. The agentic harnesses, the RL-on-verifiable-rewards recipe, the long-horizon
scaffolds and the cost curve were all constructed for code, and *Lean is code*. Formal mathematics
inherited a fully-built industry. That is why maths is compressing into eighteen months an arc that
took software engineering five years.

**A working estimate for the talk (FRAME):** mathematics and theoretical physics in August 2026 sit
roughly where software engineering sat in **mid-2025** — past denial, past the first debunking, deep
in the turbulence, with the acceptance vocabulary already being written by the field's most credible
people. But they will not take another eighteen months to get to 2026's synthesis; on current slope,
**mid-2027**.

Physics specifically is roughly **12–18 months behind mathematics** on the same curve: the gluon
amplitudes paper (Feb 2026) and the Bethe-ansatz work (Mar 2026) are physics' Erdős-#728 moment —
credible, senior-signed, single results — with no Astra-scale event yet. Note that Astra's
**exponential parallel repetition for finite two-player entangled games** is a quantum-information
theorem, so the first breach into a quantum-physics-adjacent area has already happened, on 1 Aug 2026.

### Projected next phases (FRAME — clearly labelled as extrapolation)

1. **Late 2026 — the verification crunch.** Referee capacity, not model capacity, becomes the binding
   constraint. Expect explicit journal policies on AI-derived results, a formal-certificate norm for
   certain classes of claims, and at least one high-profile AI-derived result found to be wrong after
   celebration. The 🔴 and ⚪ markers on Tao's tracker are the leading indicator.
2. **2027 — prestige reallocation.** Tao's proposal (credit to the first to *explain*, "adoption" for
   orphaned proofs) either becomes a norm or fails visibly. Hiring, prizes, and PhD structure follow
   or don't. This is the true fork in the road, and it is a *sociological* fork, not a technical one.
3. **2027 — the bifurcation.** Mathematics splits the way SWE did: enormous demand for people who can
   pose problems, formalise, verify and digest at scale; contraction in problem classes that are
   pure search. Entry level hit hardest, exactly as in SWE.
4. **The physics-specific turn.** Physics has a defence mathematics lacks: **experiment**. But it also
   has a vulnerability mathematics lacks: much of theoretical physics is not formalisable in Lean, so
   the verification loop that made maths tractable does not transfer. Expect physics to be *slower to
   fall and slower to check* — which is the worse combination, and worth saying out loud to this
   audience.

---

## 4. Positive extrapolation — grounds for "be ambitious, aim high"

Six bullets, each with its number and source. The argument is not "AI will do it for you"; it is
**"the ceiling on what one person can attempt has risen by an order of magnitude, and the people who
recognised that first are the ones doing the interesting work"**.

1. **Capability is still rising linearly on a ruler that cannot saturate.** Epoch Capabilities Index:
   **+13.0 points/year** at the frontier, no ceiling in sight, across 179 models since 2023. Every
   benchmark that *can* saturate has: GPQA Diamond is at **94.6%** against expert humans at 69.7%.
   The apparent plateaus are artefacts of the ruler, not the models.
   `Wuerzburg-talk-2026/model-progress/results/key_numbers.md` **[repo]**

2. **And there is still a long way to go — which is the *good* news for a researcher.** **CritPt**,
   research-level physics problems, tops out at **32.3%**. Humanity's Last Exam at 46.4%. FrontierMath
   at 52.4%. The frontier of *your* field is not solved. There is room to be the person who works out
   how to close it.
   `model-progress/results/key_numbers.md` **[repo]**

3. **The cost of an attempt has collapsed by ~1000×.** GPT-4 at $30/M input tokens (Mar 2023) →
   Gemini 3.1 Flash at $0.10/M (Apr 2026): a **~99.7%** fall for equal-or-better capability. Concretely:
   AlphaProof Nexus resolved decade-open Erdős problems at **a few hundred dollars each**; OpenAI's
   Astra results came in at **under $2,000 per problem**. "Try it a hundred ways and check" is now a
   research strategy a single person can afford.
   [TokenCost](https://tokencost.app/blog/ai-price-index); [arXiv:2605.22763](https://arxiv.org/abs/2605.22763);
   [OpenAI, 1 Aug 2026](https://openai.com/index/ten-advances-in-mathematics/) **[web]**

4. **The horizon over which a model can act autonomously is doubling every ~4–7 months.** METR TH1.1
   (29 Jan 2026): 50%-reliability task length has doubled every ~7 months for six years, and every
   ~**4 months** over 2024–25. GPT-2: 2 seconds. Claude 3.7 Sonnet: 50 minutes. o3: ~2 hours.
   Opus 4.6: ~**12 hours**. Whatever you can specify and check, you can increasingly delegate.
   [METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/) **[web]**

5. **The models arrive faster than anyone can evaluate them — and open weights are only ~6 months
   behind.** New best-ever model every **49 days** (was 72); 17.5 models/quarter (was 9.25 in 2023);
   open-weights lag median **5.7 months** since 2025, currently 6.9 (GLM-5.2). You do not need to be
   at a frontier lab to work at close to the frontier.
   `model-progress/results/key_numbers.md` **[repo]**

6. **The historical lesson from SWE is unambiguous about who did well.** Not the people who denied it
   (the METR result they leaned on was withdrawn by its own authors in Feb 2026), and not the people
   who surrendered to it (the 2025 "vibe coding" cohort produced the review crisis of 2026 —
   +441.5% review time). **The people who did well adopted orchestration and verification early**:
   they learned to specify precisely, to build the checking apparatus, and to own the result. That is
   exactly what Tao is now proposing for mathematics — credit to the person who *digests and explains*,
   not the one who generates. The transferable skill is not prompting. It is **taste, specification,
   and the discipline of verification** — and physicists already own all three.
   [METR Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/);
   [Faros/FlowVerify 2026](https://www.flowverify.co/blog/ai-code-review-bottleneck-2026-data);
   [Tao, ICM 2026, arXiv:2608.16753](https://arxiv.org/abs/2608.16753) **[web]**

**The closing frame (FRAME):** every previous automation of a technical craft raised, not lowered,
the ambition of the people who stayed. The unit of work moves up. If a decade-open conjecture now
costs $2,000, the correct response is not to ask what is left to do — it is to ask **what you would
attempt if the tedious 90% were free**. Aim there.

---

## 5. Slide-ready distillation

Three slides. Each item ≤10 words, each dated, chosen to maximise information per line.

### Slide A — The SWE grief timeline (10 items)

| Date | Line (≤10 words) | Stage |
|---|---|---|
| Nov 2022 | ChatGPT launches — everyone can suddenly try it | shock |
| Feb 2024 | Huang: "nobody should learn to code" | anger |
| Mar 2024 | Devin: "the first AI software engineer" | anger |
| Apr 2024 | Devin debunked — fails 85% of tasks | bargaining |
| Feb 2025 | Karpathy: "vibe coding"; Claude Code ships | the turn |
| Mar 2025 | Amodei: "90% of code in six months" | peak proclamation |
| May 2025 | Klarna rehires the humans it replaced | first walk-back |
| Jul 2025 | METR RCT: experienced devs 19% slower | the great comfort |
| Nov 2025 | Opus 4.5 first past 80% SWE-bench | threshold crossed |
| Feb 2026 | METR retires that study — no counterfactual left | comfort expires |
| Jul 2026 | Review time +441%, throughput +34% | bottleneck moved |
| 2026 | Hiring returns, bifurcated: AI roles +50–100% | acceptance |

### Slide B — Maths/physics: the same arc, offset (10 items, paired)

| SWE | ↔ | Maths/physics |
|---|---|---|
| Jun 2021 Copilot writes plausible code | ↔ | Jul 2024 IMO silver: AlphaProof |
| Nov 2022 ChatGPT: everyone tries it | ↔ | Jul 2025 IMO gold, in natural language |
| Mar 2024 Devin hype | ↔ | Oct 2025 "GPT-5 solved ten Erdős problems" |
| Apr 2024 Devin debunked | ↔ | Oct 2025 Retracted — it was literature search |
| Feb 2025 Claude Code: the tooling loop closes | ↔ | Jan 2026 Erdős #728: model → Lean → human |
| Q2 2025 "Oh f***, it's better than expected" | ↔ | May 2026 Unit distance falls; Gowers: "Annals, no hesitation" |
| Mar 2025 Amodei: "90% of code" | ↔ | **Aug 2026 Astra: ten conjectures, Lean-certified, $2k each** |
| Jul 2025 METR: the comforting counter-evidence | ↔ | Jan 2026 Tao: "speed, not difficulty" |
| 2025–26 Stack Overflow collapses | ↔ | May 2026 arXiv bans unchecked-LLM authors |
| 2026 Bottleneck moved to review | ↔ | Jul 2026 Tao: prestige must move to digestion |

Closing line for the slide: **offset ~3 years in 2024, ~9 months now — and shrinking, because maths
inherited the tooling built for code.**

### Slide C — The extended timeline: be ambitious (8 items)

| Number | Line (≤10 words) |
|---|---|
| +13.0 ECI pts/yr | Capability still linear on a ruler without a ceiling |
| 94.6% vs 69.7% | GPQA saturated; experts overtaken in early 2025 |
| 32.3% | CritPt research physics — your frontier is still open |
| ~1000× | Cost per attempt collapsed, 2023 → 2026 |
| $2,000 | Price of a decade-open conjecture, August 2026 |
| ×2 / 4 months | Autonomous task horizon: 2 s → 12 hours |
| 49 days | New best-ever model; open weights 6.9 months behind |
| Feb 2026 | "AI slows devs" withdrawn — by its own authors |
| 2026 | Thrived: those who adopted orchestration and verification early |
| — | **Ask what you'd attempt if the tedious 90% were free** |

---

## 6. Caveats and unverified items

- **Correction for the deck:** arXiv:2602.12176 is *"Single-minus gluon tree amplitudes are nonzero"* —
  gauge-theory scattering amplitudes, not string theory. Strominger and Skinner are authors, which is
  the likely origin of the mislabel. Recommend "a new result in theoretical physics" or
  "gauge-theory amplitudes".
- **IMO 2026 perfect scores (42/42, RedNote dots-note 3.0 and Huawei Celia)** rest on a single strong
  outlet (SCMP) plus aggregators. Verify before putting on a slide.
- **The Faros AI "+441.5% review time" and "output per engineer +60%" figures** come from vendor
  telemetry reported by aggregators, not a peer-reviewed study. Directionally corroborated by DORA
  2025 and by Stack Overflow's 66% "fixing almost-right code" figure, but the precise number should
  be attributed carefully or rounded to "review time up several-fold".
- **Kevin Buzzard's Xena post** returned HTTP 403 to direct fetch; summarised via the search index and
  corroborating coverage.
- **The exact composition of Astra's ten problems** comes from secondary coverage of OpenAI's PDF.
  Read <https://cdn.openai.com/pdf/ten-proofs-oai.pdf> directly before naming a specific problem on a slide.
- **Grief-stage labels are the talk-owner's FRAME**, not a claim about anyone's actual emotional state.
  The stages overlap and run concurrently in different sub-populations.
- **Pre-2025 dates marked [mk]** (Copilot preview 29 Jun 2021, Copilot GA 21 Jun 2022, ChatGPT
  30 Nov 2022, GPT-4 14 Mar 2023) are from model knowledge and were not re-verified this session;
  they are uncontroversial but should be spot-checked if quoted to the day.
