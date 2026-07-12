# Live-demo prompts: Würzburg colloquium

Pre-written prompts for the live Claude Code demo. Paste one into a fresh
Claude Code session in an empty scratch directory. Each is offline-safe (no
network, no API keys) and completable in ~3–5 minutes by a coding agent.

**No API keys appear in this file.** The agent should already be authenticated.

---

## PRIMARY: Damped, driven pendulum phase portrait

> In a fresh directory, write a self-contained Python script `pendulum.py`
> that integrates the damped, driven pendulum
> `θ'' + b·θ' + sin(θ) = A·cos(ω·t)` with `b = 0.5`, `A = 1.2`, `ω = 2/3`
> using scipy's `solve_ivp`. Produce two figures with matplotlib and save
> them as PNGs: (1) `phase.png`, the phase portrait `(θ mod 2π, θ')` for a
> single long trajectory after discarding transients; (2) `poincare.png`, a
> Poincaré section sampled once per drive period. Use only numpy, scipy and
> matplotlib. Run the script, confirm both PNGs are written, and briefly
> describe what the strange attractor looks like.

Why it works live: classic chaotic system, visually striking, exercises the
full loop (write → run → read output → describe). Fails gracefully if scipy is
missing (fallback: hand-rolled RK4).

---

## BACKUP A: Self-generated CSV data analysis

> Create `analysis.py` that (1) generates a synthetic dataset of 500
> "measurements" of a decaying exponential `y = A·exp(-t/τ) + noise` with
> `A = 5`, `τ = 2.0`, Gaussian noise σ = 0.2, over `t ∈ [0, 10]`, and writes
> it to `data.csv`; (2) reads `data.csv` back, fits `A` and `τ` with
> `scipy.optimize.curve_fit`, and prints the recovered parameters with their
> standard errors; (3) saves `fit.png` overlaying the data and the best-fit
> curve. Run it and report whether the fit recovered the true parameters
> within uncertainty.

Why it works live: demonstrates the filesystem-as-ground-truth point directly
- the agent writes a file, then re-reads it rather than trusting memory. Pure
numpy/scipy/matplotlib, fully offline.

---

## BACKUP B: Ising model Monte Carlo

> Write `ising.py`: a Metropolis Monte Carlo simulation of the 2D Ising model
> on a 32×32 lattice with periodic boundaries. Sweep temperature from 1.0 to
> 3.5 in 20 steps, and at each temperature run enough sweeps to equilibrate,
> then measure the mean absolute magnetization per spin. Save
> `magnetization.png` (⟨|m|⟩ vs T) and print the temperature where the
> magnetization drops most steeply. Use only numpy and matplotlib. Run it and
> comment on how close the crossover is to the known T_c ≈ 2.27.

Why it works live: physics-flavoured, a real computation with a known answer to
check against, numpy-only. Slightly longer; keep the lattice small if time is
tight.

---

### Operator notes
- Have a scratch directory ready and `cd` into it before pasting.
- If the primary stalls on a missing package, tell the agent "use only the
  standard library plus numpy/matplotlib" and let it adapt.
- The point of the demo is the *loop*: writing, running, reading back the
  result, correcting: not the specific artefact.
