# Assignment/exam decorrelation — regression summary

Synthetic data. `exam = a + b * assignment`, OLS with HC3 robust errors.
Assignment out of 100, exam out of 10, so `b = 0.10` means the two
instruments agree exactly in percentage terms.

| Year | n | gradient b | 95% CI | r | R² | p | Spearman ρ | mean assign. | % below pass | mean exam |
|---|---|---|---|---|---|---|---|---|---|---|
| 2020 | 104 | 0.099 | [0.084, 0.114] | 0.79 | 0.62 | 5.1e-38 | 0.78 | 39.9 | 53% | 4.64 |
| 2021 | 98 | 0.097 | [0.084, 0.110] | 0.82 | 0.67 | 3.8e-47 | 0.82 | 41.1 | 43% | 4.34 |
| 2022 | 112 | 0.107 | [0.096, 0.118] | 0.84 | 0.71 | 4.1e-81 | 0.81 | 37.8 | 57% | 4.37 |
| 2023 | 96 | 0.092 | [0.078, 0.107] | 0.80 | 0.63 | 3.0e-35 | 0.79 | 39.2 | 50% | 4.34 |
| 2024 | 108 | 0.049 | [0.021, 0.076] | 0.33 | 0.11 | 4.8e-04 | 0.29 | 67.1 | 6% | 4.95 |
| 2025 | 101 | 0.015 | [-0.024, 0.055] | 0.08 | 0.01 | 0.44 (n.s.) | 0.08 | 70.1 | 0% | 4.63 |

## Did the gradient actually change?

Pooled model `exam = a + b·assignment + c·post + d·(assignment × post)`,
with `post = 1` for 2024–25:

- gradient before ChatGPT: **b = 0.099**
- change in gradient after: **d = -0.063**  (95% CI [-0.086, -0.040], p = 1.1e-07)
- gradient after ChatGPT: **b + d = 0.036**

The interaction is large, negative and highly significant: the assignment
grade has lost essentially all of its predictive power over the exam.
