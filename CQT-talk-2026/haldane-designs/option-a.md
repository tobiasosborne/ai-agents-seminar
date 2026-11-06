# Option A: The Doubling Machine

**Pitch (about 150 words).** A dark instrument panel. The proof is a machine with one input, the partition function Z_n(β), two gauges, the Gibbs purity T and the spatial purity S, and one moving part, a glowing 2×2 square on the (n, β) board. Everything is computed live in the page: a classical Ising ring where Z_n = λ₊ⁿ + λ₋ⁿ is exact for any (n, β), and spin-1/2 and spin-1 Heisenberg rings (4 to 8 sites, up to 729 states) diagonalised at load with a Jacobi eigensolver. Slide 1 shows the two readings side by side. Slide 2 slides the square and lets the four Z's cancel as tokens, the identity checked to twelve digits on both toys. Slide 3 squares a draggable probability vector, then shows the two squarings moving along different axes. Slide 4 turns the crank: defects collapse doubly exponentially while β doubles, the gap bound flattens, and a gapless seed stalls it. Slide 5 is the fine print. Every number is live or from the explainer and the review.

**Keys.** Arrows and Space as in the deck. Tab selects a knob (glowing border), `[` `]` adjust it, `{` `}` coarse. Slide 4: `P` paper seed (u₀ = 1/8, C = 7.9), `E` the explainer's toy (0.1, 5), `G` a gapless seed (0.4). Mouse is a bonus: knobs are range inputs, the bars on slide 3 are draggable. `?still` renders every slide at its final state.

**Live computations (not canned).** (1) Ising ring, J = 1, h = 0: log Z, S, T from λ± = 2cosh β, 2sinh β in closed form, stable to n = 256 and β = 8; energy levels E = −(n − 2k) with degeneracy 2·C(n, k) for the Gibbs bars. (2) Heisenberg rings H = Σ S_i·S_{i+1}, periodic: s = 1/2 with n = 4, 6, 8 and s = 1 with n = 4, 6, built sector by sector in total S^z and diagonalised with cyclic Jacobi (about 0.2 s at load). Checks run in Node before shipping: Z_n against brute-force sums, E₀ = −2 (n = 4), −2.80278 (n = 6), −3.65109 (n = 8) for spin 1/2, E₀ = −6 for spin-1 n = 4, Tr H = 0, the square identity to 1e−12 on both toys. (3) The squaring toy and the bootstrap recurrence are evaluated from the knobs on every change.

## Slides and build steps

### 1. `s-hg-readings`: "One Z, two readings" (3 steps)
Left: Ising ring, knobs n (even, 4 to 64) and β (0.05 to 8, shared). Right: a quantum ring chosen with the ring knob. Readouts: Z_n(β), λ±, E₀, the true gap, gauges for T and S with ticks at 1/2 and 7/8.
- **0:** *Say:* "One number, read two ways. Left a toy where both readings are exact, right a quantum ring diagonalised in this page."
- **1:** Physical reading: Gibbs formula chips and the T gauge label. *Say:* "T is the purity of the Gibbs weights. Large β drives it to 1." Note the honest footnote on the Ising gauge: the ring has two ground states, so its T saturates at 1/2. That is the purity test seeing degeneracy.
- **2:** Spatial reading: Z_n = Σ λᵢⁿ, the S gauge. *Say:* "S is the purity of the transfer spectrum. Large n drives it to 1. The paper's kernel is real symmetric, so even powers are weights." For the s = 1/2, n = 4 ring the S gauge is real too: Z₈/Z₄², both exact here.
- **3:** The gap line appears. *Say:* "max p ≥ purity, so T > 1/2 gives uniqueness and e^(−βγ) ≤ u/(1−u)." Then Tab to β and hold `]`: the bound log((1−u)/u)/β rises toward the true gap E₁ − E₀.

### 2. `s-hg-square`: "The square and the cancellation" (3 steps)
Knobs n (4 to 64) and β (1/8 to 4) slide the square; the four corner readouts show Z and the purities on the edges.
- **0:** *Say:* "Four Z's at the corners. Each purity is a ratio of two of them."
- **1:** Both products appear as token fractions, Z's upstairs and downstairs, coloured by corner.
- **2:** Tokens pair off and vanish (1.4 s animation; instant under `?still`). *Say:* "Every Z once upstairs, once downstairs. Both sides are Z₂ₙ(2β)/Zₙ(β)⁴. Trivial, and not previously exploited."
- **3:** Numeric check: LHS and RHS to 12 significant digits on the Ising toy and on the spin-1/2 ring at n = 4 (from Z₄ and Z₈), plus the second identity one square up. Slide the square: the digits keep agreeing.

