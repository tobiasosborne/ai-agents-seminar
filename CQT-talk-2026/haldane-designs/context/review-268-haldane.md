# Quick adversarial read: "The periodic spin-one Haldane gap" (family 268)

*One Opus reviewer, one pass, 7 Oct 2026. Read from the LaTeX; the paper's exact-rational scalar checkers and trial-state contractions were re-run; an independent exact diagonalisation for $n\le 9$ was done before numerics were stopped at Tobias's request. Anything not checked is marked unverified.*

## 1. Theorem and proof architecture

**Theorem 1.1.** For $H_L=\sum_j \mathbf S_j\cdot\mathbf S_{j+1}$, spin 1, periodic: for every even $L\ge 60$ the ground state is unique and $\gamma_L>\tfrac{4}{105}\log\tfrac{80}{79}\approx 4.8\times10^{-4}$; for every even $L\ge 2304$, $\gamma_L>\log 20/784\approx 3.8\times10^{-3}$. Hence $\liminf_L\gamma_L>0$.

The chain of implications:

1. **Prop 3.1, transfer operator.** Write $-h=\sum_\alpha G_\alpha\otimes G_\alpha$ with $G_\alpha$ real antisymmetric, $\|G_\alpha\|=1$. Expanding $e^{-bH}$ in time-ordered bond events gives $Z_n(b,g)=\operatorname{Tr}(X_b^{\,n}U_g)$, where $X_b$ is a real symmetric Hilbert–Schmidt kernel on bond histories. So $Z_n(b)=\sum_i\lambda_i(b)^n$ with one real list $\lambda_i(b)$ for all $n\ge4$.
2. **Lemma 3.2, sectors.** $D_2$ and cyclic symmetries split the spectrum into lists $I$, $O$ (twice) and $N$ (three times), each recoverable from $Z_n$, $Z_n(P)$, $Z_n(C)$.
3. **Two purities.** For even $n$: the spatial purity $S(n,b)=Z_{2n}(b)/Z_n(b)^2$ of the weights $|\lambda_i|^n/Z_n$, and the Gibbs purity $T(n,b)=Z_n(2b)/Z_n(b)^2$.
4. **Lemma 4.1, squaring.** A probability vector with purity defect $u$ has normalised square with defect at most $f(u)=u^2/\bigl(2(1-u)^2\bigr)$.
5. **Cancellation identities.**

$$
S(n,2b)=\frac{S(n,b)^2\,T(2n,b)}{T(n,b)^2},\qquad
T(4n,b)=\frac{T(2n,b)^2\,S(2n,2b)}{S(2n,b)^2}.
$$

   These carry bounds on $(S(n,b),T(2n,b))$ to bounds on $(S(2n,2b),T(4n,2b))$.
6. **Prop 4.3, doubling.** Defects obey $u_{j+1}\le C u_j^2$: doubly exponential decay while $b_j=2^j b_0$ grows only exponentially.
7. **Prop 4.3, interpolation.** Hölder on the spatial weights gives, for every even $L\in[n_j,2n_j]$,

$$
T(L,b_j)\ \ge\ \bigl[T(2n_j,b_j)\,S(n_j,b_j)^2\bigr]^{L/2n_j}.
$$

8. **Prop 4.3, conclusion.** Largest Gibbs weight $\ge 1-3u_j>\tfrac12$ gives uniqueness; $e^{-b_j\gamma_L}\le 3u_j/(1-3u_j)<r^{2^j}$ gives $\gamma_L>\log(1/r)/b_0$.
9. **Prop 5.4, seed at $L=60$.** From $Z_{6,8,10}(21/2,\{1,P,C\})$, polynomial filters on the spatial spectrum, capped-mass moment bounds, a $5/2$ raise of $b$, and the trial bound $Z_{120}>1$: $S(60,105/4)>7/8$ and $T(120,105/4)>7/8$.
10. **Prop 5.5, seed at $L=2304$.** From $Z_{4..12}(49/4,\{1,P\})$ and $Z_{72}>1$: defects $0.048$ and $0.18$ at $(36,49/4)$; six rounded updates bring both below $0.01$ at $(2304,784)$.
11. **§6.** Prop 4.3 on the two seeds gives the theorem.

## 2. Load-bearing steps

