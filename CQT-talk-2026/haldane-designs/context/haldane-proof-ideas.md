# The Haldane-gap proof in family 268: the main ideas

*An explanation, not a verification. Where I say "known" or "new" I am giving my own judgement.*

## 1. One partition function, two readings

Everything runs on the ring partition function $Z_n(\beta)=\operatorname{Tr}e^{-\beta H_n}$, where $H_n$ is the spin-1 Heisenberg chain on $n$ sites with periodic boundary conditions. The point of the paper is that $Z_n(\beta)$ can be read in two ways.

The **physical reading** is the usual one: $Z_n(\beta)=\sum_k e^{-\beta E_k}$ over the energy levels of the $n$-site chain, so the Gibbs weights $p_k=e^{-\beta E_k}/Z_n(\beta)$ form a probability distribution over eigenstates. Large $\beta$ concentrates it on the ground state.

The **spatial reading** treats the ring as a one-dimensional classical system with a transfer matrix acting across a bond, so that $Z_n(\beta)=\operatorname{Tr}X_\beta^{\,n}=\sum_i\lambda_i(\beta)^n$. The familiar example is the classical Ising ring, $Z_n=\lambda_+^n+\lambda_-^n$. For a quantum chain the role of a classical spin configuration is played by a continuous-time history of bond events (the Aizenman–Nachtergaele expansion of 1994, which is standard), and the transfer "matrix" is an integral operator on bond histories. The paper's construction makes this kernel real and symmetric, so all $\lambda_i(\beta)$ are real, and every even power $|\lambda_i|^n$ is non-negative. That gives a second probability distribution, $q_i=|\lambda_i|^n/\sum_j|\lambda_j|^n$, over the spatial spectrum. Large $n$ concentrates it on the top eigenvalue, the way $\lambda_+^n$ dominates $\lambda_-^n$ in the Ising ring once $n$ exceeds the correlation length.

## 2. Purity as the one number to track

For any probability vector the purity $\sum_k p_k^2$ lies in $(0,1]$ and is close to 1 exactly when one entry dominates. For instance $(0.9,0.1)$ has purity $0.82$ and $(0.99,0.01)$ has purity $0.98$. The useful elementary fact is $\max_k p_k\ge\sum_k p_k^2$, so purity $\ge1-u$ forces a single entry of weight at least $1-u$.

Both distributions above have purities that are ratios of partition functions:

$$
T(n,\beta)=\sum_k p_k^2=\frac{Z_n(2\beta)}{Z_n(\beta)^2},\qquad
S(n,\beta)=\sum_i q_i^2=\frac{Z_{2n}(\beta)}{Z_n(\beta)^2}.
$$

$T$ is the Gibbs purity ("is the $n$-site chain thermally in its ground state at inverse temperature $\beta$?"), $S$ is the spatial purity ("is the ring longer than the correlation length at this $\beta$?"). Notice how little you need to turn $T$ into a gap. If $T(L,\beta)\ge1-u$ with $u<1/2$ then the ground state is unique, because two degenerate levels would each carry weight at most $1/2$. And the first excited level has $p_1/p_0=e^{-\beta\gamma_L}\le(1-p_0)/p_0\le u/(1-u)$. For example, $T(L,784)\ge0.99$ would give $\gamma_L\ge\log 99/784\approx0.006$. The paper's actual constant $\log20/784$ comes from a slightly cruder version of this inequality. So the whole problem becomes: show $T(L,\beta)$ is near 1 with $\beta$ growing no faster than $\log(1/u)$.

## 3. The cancellation

This is the part you asked about. Take the four partition functions at the corners of a $2\times2$ square in the $(n,\beta)$ plane: $(n,\beta)$, $(2n,\beta)$, $(n,2\beta)$, $(2n,2\beta)$. Each purity is a ratio of two of them, and the ratios compose:

$$
S(n,2\beta)\,T(n,\beta)^2=\frac{Z_{2n}(2\beta)}{Z_n(2\beta)^2}\cdot\frac{Z_n(2\beta)^2}{Z_n(\beta)^4}=\frac{Z_{2n}(2\beta)}{Z_n(\beta)^4}=S(n,\beta)^2\,T(2n,\beta).
$$

So $S(n,2\beta)=S(n,\beta)^2T(2n,\beta)/T(n,\beta)^2$, and by the same bookkeeping $T(4n,\beta)=T(2n,\beta)^2S(2n,2\beta)/S(2n,\beta)^2$. As algebra this is trivial: every $Z$ appears once upstairs and once downstairs. I am not aware of these identities being used before, and I would not call the identity itself the discovery. What is new is noticing that it lets you trade movement along the $\beta$ axis for movement along the $n$ axis, which is the next paragraph.

## 4. Squaring moves you in both directions