### 3. `s-hg-squaring`: "Squaring moves each purity along its own axis" (4 steps)
Left: a four-entry vector, default (0.90, 0.05, 0.05, 0), the explainer's example. Right: the board with knobs n (Ising) and β.
- **0:** *Say:* "Purity is near 1 exactly when one entry dominates. Defect u = 1 − Σp²." Here 0.185.
- **1:** The normalised square animates in: defect 0.0122, Lemma 4.1 bound 0.0258, roughly u²/2.
- **2:** Amber hop along β, with numbers from the spin-1 four-site ring (the paper's own model, 81 states): T(4, β) → T(4, 2β), defect against f(u).
- **3:** Cyan hop along n, Ising ring: S(n, β) → S(2n, β). For two eigenvalues the lemma is exactly tight, which the digits show.
- **4:** Violet diagonal: the two identities trade the axes. *Say:* "Neither squaring alone reaches (2n, 2β)."

### 4. `s-hg-bootstrap`: "The bootstrap: defects collapse, β only doubles" (4 steps)
Ladder from the paper's seed (n₀, β₀) = (60, 105/4), knobs u₀ and C, rows j = 0 to 7 with nⱼ, βⱼ, uⱼ on a log bar and the bound log(1/3uⱼ)/βⱼ.
- **0:** Seed row only. Default is the explainer's toy, u₀ = 0.1, C = 5.
- **1:** One turn: along β defect 3u then (3u)²/2, along n defect 2u then 2u²; together C u². The paper has C < 7.9 for u ≤ 1/8.
- **2:** All rows: 0.1, 0.05, 0.0125, 7.8e−4, 3.1e−6, 4.7e−11, the explainer's sequence, while β runs 26.25, 52.5, 105, ...
- **3:** The convergence chart with the dashed limit log(1/r)/β₀, r = C·u₀. Press `P`: r = 79/80 and the limit reads 4.79e−4, the theorem's constant for L ≥ 60.
- **4:** The gapless panel: u₀ = 0.4 gives C·u₀ > 1 and the first update is already vacuous. *Say:* "T needs vβ ≫ n, S needs n ≫ vβ. A critical chain cannot have both."

### 5. `s-hg-proved`: "What is actually proved" (4 steps)
Theorem 1.1 verbatim from the review, then rows with status lamps: scope (even rings, liminf, not infinite volume), thin seeds and constants (6e−4 margin, 4.7e−5, 4.8e−4 against 0.41), where the work is (seeds from Z_{6,8,10}(21/2) and Z_{4..12}(49/4), D = 26 MPS), verification (no Lean; exact-rational certificates; re-run items green; Z₁₀(21/2), n = 10 to 12 at 49/4 and the symmetry reductions amber), and the reviewer's 85 to 90%.

## Risks and honest notes
- **Aesthetic risk.** Dark panel, monospace readouts: distinct from the other options, but on a bright projector the muted grey captions (1.75cqh) may wash out. Everything the audience must read is 2cqh or larger and amber, cyan or white.
- **The Ising toy's T never exceeds 1/2** because its ground state is doubly degenerate. The slide says so; it is a feature of the purity test, not a bug, but the speaker should expect the question.
- **Mixed toys on slide 3.** The Gibbs hop uses the spin-1 four-site ring and the spatial hop the Ising ring, at the same β. Both are labelled. No single small toy has both purities near 1 at one (n, β) unless n ≫ ξ(β) and β ≫ 1/gap together, which is exactly the seed condition of slide 4.
- **"12 digits agree"** is a double-precision check of the algebra, not exact arithmetic; the paper's certificates are exact rationals, and slide 5 says so.
- **One number in the explainer does not match its own formula.** In the toy run at j = 5 the explainer quotes γ ≥ 23.8/(32β₀); 23.8 is log(1/u₅), while log(1/3u₅) is 22.7. The slide computes log(1/3uⱼ)/βⱼ as the prompt asks, so it shows 2.70e−2 at j = 5 (that is 22.7/840), not 23.8/840.
- **Quantum rings are spin 1/2 or tiny spin 1, not the paper's L ≥ 60 chain.** Labelled "toy" on every panel.
- **Jacobi at load** costs about 0.2 s on a laptop (729-state spin-1 ring included); nothing is lazy, so the first slide is ready when it appears.

## Verification
- Render script: a copy of `design/render.mjs` (final state of every slide at 1920×1080 under `?still`, off-stage and clipped checks) and of `design/render-steps.mjs` (every build step, page and console errors), run with Playwright 1.5x and the bundled Chromium.
- Result: 5 slides, **0 off-stage, 0 clipped, 0 page errors, 0 console errors or warnings**, at final state and at every one of the 23 build steps. Keyboard driven end to end under Playwright (Tab, `[` `]` `{` `}`, P, E, G, arrows and back).
- Renders in `renders/a/`: `01-s-hg-readings.png` ... `05-s-hg-proved.png` (final states) and `<id>-stepK.png` for every step. Each PNG was looked at; the fixes made along the way were header overflow, an uppercase transform that turned β into B, a hidden step-0 caption, label collisions on the slide-3 board, and a hang when uⱼ underflowed to 0 in the convergence chart.
- File: `option-a.html`, 80 KB, single file, no network requests, system fonts, no em dashes, CSS scoped to the five `s-hg-*` ids, engine copy with `slides`, `goTo`, `applySteps`, `maxStepsFor`, `state` as globals.
