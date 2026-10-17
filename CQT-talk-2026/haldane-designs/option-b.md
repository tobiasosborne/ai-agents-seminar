# Option B: Two Lenses

**Pitch (150 words).** One persistent object: the (n, beta) plane, both axes log2, coloured by purity for a toy whose partition function is exact, the classical Ising ring with Z_n = lambda_+^n + lambda_-^n. Two lenses read the same Z: the physical lens T(n, beta) = Z_n(2 beta)/Z_n(beta)^2 and the spatial lens S(n, beta) = Z_2n(beta)/Z_n(beta)^2. On log2 axes every doubling (n, beta) to (2n, 2 beta) is one 45-degree hop, so the bootstrap is a straight staircase. Light paper, one vermilion accent, serif display type. Live: two draggable probes with exact Gibbs and transfer weights; a draggable 2x2 square with both cancellation identities evaluated to 12 digits; the squaring hops with Lemma 4.1 checked; a draggable seed whose defect ladder, the paper's own update rule, collapses doubly exponentially while the gap bound log(1/3u_j)/beta_j settles. Press G: the toy turns critical-like (h = 0) and the seed region vanishes. Risks: the toy fails by degeneracy, not scale invariance; slide 5 is dense.

**Keys:** arrows or space as in the deck. H J K L move the active probe, square, point or seed; 1 and 2 pick a probe on slide 1; G toggles gapped (h = 0.1) and critical-like (h = 0); [ and ] step h through 0, 0.02, 0.05, 0.1, 0.2, 0.5; R resets the slide. Mouse drag on any handle is a bonus. `?still` renders every final state.

## The toy, exactly

Classical Ising ring, n sites, periodic, H = -J sum s_i s_{i+1} - h sum s_i with J = 1. Transfer matrix eigenvalues lambda_+- = e^beta cosh(beta h) +- sqrt(e^{2 beta} sinh^2(beta h) + e^{-2 beta}), both positive, Z_n = lambda_+^n + lambda_-^n for every n. Everything is computed in the log domain, so n up to 512 and beta up to 64 never overflow. Gibbs purity T is the sum of p^2 over all 2^n configurations; the bar chart shows the exact weights of the leading levels (all up, the n single flips, all down, the rest). Spatial purity S is the purity of the two-weight vector (lambda_+^n, lambda_-^n)/Z. The colour field evaluates the closed form at real n; probes snap to integer n. Verified against brute-force enumeration for n = 4, 5, 6 (T and log Z agree to 12 digits) and the two identities hold to 7e-16 relative over 2000 random points at six field strengths. Defects below 1e-12 are rounding and are displayed as "< 10^-12".

The toy's critical-like switch is h = 0: lambda_-/lambda_+ = tanh beta tends to 1, xi diverges, and the ground state is doubly degenerate so T <= 1/2 everywhere. That is a different failure mechanism from a gapless quantum chain (scale invariance, v beta >> n against n >> v beta); the slides say so explicitly.

## Slides and build steps

**1. `s-hg-lenses` (4 states)**
- 0: Heatmap coloured by T, physical probe at (16, 1) with exact Gibbs bars, T, max p >= T, and the gap readout. Say: "One Z, read as a thermal distribution."
- 1: Spatial lens card appears, heatmap recoloured by S, probe at (4, 2) with the two transfer weights and xi. Say: "The same Z, read as a transfer spectrum. Purity means the ring is longer than xi."
- 2: Heatmap shows min(T, S); the region where both exceed 7/8 lights up with both 7/8 contours. Say: "Both above 7/8 at one point is the seed. Purity above 1/2 already gives a unique ground state and e^{-beta gamma} <= u/(1-u)."
- 3: Toggle to h = 0: the region vanishes, T caps at 1/2. Say: "Critical-like: no seed anywhere. The toy fails by degeneracy; a gapless chain fails by scale invariance, see slide 4."

**2. `s-hg-square` (4 states)**
- 0: Square with lower-left corner (8, 1); four Z values in a mirrored 2x2 diagram. Say: "Four partition functions."
- 1: Edges labelled with the four purities as ratios of corner values.
- 2: The two paths around the square (up then right, right then up) highlighted; both products and Z_2n(2 beta)/Z_n(beta)^4 printed to 12 digits, computed separately. Say: "Every Z once upstairs, once downstairs."
- 3: Mirror identity for T(4n, beta) evaluated live; takeaway. Say: "Trivial algebra, new use: it trades the beta axis for the n axis."

**3. `s-hg-squaring` (4 states, animated)**
- 0: Point at (8, 2) with its Gibbs and transfer bars and defects.
- 1: Gibbs bars morph to their normalised squares, the point hops up to (8, 4); the new defect is checked against u^2/(2(1-u)^2). Say: "Squaring the Gibbs weights is doubling beta."
- 2: Transfer bars square, the point hops right to (16, 2); for two weights the lemma is an equality. Say: "Squaring the transfer weights is doubling n."
- 3: The diagonal stitch to (16, 4). Say: "The identities move each purity the other way; together, one diagonal step."

**4. `s-hg-bootstrap` (4 states, animated)**
- 0: Seed domino at (16, 2) and (32, 2) with the seed defects; heatmap coloured by min(S(n, beta), T(2n, beta)).
- 1: First hop; the ladder shows u_0 and u_1 from the paper's update (G(1/8) = 913952/117649), the toy's exact defects, and the gap bound.
- 2: Full staircase, eight ladder rows, gap bound settling near 1.14 (toy units) against the toy's true gap 4.2. Say: "log(1/u_j) and beta_j both grow like 2^j, so the quotient settles. One seed gives every size."
- 3: Toggle to h = 0: stalled, grey dotted attempt, the paper's gapless argument in the takeaway.

**5. `s-hg-proved` (5 states)**
- 0: The paper's own plane with the two seeds (60, 105/4) and (36, 49/4) and their staircases, no toy.
- 1 to 4: Theorem 1.1 with its constants, the seeds and the 6e-4 margin, the verification status (no Lean, exact-rational certificates, what the review re-ran, what is unverified, 85 to 90%), the caveats (even rings, liminf, constant a thousand times below 0.41, finite-size RG-flow criterion).

## Verification

Render script: a copy of the deck workflow (deck-spec section 5) run with Playwright at 1920x1080 against `option-b.html?still`, final state of every slide plus every build step without `still` (animations allowed to finish). Results in `renders/b/`: 5 final PNGs, 22 step PNGs, `report.json`. Off-stage check: 0 findings. Clipped check: 0 findings. Page errors and console errors: 0. Every PNG inspected by eye; overlaps fixed by moving contour labels to contour extremes and shortening slide 5 labels. File size 79 KB, no network requests, no external fonts, no em dashes.

Integration: copy everything between `<!-- BEGIN HALDANE SLIDES -->` and `<!-- END HALDANE SLIDES -->` into talk.html's `#stage`. CSS is scoped to the five ids. The script registers its controllers on DOMContentLoaded and self-starts if the deck opens on one of these slides.
