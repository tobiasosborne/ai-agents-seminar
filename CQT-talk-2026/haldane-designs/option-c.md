# Option C: "Worldlines"

**Pitch (about 150 words).** A blackboard. Chalk strokes wobble through an SVG displacement filter, the labels are chalk-white, yellow, pink and blue, and the proof is told as five pictures. Slide 1 draws the ring in imaginary time, six worldlines with bond events arriving as a Poisson process, then rotates the board so the transfer operator reads across bonds instead of along time: the same number, read two ways. Slide 2 is the purity spotlight: a chalk histogram of Gibbs weights that narrows as β rises, a dial for the purity, and the moment the ground state gets circled as unique. Slide 3 is the 2x2 square with the cancellation drawn as two routes to the same corner. Slide 4 is the flow: diagonal doubling hops with the defects written beside each, converging to the theorem's own constant, and a hatched critical patch where the hops stall. Slide 5 is the fine print. Four of the five slides compute live. Risks: the chalk filters cost GPU on weak laptops; the toys are spin-½, not spin 1.

**Keys.** Arrows or space as in the deck. Bonus keys per slide: `[` `]` change β on slides 1 to 3 and u₀ on slide 4; `M` cycles the Trotter slices on slide 1; `-` `=` change n on slide 2 and C on slide 4. `?` lists them. `?still` and print render every slide at its final state.

## Live computations (all in vanilla JS, at page load, about 0.1 s)

- Spin-½ Heisenberg rings of 4, 6 and 8 sites, diagonalised exactly with a cyclic Jacobi solver blocked by total Sz (largest block 70). Checked against known values: E₀(6) = −2.802776, E₀(8) = −3.651093, gap(8) = 0.5227.
- The 6-site ring as a Trotter lattice (checkerboard, 2M slices, τ = β/M): Z contracted along time, Tr[(T_A T_B)^M] on 64 states, and along space, Tr[(X_e X_o)^{n/2}] on 2^{2M} column states. The two agree to 15 digits; as M grows they approach the exact Gibbs sum.
- A classical three-state ring (J = 1, D = 1/2), exact 3x3 transfer matrix, for the spatial weights q_i ∝ |λ_i|^n and S.
- The doubling ladder u_{j+1} = C u_j² with the paper's seed values u₀ = 1/8, C = 7.9 at (60, 105/4): the bound log(1/3u_j)/β_j converges to log(1/(C u₀))/β₀ = (4/105) log(80/79) = 4.79·10⁻⁴, the theorem's constant for L ≥ 60.

## Slides and build steps (speaker drives with the right arrow)

**1. s-hg-worldlines "One partition function, two readings"** (3 steps, two live readings)
- Enter: six chalk worldlines on the unrolled cylinder, height β = 2. Bond events tick in over 2.6 s as a seeded Poisson process at rate 1 per bond per unit β. *Say:* "Z = Tr e^{−βH}. Expand the exponential: a history of bond events on this cylinder."
- Step 1: eight dashed slices appear (the toy lattice) and a scanner sweeps upward. Read along time: the Gibbs sum over 64 levels, 657.156 for the uncut ring, and the lattice value 681.135416929577. *Say:* "Read it along time: a transfer matrix on rows of six spins. That is the Gibbs reading."
- Step 2: the board rotates 90 degrees and the scanner sweeps across bonds. Read along space: the column transfer matrix on 256 states gives 681.135416929576. *Say:* "Now read it across bonds. Same number to fifteen digits. The paper does this in continuous time, with a real symmetric kernel, so the spectrum is one real list for every n."
- Step 3: the takeaway. Two probability vectors: p_k ∝ e^{−βE_k} and q_i ∝ |λ_i|^n.

**2. s-hg-spotlight "Purity as a spotlight"** (4 steps, two live toys)
- Enter: β = 0.5 on the 8-site ring. The beam covers the whole row, purity 0.0059. *Say:* "One number to track: Σ p_k². The spotlight width is its inverse."
- Step 1: β animates to 2. Purity 0.105, largest weight 0.267. *Say:* "Turning β up narrows the beam."
- Step 2: β animates to 8. Purity 0.9132 > 7/8. The ground-state bar is circled "unique", and p₁/p₀ = e^{−βγ} ≤ u/(1−u) gives γ ≥ 0.294 against the true gap 0.523. *Say:* "max p ≥ purity. Above one half the ground state is unique, and the first excited level is exponentially suppressed. The bound is loose, as the paper's constants are."
- Step 3: on the right, n animates from 4 to 64 for the classical three-state ring: the spatial weights narrow to the top eigenvalue, S from 0.54 to 0.9999. *Say:* "The same along n, once the ring is longer than the correlation length."
- Step 4: the takeaway and the whole problem: show T(L, β) near 1 with β growing no faster than log(1/u).

