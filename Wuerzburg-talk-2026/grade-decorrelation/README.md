# Assignment/exam decorrelation — synthetic illustration

Figures for the Würzburg Physikalisches Kolloquium talk, illustrating the
finding from the analysis of our first-year theoretical physics courses:
**the weekly take-home assignment (Studienleistung) stopped predicting the
final exam (Prüfungsleistung) when ChatGPT arrived.**

> ⚠️ **The data in `data/grades.csv` is synthetic.** It is generated to
> reproduce the qualitative structure of the real six-year analysis, not the
> real numbers. Nothing here should be presented as the measured data, and no
> student-level data is involved. See "Honesty on the slide" below.

## The finding, in one line

The exam distribution is stationary across all six years. The assignment
distribution inflates and compresses. The gradient relating them collapses to
zero — so the two instruments, which used to measure the same thing, no longer
measure the same thing. It is the *assignment* that stopped measuring.

| Year | gradient b | 95% CI | r | mean assignment | % below pass | mean exam |
|---|---|---|---|---|---|---|
| 2020 | 0.099 | [0.084, 0.114] | 0.79 | 39.9 | 53% | 4.64 |
| 2021 | 0.097 | [0.084, 0.110] | 0.82 | 41.1 | 43% | 4.34 |
| 2022 | 0.107 | [0.096, 0.118] | 0.84 | 37.8 | 57% | 4.37 |
| 2023 | 0.092 | [0.078, 0.107] | 0.80 | 39.2 | 50% | 4.34 |
| 2024 | 0.049 | [0.021, 0.076] | 0.33 | 67.1 | 6%  | 4.95 |
| 2025 | 0.015 | [-0.024, 0.055] | 0.08 | 70.1 | 0%  | 4.63 |

Full numbers, including Spearman ρ and the pooled interaction test, in
`results/regression_summary.md`.

## Units

Assignment: 10 weekly sheets × 10 marks = aggregate **out of 100**.
Exam: **out of 10**. So the OLS gradient is in exam-points per assignment-point,
and **b = 0.10 means the two instruments agree exactly** in percentage terms —
which is what 2020–2023 shows. b = 0 means the assignment grade tells you
nothing about the exam.

## The generative model (`generate_data.py`)

Every student has a latent ability θ ~ N(0,1).

- **Exam** — invigilated, so it measures θ in every year. Its parameters are
  *identical* for all six years: `exam = 4.9 + 1.9 θ + 0.95 · t₄`, giving a
  roughly normal distribution centred near 50% with fat tails on both sides.
  This is the control.
- **Assignment 2020–2023** — honest work: `40ish + 17 θ + N(0,6)`, peaked at the
  40% pass mark, plus ~10% disengaged students who stop submitting (the tail
  running into 0%, who also do badly in the exam).
- **Assignment 2024** — each student adopts ChatGPT to a degree u ~ Beta(2.6,1.9),
  **independent of θ**, which pulls their score towards a ceiling: `score +=
  u · (ceiling − score)`. This simultaneously inflates the mean above 60%,
  erases the low tail, and destroys the θ signal.
- **Assignment 2025** — near-universal adoption (u ~ Beta(6,2.2)), a much weaker
  honest loading (6 instead of 17), and a hard floor at the 40% pass mark:
  nobody fails. Peak at 60–70%.

The key structural point: **AI usage is uncorrelated with ability.** That is the
entire mechanism. A high assignment mark in 2025 is evidence that a student ran
a tool, not that they understand Lagrangian mechanics.

## The analysis (`analyse.py`)

Per year: OLS of exam on assignment with **HC3 heteroskedasticity-robust**
standard errors (the residual variance is not constant once the ceiling
effects bite), 95% CI on the gradient, R², Pearson r, and Spearman ρ as a
rank-based check that the collapse is not an artefact of the ceiling.

The headline claim is also tested directly, by pooling all six years and
fitting

    exam = a + b·assignment + c·post + d·(assignment × post),    post = 1 for 2024–25

The interaction coefficient is **d = −0.063, p ≈ 1×10⁻⁷** — the gradient after
ChatGPT is 0.099 − 0.063 ≈ 0.036 and falls to ~0.015 by 2025. The decorrelation
is not eyeballed off a scatter plot; it is a significant interaction.

## Figures

| File | Use |
|---|---|
| `figures/scatter_2020.pdf` … `scatter_2025.pdf` | The six requested plots — one year each, assignment vs exam, OLS fit + 95% band. Build the story one slide at a time. |
| `figures/scatter_grid.pdf` | All six on one slide (2×3). The punchline slide. |
| `figures/gradient_by_year.pdf` | The gradient with CIs, year by year — the collapse as a single line. |
| `figures/distributions.pdf` | The marginals: the assignment moved, the exam did not. |

Non-significant fits are drawn **dashed** and annotated `n.s.`, so significance
is never carried by colour alone. Fits are drawn only over the range where
students actually exist — in 2025 nobody scores below 40, so the line starts there.

## Regenerating

```bash
../../feo_venv/bin/python generate_data.py   # writes data/grades.csv
../../feo_venv/bin/python analyse.py         # writes figures/ and results/
```

Deterministic: each year is seeded with the year, so the figures are stable
across runs. Needs numpy, scipy, pandas, matplotlib, statsmodels.

Colours are the deck's Whitney Teal palette (`beamercolorthemeTJO.sty`); the
three-series categorical set in `distributions.pdf` was checked with the dataviz
palette validator (passes lightness, chroma and CVD separation; the tritan
margin is in the floor band, so each series also has its own line style and a
direct label).

## Honesty on the slide

The data is synthetic and the slide must say so. Two defensible framings:

1. **"Illustration of the effect we measured"** — put *Synthetic data,
   illustrative* in the caption, quote the real gradients in the text, and
   describe the actual study verbally.
2. Swap `data/grades.csv` for the real aggregates and re-run `analyse.py`
   unchanged — the analysis code makes no assumption about where the CSV came
   from. It only needs columns `year, assignment, exam`.

The second is much stronger if the real data can be shared in aggregate.
