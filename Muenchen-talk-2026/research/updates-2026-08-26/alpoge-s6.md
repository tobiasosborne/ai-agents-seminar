# alpo.ge/s6.pdf — Alpöge's claimed complex structure on S⁶

**Downloaded:** 2026-08-26, from https://alpo.ge/s6.pdf (200 OK, 1,113,315 bytes, PDF 1.7, 108 pages).
Local copy: `/tmp/claude-1000/-home-tobias-Projects-ai-agents-seminar/61cb6b74-a3e2-4bd5-88e5-e7a0c81966ab/scratchpad/s6.pdf`

**PDF metadata:** no Title/Author/Subject/Keywords set; Creator "LaTeX with hyperref"; Producer pdfTeX-1.40.27; CreationDate/ModDate both stamped to the SOURCE_DATE_EPOCH default `1980-01-01` (i.e. deliberately stripped/reproducible-build date — the real posting date has to come from external sources, not the file).

## What the document is

**NOT** the Jacobian-conjecture counterexample. That was a separate, much shorter result (a single explicit polynomial map posted on X in July 2026). This PDF is a **different, unrelated claim**: a purported resolution of the **Hopf problem** — whether the 6-sphere S⁶ admits an integrable complex structure — open since 1947/48.

- **Title (page 1, restated on p.3):** *"The (3,4,∞) modular family of 2-tori, completed at its three special points, is a complex structure on S⁶"* / equivalently *"A compact complex threefold fibred by tori over the projective line, and the six-sphere."*
- **Author:** not printed anywhere in the PDF itself (no name, affiliation, or email appears in 108 pages — checked via full-text grep for "acknowledg", "thank", "email", "@", author name variants). Authorship is established only externally: Levent Alpöge (mathematician, works at/with Anthropic) has publicly claimed the result on X, crediting Claude for the write-up.
- **Date:** not stated in the PDF (stripped metadata, no dated preprint header, no arXiv number). External reporting (Terry Tao's blog, X posts, tech press) places the announcement around **21 July – early August 2026** (contemporaneous with the Jacobian-conjecture news cycle, which is a separate result by the same person).

## Main mathematical claims

The paper constructs an explicit compact connected complex 3-manifold $X$ with a holomorphic map $f: X \to \mathbb{P}^1$ such that:

1. Over $B^\circ = \mathbb{P}^1 \setminus \{p_0,p_1,p_2\}$, $f$ is a proper holomorphic submersion with fibres = complex 2-tori, built from explicit period functions $\tau,\mu,\beta$ on the upper half-plane for the $(3,4,\infty)$ triangle-group orbifold ($\tau$ is literally the elliptic modular function, $j(\tau) = 1728t$).
2. The fibre over $p_0$ is a reduced, irreducible normal-crossings divisor $W$: the normalisation of $W$ is a degree-six del Pezzo surface $dP_6$ with the three pairs of opposite sides of its anticanonical hexagon glued together (Mumford-style toric degeneration).
3. The fibres over $p_1, p_2$ are non-reduced/multiple (multiplicities 3 and 4) with bielliptic reductions $S_1, S_2$, produced by Kodaira logarithmic transforms.
4. **Main theorem:** $X$ is simply connected with $H_*(X;\mathbb{Z}) \cong H_*(S^6;\mathbb{Z})$ ($e(X)=c_3(X)=2$), hence (Hurewicz+Whitehead+Smale+ $\Theta_6=0$) $X$ is **diffeomorphic to $S^6$**.
5. **Corollary 1.1:** "The six-sphere $S^6$ carries an integrable complex structure" — transported from $X$ along the diffeomorphism.
6. Algebraic dimension $a(X)=1$ (not Moishezon, not Kähler, $b_2(X)=0$); the construction is not metric-related and bears no relation to the classical octonionic almost-complex structure on $S^6$ (that one is known non-integrable, Nijenhuis tensor nowhere zero — LeBrun's theorem).

**Section 10 is a direct, explicit confrontation with a published contradiction.** Campana–Demailly–Peternell (CDP98 + a 2020 corrigendum "CDP20") had proved that any compact complex threefold homeomorphic to $S^6$ must have algebraic dimension $a(X)=0$ — which would directly rule out this construction's $a(X)=1$. Alpöge's paper states point-blank: *"The Theorem contradicts [CDP20, Cor. 2.3] as published,"* and devotes an entire section to locating the exact step where the CDP proof fails for this $X$: their argument implicitly assumes $H^0(\widetilde{\Omega}^1_S \otimes A)=0$ on the reduced fibre, which requires a non-normal-crossings hypothesis that fails precisely because $W$ (the fibre over $p_0$) is non-normal. The paper proves (Thm 10.5) $R^2f_*(T_X\otimes L)\neq 0$ for *every* line bundle $L$, which is the condition under which the CDP argument breaks down. This is presented as "repairing" the discrepancy in the literature by identifying which prior published lemma doesn't apply, rather than claiming CDP's paper is simply wrong.

This is an unusually confrontational move for a paper claiming to resolve a 78-year-old problem: it explicitly says an existing peer-reviewed theorem (in a corrected/corrigendum'd paper, no less) does not apply to its own construction, and stakes the whole result on that being correct.

## AI / LLM involvement

- **Inside the PDF itself: zero mentions.** Full-text search of all 108 pages for "Claude," "Anthropic," "AI," "LLM," "GPT," "large language model," "Opus," or any acknowledgments/model-credit language returns **nothing**. The paper reads as a conventional, dense, notation-heavy algebraic/complex-geometry preprint with no AI disclosure, no methods statement about how it was produced, and no acknowledgments section at all.
- **Outside the PDF (per press/social coverage):** Alpöge has said Claude was "heavily involved" and that he had **Claude Opus 5** write out the full 100+ page argument, with the core construction reproducible from the first page or two of the PDF. Coverage (officechai, HuggingNews, KuCoin, X posts from Justin Curry and Mark Kretschmann) frames this as Alpöge (an Anthropic researcher/mathematician) doing the mathematical work in collaboration with Claude, which then produced the fully written-out, page-length formal argument.
- **Slide-worthy tension:** the paper that is being sold externally as "Claude solved the Hopf problem" contains **no trace of that framing internally** — a reader encountering the PDF cold would have no way to know an LLM was involved at all. The AI-authorship claim lives entirely in the surrounding social-media/press layer, not in the artifact itself.

## Verification status

- **Not Lean-checked / not formalized** — nothing in the paper or coverage mentions formal verification (Lean, Coq, Isabelle). This is a traditional human-language mathematical proof, not machine-checked.
- **Not peer-reviewed.** No journal, no arXiv identifier found for *this* paper (contrast with the Jacobian-conjecture counterexample, which was tracked on openconjectures.org as "pending peer review"). This S⁶ paper appears to exist only as a self-hosted PDF on Alpöge's personal domain (alpo.ge) plus derivative commentary (e.g. a "VibeMathed" community-checking page at vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6).
- **Announced, not vetted.** Community reaction (Reddit, X) is described as interested but cautious, "immediately focused on the difficulty of independently checking such a subtle result." Coverage explicitly frames it as a first-party claim, not an independently confirmed proof.
- **Loaded historical context:** the Hopf problem has a graveyard of retracted/disputed claims in both directions — including a well-publicized 2016 claim by Michael Atiyah that S⁶ has *no* complex structure, later widely rejected by experts, and a paper literally titled "The Non-Existent Complex 6-Sphere" (arXiv:1610.09366) rebutting an earlier purported construction. Alpöge's own paper is aware of this literature (cites LeBrun's no-go theorem, Etesi's disputed construction, and calls the field's history one of "many faulty advances").
- The paper's own §1.2 candidly states it directly contradicts a corrected, published theorem (CDP20) and that resolving the contradiction is the crux of the whole paper (§10) — i.e., the author has identified the single most likely point of failure and pre-argued it, but this has not yet been checked by independent experts.

## Quotable lines for the talk

- Abstract: *"We prove that X is simply connected with the integral homology of $S^6$, hence diffeomorphic to $S^6$, ... together with $f_*\mathcal{O}_X=\mathcal{O}$, ... $K_X \cong f^*\mathcal{O}(-1)\otimes\mathcal{O}_X(2S_2)$, ... and $\mathrm{Aut}^0(X)\cong\mathbb{C}^*$. The existence of such an X is incompatible with [CDP20, Cor. 2.3]; the last section locates the point at which the two accounts diverge..."*
- §1.2: *"The Main Theorem is incompatible with a published result... it therefore contradicts [CDP20, Thm 2.2] and [CDP20, Cor. 2.3]... this failure is repairable for the purpose of the proof of Cor. 2.3 at X (§10), unlike the reduction at the non-normal fibre, which is decisive."*
- §1.4 (context / self-aware history): *"...no complex structure on $S^6$ is orthogonal with respect to the round metric... The structure constructed here is not produced from a metric and carries no a priori relation to the round one... Constructions of complex structures on $S^6$ have been claimed by entirely different means... nothing here depends on them or bears on their validity."*
- The single strongest "AI-generated math is arriving faster than verification" line for the talk is not *in* the paper — it's the juxtaposition: **a 108-page, fully symbolic, notation-dense proof that a named AI model (Claude Opus 5) is reported to have written start-to-finish, addressing and attempting to overturn a corrected 2020 peer-reviewed theorem, self-hosted with no journal, no arXiv number, no Lean check, and zero internal acknowledgment that AI was involved at all** — released within days/weeks of the same author's separate, already-famous Jacobian-conjecture counterexample.

## Sources consulted (web, for context not in the PDF)

- https://x.com/mark_k/status/2091964029283573913 (announcement thread)
- https://x.com/currying/status/2091718876102803916 (Justin Curry reaction, calls out Atiyah's 2016 claim)
- https://officechai.com/ai/anthropic-researcher-says-claude-helped-build-a-complex-structure-on-s%E2%81%B6-taking-aim-at-the-unsolved-hopf-problem/
- https://huggingnews.com/ai/levent-alpoge-solves-6-sphere-problem-open-since-1948-with-claude-577b0fa2
- https://www.kucoin.com/news/flash/ai-breaks-78-year-old-math-conjecture-on-s-complex-structure
- https://vibemathed.com/problem/modular-family-of-2-tori-as-a-complex-structure-on-s6
- (context, separate result) https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
- (context, separate result) https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/
