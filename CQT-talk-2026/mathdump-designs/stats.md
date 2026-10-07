# openai/math hard numbers (computed 2026-10-07 from the clone; see stats.json for everything)
Release: initial commit 2026-10-06 14:58 PDT (22:00 UTC). README: 722 manuscripts, 372 families, ~4,000 problems posed, ~3 h ChatGPT-Pro compute per result, unreleased internal model. Family numbers run 001-377 with 045, 061, 070, 123, 163 absent.
## Totals
files 132,880; size 3.1 GB (lean/ 1.8 GB, preprints/ 606 MB); .lean files 122,141; Lean lines 26,001,191 (25.9M under OAI/; ~213 lines/file; "generated or machine-assisted"); .tex 7,731; tex chars 128.3M / lines 2.78M; PDFs 762 (722 main + 29 figures + 11 traces); .bib 501; bib entries 12,928 (~8,941 unique); verification/ dirs 30 (300 files); .py 125; .md 997; .json 479 (405 comparator configs); 23 patches.
## Per discipline (families / papers / with lean docs / coverage)
Number theory 001-031: 31 / 58 / 16 / 51.6%
Algebraic & complex geometry 032-069: 36 / 89 / 7 / 19.4%
Real & complex analysis 071-086: 16 / 26 / 9 / 56.2%
Convex & metric geometry 087-101: 15 / 30 / 13 / 86.7%
Theoretical CS 102-142: 40 / 73 / 32 / 80.0%
Dynamics & ergodic theory 143-154: 12 / 19 / 9 / 75.0%
Combinatorics 155-192: 37 / 50 / 33 / 89.2%
Algebra 193-210: 18 / 29 / 9 / 50.0%
Probability & stat mech 211-239: 29 / 105 / 19 / 65.5%
Mathematical logic 240-245: 6 / 8 / 6 / 100%
Group theory 246-259: 14 / 22 / 12 / 85.7%
Mathematical physics 260-284: 25 / 59 / 17 / 68.0%
Operator algebras 285-303: 19 / 31 / 14 / 73.7%
Topology 304-321: 18 / 26 / 3 / 16.7%
Functional analysis 322-332: 11 / 19 / 10 / 90.9%
Differential geometry 333-361: 29 / 49 / 15 / 51.7%
PDE 362-377: 16 / 29 / 11 / 68.8%
TOTAL: 372 / 722 / 235 / 63.2%
Caveat: formalization.yaml lists only 192 source papers; 405 comparator challenges (several per family). "Has lean docs" ≠ "headline verified": the docs often formalize a fragment (e.g. 266 MUB(6)=3 formalizes only ≤5; 265 area law has NO docs entry yet a 24k-line Lean tree for its §2 subvolume bound).
## Papers per family
min 1, median 1, mean 1.94, max 14. Histogram 1:205, 2:96, 3:36, 4:13, 5:7, 6:4, 7:3, 8:3, 9:1, 12:1, 13:2, 14:1. 55% single-paper. Largest: 034 log abundance Kähler (14), 260 spacetime Penrose (13), 237 honeycomb SAW (13), 238 Thorp shuffle (12), 376 universal computation in Navier–Stokes (9), 227 SK autocorrelation (8), 032 K3 Hodge/Kuga–Satake (8), 014 restricted geometric Langlands (8).
## Dates (from directory names; 721 dated + 1 ISO-named = Sep 24)
Sep 10: 2; Sep 17: 1; Sep 18: 1; Sep 22: 3; Sep 23: 177; Sep 24: 193 (busiest, 26.7%); Sep 25: 90; Sep 26: 53; Sep 27: 51; Sep 30: 5; Oct 1: 1; Oct 2: 1; Oct 3: 6; Oct 4: 24; Oct 5: 112; Oct 6: 1.
Sep 23-24 = 370 papers = 51.2%. Sep 23-27 = 564 = 78%. Oct 4-5 = 136 = 19%. First Sep 10, last Oct 6.
## Length
tex chars: min 18,006 / median 132,006 / mean 177,259 / max 2,989,884. tex lines: 465 / 2,948 / 3,844 / 85,632. PDF pages (722 main): min 6 / median 39 / mean 48 / max 262; total 34,815 pages (all 762 PDFs: 35,087). Page histogram by tens: 0-9:11, 10s:115, 20s:143, 30s:98, 40s:105, 50s:61, 60s:42, 70s:35, 80s:28, 90s:25, 100s:15, 110s:7, 120s:7, 130s:5, 140s:5, 150+:20.
Longest tex: Uniform Stability of the Spherical Laughlin Gap 2.99M chars / 85,632 lines (3x next); 3-machine scheduling 1.08M; Spacetime Penrose 0.99M (262 pages, longest PDF); FK interfaces 0.96M; FK planar maps 0.89M (232 pp); Liouville sphere q=4 0.85M (217 pp); limit cycles 0.83M; self-dual RC interfaces 0.82M (207 pp); Quasi-Riemann (Sep 30) 0.77M (199 pp); quasipolynomial AP 0.76M (198 pp). Shortest: 6-7 page papers (~18k chars).
## Lean
docs 235; ComparatorChallenges 405 .lean + 405 .json; OAI lines 25,910,542 in 121,734 files; sorry in OAI: 0; sorry in challenges: 509 (placeholders, intentional); 507 theorem names; axioms allowed in all 405 configs: propext, Quot.sound, Classical.choice only; toolchain lean4 v4.34.1; Mathlib pinned to commit d13f23b7; 23 patches porting external libs (PrimeNumberTheoremAnd, carleson, gromov, iut...). comparator tool checks solution proves exactly the challenge statement; needs comparator + landrun sandbox + lean4export.
OAI lines by area: Analysis 6.82M, Combinatorics 5.77M, NumberTheory 2.99M, Probability 2.25M, Geometry 2.25M, Computability 1.46M, MathematicalPhysics 1.28M, GroupTheory 0.54M.
Top subtrees: Analysis/MutuallyUnbiased 2.84M lines (fam 266); Combinatorics/Ramsey 2.80M (189); Combinatorics/Progressions 1.12M (159); Analysis/PlanarPacking 0.92M (090); NumberTheory/Ostmann 0.61M (013); NumberTheory/Catalan 0.57M (005); MathematicalPhysics/Transonic 0.51M (?); NumberTheory/DirichletL 0.49M (003 quasi-RH); NumberTheory/CubicMoment 0.30M (023); GroupTheory/PolycyclicRecognition 0.26M (255). Top 3 = 26% of all Lean.
## Keyword scan (372 headings)
"conjecture" in 84 headings (183 descriptions); conjecture/problem/hypothesis 101; counterexample/disprove 30 headings (54 descr; lower bound); classif 6; hardness/NP/undecidab 5; named-conjecture heuristic 100 headings. First word of descriptions: Proves 165, Constructs 43, Resolves 41, Disproves 18, Determines 9, Classifies 5, Answers 3.
Famous named problems in headings (48): 003 quasi-Riemann hypothesis (Re s > 7/8; alt 11/12 human-edited); 004 Hilbert's tenth over Q; 002 full BSD from low Selmer corank; 005 irrationality of Catalan's constant; 017 irrationality exponent of π is 2; 006 Goldfeld; 102 Unique Games Conjecture; 103 L=RL=BPL; 107 matrix mult ω ≤ 9/4; 109 integer multiplication below n log n; 138 Subset Sum O(2^{0.49n}); 156 Borsuk fails in dim 9; 158 plane not 5-colourable; 161 Sidorenko counterexample; 162 Ryser counterexample; 168 KL combinatorial invariance; 173 Seymour second neighbourhood; 180 Barnette; 196 Kaplansky zero-divisor counterexample; 197 Kaplansky direct finiteness; 157 Hadwiger disproved (fractional); 073 Falconer; 078 3D Bochner–Riesz; 087 Mahler; 143 Hilbert 16th uniform bounds; 246 Cannon; 248 Thompson's F nonamenable; 285 Baum–Connes & Kadison–Kaplansky counterexamples; 287 free group factors isomorphic; 288 Kadison similarity; 304 Hilbert–Smith; 312 Grothendieck homotopy hypothesis; 268 spin-one Haldane gap; 274 parity ∉ QAC0; 338 Yau uniformization; 339 Katok entropy rigidity; 340 nearby Lagrangian counterexample; 369 hot spots; 375 De Giorgi dim 8; 244 Partition Principle ⇏ Choice; 038 Fujita freeness; 040 Bloch for surfaces; 193 Serre multiplicity; 194 Lech; 259 group without fixed price; 322 Tingley; 344 metric Blaschke; 016 Zilber–Pink; 039 Nagata.
## Reasoning traces (10): 007 (7 pp), 017 π (42), 087 Mahler (45), 102 (16), 159 (41), 197 (23), 221 (5), 271 Heisenberg FM (6), 362 RVM (6), 287 free group factors (11). Total 202 pp.
## Bibliography
Top cited: OpenAI 403 entries (self-citation, 3.1%, @misc "OpenAI Math Release preprint"); Demailly 99; Lieb 95; Peternell 91; Fujino 90; Tao 86 (57 unique, top human by unique); Campana 80; Milne 68; Sheffield 67; Kollár 63; Miller 60; Hacon 60; Duminil-Copin 54; Gwynne 53; Păun 53; Yau 51; Birkar 50; Gromov 49; Schramm 46; Deligne 46; Serre 43; Bourgain 42; Khot 41; Erdős ~50 combined.
Cited years: ≤1900s 14; 1910s 16; 1920s 50; 1930s 118; 1940s 99; 1950s 329; 1960s 589; 1970s 1,038; 1980s 996; 1990s 1,296; 2000s 2,226; 2010s 2,922; 2020s 3,185. Range 1637-2027. 2025: 502; 2026: 1,217 (9.4%; 814 of them not OpenAI). Mean 17.9 bib entries per paper; max 96.
## Other
Provenance exceptions: QRH zero-free region and Hodge for CM abelian varieties did not follow the standard procedure; 11/12 writeup "human edited for readability"; Oct 5 QRH README "written with human assistance". 4 INPUTS.md files (one says source argument "does not establish that it was the final revision"). 30 verification/ dirs with Python + JSON certificates (e.g. Heisenberg chain: scalar_checks.py, trial_verify.py). Every preprint has build/ tex sources. No errata files. Main PDF names: paper.pdf 424, main.pdf 91, manuscript.pdf 19, article.pdf 16...