If you square a probability vector and renormalise, the dominant entry becomes more dominant, and quadratically so: a defect $u$ becomes a defect of about $u^2/2$ (the paper's Lemma 4.1 gives $u^2/(2(1-u)^2)$). Example: $(0.90,0.05,0.05)$ has defect $0.185$; its normalised square $(0.994,0.003,0.003)$ has defect $0.012$.

Now look at what squaring does to the two distributions. Squaring the Gibbs weights at $(n,\beta)$ gives the Gibbs weights at $(n,2\beta)$, because $e^{-2\beta E_k}$ is the square of $e^{-\beta E_k}$. Squaring the spatial weights at $(n,\beta)$ gives the spatial weights at $(2n,\beta)$, because $|\lambda_i|^{2n}$ is the square of $|\lambda_i|^n$. So squaring moves $T$ along $\beta$ and moves $S$ along $n$. The cancellation identities are the bridge between the two axes: they let a bound on $T$ at larger $n$ be paid for with bounds on $S$, and vice versa.

## 5. The bootstrap, with numbers

Suppose at some $(n,\beta)$ both defects are at most $u$: $S(n,\beta)\ge1-u$ and $T(2n,\beta)\ge1-u$. Then:

- From the first identity, dropping $T(n,\beta)^2\le1$ in the denominator, $S(n,2\beta)\ge(1-u)^3$: defect about $3u$. Square it: $S(2n,2\beta)$ has defect about $(3u)^2/2$.
- From the second identity, dropping $S(2n,\beta)^2\le1$, $T(4n,\beta)\ge T(2n,\beta)^2S(2n,2\beta)$: defect about $2u$. Square it: $T(4n,2\beta)$ has defect about $2u^2$.

So the pair $(S,T)$ at $(2n,2\beta)$ has defect at most $Cu^2$ for an explicit $C$ (the paper has $C<7.9$ when $u\le1/8$). Iterating, the defects go $u,\ Cu^2,\ C^3u^4,\ C^7u^8,\dots$: doubly exponential decay in the number of doublings $j$, while $\beta_j=2^j\beta_0$ and $n_j=2^jn_0$ grow only exponentially. A toy run with $u_0=0.1$ and $C=5$: $0.1,\ 0.05,\ 0.0125,\ 7.8\times10^{-4},\ 3.1\times10^{-6},\ 4.7\times10^{-11}$.

Feed that into the gap inequality of section 2: $e^{-\beta_j\gamma}\le 3u_j$ gives $\gamma\ge\log(1/3u_j)/\beta_j$, and since $\log(1/u_j)$ grows like $2^j$ and $\beta_j$ grows like $2^j$, the ratio stays bounded below by a fixed positive number. In the toy run at $j=5$: $\gamma\ge 23.8/(32\beta_0)\approx0.74/\beta_0$, and the next doubling gives essentially the same number. That is the entire mechanism by which data at one small $(n,\beta)$ implies a gap at all larger ring sizes $n_j=2^jn_0$. The even sizes in between are filled in by a Hölder inequality on the spatial weights, which costs only a power.

## 6. Why it is not a free lunch

The seed condition asks for both purities to be near 1 at the same $(n,\beta)$. $T(n,\beta)\approx1$ needs $\beta$ much larger than the inverse finite-size gap of the $n$-site chain, and $S(n,\beta)\approx1$ needs $n$ much larger than the correlation length $\xi(\beta)$. For a gapless chain with velocity $v$ the finite-size gap is about $v/n$ and the correlation length about $v\beta$, so the two demands read $v\beta\gg n$ and $n\gg v\beta$, which cannot both hold; the best compromise leaves defects around $0.3$ to $0.5$, well above the $1/8$ the bootstrap needs. For a gapped chain, $\xi$ and $1/\Delta$ are both finite and the two conditions decouple. So the criterion says: if a finite ring already looks gapped on both axes with a margin of $1/8$, then it looks gapped at every larger scale. It is a rigorous version of the renormalisation-group statement that a scale-invariant system has purities stuck at a fixed point while a gapped one flows to purity 1. Nothing in it uses spin 1, frustration-freeness, or a Knabe-type local gap; it needs only the real symmetric transfer kernel and the seed.

## 7. The seeds, which is where the work is

The bootstrap starts at $(n,\beta)=(60,105/4)$, and nobody can compute $Z_{60}$ or $Z_{120}$ at $\beta\approx26$ directly. What can be computed exactly is $Z_n(\beta)$ for $n\le10$ at $\beta=21/2$ (59,049 states, done in exact integer arithmetic with a rigorous truncation bound on the exponential series). The seed argument then has to squeeze bounds on $S(60,105/4)$ and $T(120,105/4)$ out of that. Three ingredients do it. First, low moments control high moments of a real spectrum: for example the number of eigenvalues with $|\lambda_i|\ge c$ is at most $Z_{10}/c^{10}$, and the symmetry sectors (an $A_4$ acting on the three spin components, giving multiplicities 1, 2 and 3) sharpen this into polynomial-filter inequalities. Second, a variational matrix-product state of bond dimension 26, contracted exactly, lower-bounds the top eigenvalue through $Z_{120}>1$ after an energy shift. Third, a "$5/2$-power" cousin of the squaring lemma moves the Gibbs distribution from $\beta=21/2$ to $\beta=105/4$. The certified margins at the end are thin, $S(60,105/4)>7/8$ by only $6\times10^{-4}$, which is why the resulting gap constant, $4.8\times10^{-4}$, is a thousand times smaller than the true gap of about $0.41$. A second seed at $L=2304$ from exact $Z_n$ with $n\le12$ at $\beta=49/4$ gives the better constant $\log20/784$. If there is a mistake anywhere, it is far more likely in this section than in sections 3 to 5.

## 8. What is old, what is new, in one place

Old: the bond-event expansion and the quantum-to-classical mapping (Aizenman–Nachtergaele), purity as a concentration proxy, the fact that squaring sharpens a distribution. Trivial but, as far as I know, not previously exploited: the two cancellation identities on a $2\times2$ square of $(n,\beta)$. New: the observation that squaring moves the two purities along different axes, so the identities turn a seed at one $(n,\beta)$ into doubly exponential concentration at $(2^jn,2^j\beta)$, which is exactly the rate needed to survive the $1/\beta_j$ in the gap bound. Technical heart: the finite-moment extrapolation that certifies the seed. The price for generality is that the constants are tiny, and the theorem is a statement about even periodic rings and the $\liminf$ of their gaps, not about every infinite-volume ground state.
