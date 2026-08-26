# Model progress — key numbers

Source: Epoch AI Benchmarking Hub (CC-BY), snapshot 2026-08-26. 198 distinct models.

- **snapshot**: 2026-08-26
- **n_models_total**: 198
- **gpqa_top**: 0.9482323232323232
- **gpqa_top_model**: gemini-3.7-flash_high
- **eci_points_per_year**: 13.67
- **n_models_since_2023**: 198
- **frontier_leader**: Claude Fable 5 (162.49)
- **open_frontier_leader**: Kimi K3 (157.49)
- **estimated_eci_qwen_3_8_27b**: 153.74
- **median_days_between_records_before_jul2024**: 56.0
- **median_days_between_records_since_jul2025**: 47.0
- **models_per_quarter_2023**: 9.25
- **models_per_quarter_2026**: 20.5
- **median_lag_months_since_2025**: 5.3
- **latest_lag_months**: 4.4
- **latest_open_model**: Kimi K3

## Benchmark ladder (is it dead?)

```
                benchmark first_measured  best_today date_of_best  dead
                     MMLU     2021-08-05       0.881   2024-11-20 False
             MATH level 5     2023-06-13       0.981   2025-08-07  True
             GPQA Diamond     2023-03-14       0.948   2026-08-13  True
             FrontierMath     2024-06-20       0.524   2026-04-23 False
     Humanity's Last Exam     2024-09-24       0.464   2026-02-19 False
CritPt (research physics)     2024-07-23       0.323   2026-07-09 False
```

## Open-weights lag

```
 open_date        open_model    eci closed_first_reached closed_model  lag_days
2025-09-29 DeepSeek-V3.2-Exp 144.86           2025-04-16           o3       166
2025-11-06  Kimi K2 Thinking 145.94           2025-04-16           o3       204
2025-12-01     DeepSeek-V3.2 146.38           2025-04-16           o3       229
2026-01-27         Kimi K2.5 148.13           2025-08-07        GPT-5       173
2026-04-07           GLM-5.1 150.86           2025-11-18 Gemini 3 Pro       140
2026-04-20         Kimi K2.6 151.04           2025-11-18 Gemini 3 Pro       153
2026-06-16           GLM-5.2 152.14           2025-11-18 Gemini 3 Pro       210
2026-07-16           Kimi K3 157.49           2026-03-05  GPT-5.4 Pro       133
```

## Estimated ECI (not an Epoch measurement)

- **Qwen 3.8 27B** (2026-08-14, Alibaba, Open weights (unrestricted)): **ECI 153.74**, give or take 3.9 index points.
  - inverted from vendor self-reported GPQA diamond 89.2%, HLE 30.8% via Epoch's own IRT item parameters
  - per-benchmark: GPQA diamond -> 153.59; HLE -> 153.79
  - uncertainty = RMS error of the same two-benchmark inversion against Epoch's published ECI, over models with ECI >= 148
  - not used in any envelope, fit or lag number
  - unusable vendor benchmarks (not in Epoch's ECI item bank): LiveCodeBench v6 90.3%, SWE-bench Pro 61.7%