| Step | Assessment | Reason |
|---|---|---|
| (a) Thermal purity to $T=0$ gap | correct | Max weight $\ge$ purity $>\tfrac12$ excludes degeneracy; $w_1/w_0\le(1-w_0)/w_0$ gives the gap; the shift $aL$ cancels. Every inequality checked. |
| (b) Why $L$ and $\beta$ double together, no degradation | correct | Both cancellation identities re-derived by hand. $\log(1/u_j)\sim 2^j\log(1/r)$ grows exactly as fast as $b_j$. Interpolation (step 7) verified. $G(1/8)=913952/117649<7.9$, $r=79/80$ check by hand and by the exact-fraction script. |
| (c) Why it fails for gapless chains | correct; the seed is what fails | Nothing in step 1 uses spin 1; spin-1/2 and bilinear–biquadratic chains also give symmetric real kernels. For a $z=1$ critical chain $S$ and $T$ are scale-invariant functions of $vb/n$: $T\to1$ needs $vb\gg n$, $S\to1$ needs $n\gg\xi(b)\sim vb$. Best compromise $vb\approx\sqrt2\,n$ gives defects $\approx 0.3$ to $0.5$, far above the required $u_0\le1/8$. For the Haldane chain at $(60,26.25)$ physics predicts $\sim10^{-4}$, so the certified $1/8$ is loose. A rigorous finite-size RG-flow criterion, not Knabe-type, no frustration-freeness needed. |
| (d) Signs and positivity | correct, avoided rather than handled | No sublattice rotation. Kernel real symmetric but not positive. Self-adjointness makes $\lambda_i$ real, so even-$n$ weights $|\lambda_i|^n\ge0$. Odd $n$ appears only as signed moments inside the polynomial filter (Lemma 5.3), handled correctly. Odd $L$ never claimed. Twisted kernel identity, $U_g$ representation, sector inversion, $O/N$ multiplicities all checked. |
| (e) What the certificates certify | exact arithmetic, one tight margin | Thermal tables: exact integer Horner evaluation of a conditioned-Poisson polynomial with floors, proven error $\le 281(\sqrt{3^n}+1)$, rigorous enclosure of $e^{x_n}$, rational comparisons; int64 with a no-overflow induction, or Python big integers. Trial bounds: exact big-integer contraction of a $D=26$ SU(2) MPS. Scalars: `Fraction`s. |

**What was actually re-run.** Both scalar scripts pass every assertion; tightest margins $4.7\times10^{-5}$ in $(q-1)^5<R_q^2$ and $6\times10^{-4}$ in $S(60)>7/8$. Both trial contractions pass with energy per site $\approx-1.4014821$, above $e_\infty=-1.40148404$ as required. Independent contraction of $\psi_N$ for $N=4,6,8$ matches the paper's $U_N/V_N$ formula to $10^{-13}$. Independent exact diagonalisation reproduces every tabulated centre for $n=6,8$ at $b=21/2$ (three twists) and $n=4..9$ at $b=49/4$ to $\pm10^{-6}$. Hankel matrices of $Z,J,N$ at $b=49/4$ (orders 4 to 12) positive definite, smallest eigenvalue $\approx 9\times10^{-3}$, consistent with a genuine moment sequence.

**Unverified.** $Z_{10}(21/2,\{1,P,C\})$, which the $L\ge60$ theorem needs (run stopped); $n=10,11,12$ at $b=49/4$; the symmetry and orbit-multiplicity reduction proofs in detail.

## 3. Errors, gaps and rough spots

No mathematical error found. Everything else is presentational:

- **Overloaded symbols.** $b_0$ is $21/2$ inside Prop 5.4 but $105/4$ in Prop 4.3 and §6. $U$ is $100245/10^5$ (Prop 5.4), $100139/10^5$ (Cor 5.6), the unitaries $U_g$, and the contraction $U_N$. $D$ is the mass bound 1.45, the bond dimension 26, and the matrix $32R$. $C$ is the cyclic rotation and the bootstrap constant. $T$ is the Gibbs purity, the MPS transfer matrix and the triad operator. $J$ is a sector moment and the Poisson cutoff $256/280$. $E,P,Q,R$ are also reused.
- **Names point the wrong way.** `thermal120` proves the $b=21/2$ table and `thermal72` the $b=49/4$ one; `verification/source1` is the $L=2304$ seed and `source2` the $L=60$ seed.
- **External reference.** Cor 5.6 points to the boundary-field companion and is not needed for the main theorem.
- **Thin justifications.** Appendix A asserts in one sentence that reversal and negation give antiunitary symmetries of the twisted $C$-chain with equal column norms on each orbit (Appendix B argues the real-twist case more carefully). Prop 3.1's regrouping into bond histories is standard Aizenman–Nachtergaele but compressed.
- **Thin margins.** The $5/2$-power steps rest entirely on exact rational evaluation, which the script does.
- **Headline overstates slightly.** "Resolves the Haldane conjecture" versus what is proved: the even-periodic finite-volume $\liminf$ statement. Cor 6.1 gives a gap inequality for subsequential limits of periodic ground states, not uniqueness or a gap for all infinite-volume ground states. The paper says this in the body.
- **Unneeded generality.** Lemma 2.1 handles non-self-adjoint realisations, irrelevant here.

## 4. Verdict

1. Probability the theorem is proved as written: **85 to 90%**, conditional on the $n=10$ to $12$ integer totals being correct.
2. The analytic chain (steps 1 to 8) is short and elementary; checked line by line. The ideas that carry it are the symmetric bond-history transfer kernel and the two cancellation identities.
3. The roughness is presentational (recycled symbols, mislabelled appendices and directories), not substantive.
4. The criterion is non-vacuous: critical $z=1$ chains sit at a scale-invariant point with defects around $0.3$ to $0.5$ and cannot satisfy the seeds.
5. Quickest way to close the gap: an independent recomputation of $Z_{10}(21/2,\{1,P,C\})$, then the $n=11,12$ totals at $49/4$.