**3. s-hg-square "The square on the blackboard"** (4 steps, live identity)
- Enter: the four corners with Z₄(3), Z₈(3), Z₄(6), Z₈(6) from exact diagonalisation.
- Step 1: the four purities on the edges, T(4,3), T(8,3), S(4,3), S(4,6), with values.
- Step 2: two chalk dots travel the two routes to (2n, 2β); the cancelling Z's are struck through; both products print as 0.07563170461608. *Say:* "Every Z once upstairs and once downstairs. Trivial algebra, not used before as far as the explainer knows."
- Step 3: green arrows for the two squarings; live Lemma 4.1 numbers: Gibbs defect 0.2607 at (4,3) becomes 0.0148 at (4,6), bound 0.0621; spatial defect 0.3482 at (8,2) becomes 0.1427 at (16,2), bound 0.1427. *Say:* "Squaring moves T along β and S along n. The identity trades the axes."
- Step 4: the takeaway.

**4. s-hg-flow "The flow"** (3 steps, live ladder)
- Enter: the (n, β) plane in log scale, the seed circled at (60, 105/4) with the paper's "S, T > 7/8".
- Step 1: fourteen diagonal hops animate (0.38 s each) with u_j beside the first nine; the ledger fills to j = 10 and the ∞ row; the plot of log(1/3u_j)/β_j flattens onto the dashed line (4/105) log(80/79) = 4.79·10⁻⁴. *Say:* "Defects go u, Cu², C³u⁴. β only doubles. With the paper's seed numbers the bound lands on the theorem's constant. Notice it takes eight doublings to get going: the margin is thin."
- Step 2: the hatched critical patch: u₀ ≈ 0.4, C u₀² = 1.26 > u₀, the hop is crossed out, and the two demands vβ ≫ n and n ≫ vβ point away from each other. *Say:* "For a gapless chain both purities are functions of vβ/n. You cannot have both near 1. For a gapped chain the two demands decouple."
- Step 3: the takeaway, with the Hölder interpolation for the even sizes in between.

**5. s-hg-fineprint "The fine print"** (5 steps, the paper's numbers only)
- Theorem 1.1 verbatim with both constants; scope (even periodic rings, liminf, not the infinite-volume statement, true gap about 0.41); the seeds (n ≤ 10 at β = 21/2, MPS with D = 26, 5/2-power raise, margin 6·10⁻⁴; second seed (36, 49/4) with defects 0.048 and 0.18); verification (no Lean, exact-rational scripts re-run, Z₁₀(21/2) and n = 10 to 12 at 49/4 unverified); the reviewer's 85 to 90 percent verdict.

## Fidelity notes

- The Poisson ticks on slide 1 are an illustration of the expansion e^{−βH} = e^{−βn/4} e^{βΣQ_b} (rate 1 per bond per unit β is exact for H = Σ S·S with spin ½); their weights are not sampled, and the slide says so. The numbers next to them are real contractions.
- The lattice space transfer X_e X_o is not symmetric (the checkerboard breaks it); the paper's continuous-time kernel is. The slide shows the lattice trace, labels the continuum kernel as the paper's, and does not claim real eigenvalues for the toy.
- The ladder u_{j+1} = C u_j² is the explainer's simplified recursion. The paper's Prop 4.3 bookkeeping differs at finite j, but the j → ∞ limit log(1/(C u₀))/β₀ with u₀ = 1/8, C = 7.9 = 79/10 is exactly (4/105) log(80/79). The explainer's toy run (u₀ = 0.1, C = 5) reproduces when you set those keys. The explainer's "23.8/(32β₀)" at j = 5 is log(1/u₅); the slide uses log(1/3u₅) = 22.7, consistent with the bound it states.
- The critical patch on slide 4 is a sketch; the defects 0.3 to 0.5 are the review's estimate.
- Every number on slide 5 is the paper's as quoted in the review; nothing there is computed.

## Verification

- `render.mjs` (a copy of the deck's render workflow: 1920x1080, `?still`, final build state, off-stage and clipped checks) reports **ok** for all five slides, 0 issues, and **0 console or page errors**. Report in `renders/c/report.json`.
- Step renders (`<id>-stepK.png`, every step 0..max) also run with 0 errors. All 29 PNGs were inspected by eye; overlaps found in the first pass (slice label upside down after the rotation, corner labels crossing arrows, the critical patch on the staircase, a gap-bound line running off the right edge) were fixed and re-rendered.
- PNGs are palette-quantised (256 colours, no dither) to keep the folder small; the slide file itself is 76 KB, no network requests, no em dashes, system fonts only.
