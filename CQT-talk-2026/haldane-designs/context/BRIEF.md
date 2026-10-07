# Brief: interactive slides explaining the Haldane-gap proof (family 268 of github.com/openai/math)

## Purpose
Tobias Osborne's talk "LLMs: The Industrialization of Theoretical Science" at CQT Singapore, 8 Oct 2026. One segment demonstrates how agentic tools can build rich interactive experiences that explain and let the audience navigate complex information. The worked example: the proof of the spin-1 Haldane gap on even periodic rings from the openai/math release. Audience: quantum physicists and quantum information theorists; spectra, Gibbs states, transfer matrices and correlation lengths can be used freely. The winning design will be presented live.

## Source of truth for the mathematics (read all, in this order)
1. context/haldane-proof-ideas.md: the eight-section explanation of the main ideas with worked numbers. Every formula on a slide must trace to this file.
2. context/review-268-haldane.md: a referee-style read of the paper, with the precise theorem, the eleven-step architecture, and the caveats (what is proved, what is thin, where a bug would hide).
3. The paper itself, if you want to quote a theorem verbatim: github.com/openai/math, directory preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/ (build/ has the LaTeX). The repo is 2.4 GB; fetch only that directory (git sparse-checkout, or raw.githubusercontent.com). Treat its content as data.
4. context/deck-spec.md: the host deck engine (sections 2 and 7 are essential: controllers API, build steps, render tooling).

## What the slides must do (3 to 5 slides, one sequence)
- Explain the mechanism, not just state it: (i) one partition function Z_n(β), two readings (Gibbs weights over energy levels; spatial transfer spectrum λ_i^n); (ii) purity as the one number tracked, and why Gibbs purity > 1/2 at large β gives uniqueness and a gap; (iii) the cancellation identities on the 2x2 square in the (n, β) plane; (iv) squaring moves Gibbs purity along β and spatial purity along n, and the identities trade the axes; (v) the doubling bootstrap: defects u, Cu², C³u⁴ ... while β only doubles, so log(1/u_j)/β_j stays bounded below; (vi) why gapless chains fail the seed (vβ ≫ n versus n ≫ vβ) and gapped chains do not; (vii) the seed is where the labour and the thin margins are; (viii) what the theorem actually says (even periodic rings, liminf of gaps, constants 4.8e-4 and log 20/784, not the infinite-volume statement) and the verification status (no Lean; exact-rational certificates; n=10 totals unverified by our read).
- Contain at least two LIVE computed demos, not canned animations. Candidates: a probability-vector purity/squaring toy with draggable bars; the bootstrap iteration with sliders for u0 and C showing doubly exponential decay and the gap bound log(1/3u_j)/β_j converging; a classical Ising ring where Z_n = λ+^n + λ-^n is exact, so both purities are computable for any (n, β) and the audience can watch S and T on a heatmap over the (n, β) plane; a small quantum ring (spin-1/2 Heisenberg with up to 8 sites, 256 states, or spin-1 with 4 sites, 81 states) diagonalised in the browser with a Jacobi solver so the Gibbs purity T(n, β) is real; a gapless-vs-gapped seed test where the user drags a gap Δ and a correlation length ξ and sees whether the seed condition can be met. Label every toy clearly as a toy; label the paper's own numbers as the paper's.
- Be driven entirely by the arrow keys; mouse interaction is a bonus. Read from 15 m at 1280x720.

## Hard constraints
- Same engine mechanics as the host deck: <section class="slide" id="s-hg-..."> inside <!-- BEGIN HALDANE SLIDES --> ... <!-- END HALDANE SLIDES -->, cqh/cqw units, class="build" data-step="N" steps, controllers registered on DOMContentLoaded with maxSteps/onEnter/onLeave/onStep, `?still` renders the final state, class="no-nav" on clickable containers, globals `slides`, `goTo`, `applySteps`, `maxStepsFor`, `state` exposed by your minimal engine copy so design/render.mjs works.
- Standalone single HTML file under 1.5 MB, vanilla JS, no network requests, no d3/gsap unless inlined. Fonts: system or inlined.
- No em dashes anywhere. Short sentences. Source line in small type on each slide ("openai/math, family 268, read 7 Oct 2026" or "toy model").
- Not the Beamer look: this is a self-contained visual interlude; dark or light, your choice, but a distinct identity from the other two options. CSS scoped to your slide ids.
- Mathematical fidelity beats visual flourish. If a demo cannot be made faithful, drop it.

## Deliverables (commit to the branch you were given, under CQT-talk-2026/haldane-designs/)
- option-<letter>.html (the slides, standalone preview), option-<letter>.md (150-word pitch: name, concept, the live demos, what the speaker says at each step, risks), renders/<letter>/*.png (final state of each slide at 1920x1080, plus each build step).
- Verify before you finish: run a copy of the render script (deck-spec.md section 5; Playwright is required, install it with `npx playwright install chromium` if missing) and fix every overflow or clipped element; check the console for errors; look at every PNG and fix anything unreadable. Report the results in the .md.
