"""Synthetic first-year theoretical-physics grade data, 2020-2025.

Units follow the actual course structure:

    assignment  aggregate over 10 weekly take-home sheets, 10 marks each
                -> score out of 100 (numerically equal to a percentage)
    exam        single final written exam, out of 10

So the OLS gradient of exam-on-assignment is in exam-points per
assignment-point: a gradient of 0.10 means one extra assignment point buys
0.1 exam points, i.e. the two instruments agree perfectly in percentage terms.

The generative story
--------------------
Every student has a latent ability theta ~ N(0, 1).  The *exam* measures theta
under invigilation and is therefore stationary across all six years: it is the
control.  The *assignment* is unsupervised homework, and what changes over the
six years is how much of the assignment score is a measurement of theta at all.

    2020-2023   assignment = honest work.  Loads on theta, mean ~40% (the pass
                mark), with a tail of disengaged students running down to zero.
    2024        ChatGPT is widely available.  Each student adopts it to a degree
                u ~ Beta, *independent of theta*.  The assignment score is pulled
                towards a ceiling by an amount proportional to u, which both
                inflates the mean and erases the theta signal.
    2025        Adoption is near-universal and the tooling is better.  The score
                is essentially a measure of "did you run the tool", floored at
                the 40% pass mark, and carries almost no information about theta.

The exam distribution is deliberately held fixed.  That is the whole point of
the plot: the students did not change, the measurement did.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np

DATA_DIR = Path(__file__).parent / "data"

YEARS = [2020, 2021, 2022, 2023, 2024, 2025]

# Cohort sizes: a first-year theory course, ~100 students, varying year to year.
COHORT_SIZE = {2020: 104, 2021: 98, 2022: 112, 2023: 96, 2024: 108, 2025: 101}


@dataclass(frozen=True)
class ExamModel:
    """Invigilated exam, out of 10.  Identical in every year."""

    intercept: float = 4.9  # mean ~49%
    ability_loading: float = 1.9
    noise_scale: float = 0.95  # multiplies a t_4 draw -> fat tails both sides
    noise_df: int = 4

    def sample(self, theta: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        noise = self.noise_scale * rng.standard_t(self.noise_df, size=theta.size)
        return np.clip(self.intercept + self.ability_loading * theta + noise, 0.0, 10.0)


@dataclass(frozen=True)
class AssignmentModel:
    """Unsupervised weekly assignments, aggregate out of 100.

    honest_*        the pre-AI measurement of ability
    disengaged_frac students who stop submitting (the tail into zero)
    ai_*            the ChatGPT channel: an ability-independent pull towards a
                    ceiling, of strength u ~ Beta(ai_a, ai_b)
    floor           hard lower cutoff (2025: nobody is allowed to fail)
    """

    honest_intercept: float = 40.0
    honest_loading: float = 17.0
    honest_noise: float = 6.0
    disengaged_frac: float = 0.10
    ai_a: float | None = None
    ai_b: float | None = None
    ai_ceiling: float = 88.0
    ai_ceiling_spread: float = 12.0
    floor: float | None = None

    def sample(self, theta: np.ndarray, rng: np.random.Generator):
        n = theta.size
        score = self.honest_intercept + self.honest_loading * theta
        score = score + rng.normal(0.0, self.honest_noise, size=n)

        # Disengaged students: they stop handing work in, and they also do badly
        # in the exam -- this is the low-low corner that anchors the pre-AI fit.
        disengaged = rng.random(n) < self.disengaged_frac
        score[disengaged] = rng.uniform(0.0, 25.0, size=disengaged.sum())

        usage = np.zeros(n)
        if self.ai_a is not None:
            usage = rng.beta(self.ai_a, self.ai_b, size=n)  # independent of theta
            # A student-specific ceiling: how well they wield the tool, again
            # nothing to do with physics ability.
            ceiling = rng.normal(self.ai_ceiling, self.ai_ceiling_spread, size=n)
            score = score + usage * (ceiling - score)
            # Heavy users hand everything in, so they leave the disengaged tail.
            disengaged = disengaged & (usage < 0.25)

        if self.floor is not None:
            score = np.maximum(score, self.floor)

        return np.clip(score, 0.0, 100.0), usage, disengaged


# One assignment model per year.  Only this dict encodes the story.
ASSIGNMENT_MODELS = {
    2020: AssignmentModel(honest_intercept=43.0),
    2021: AssignmentModel(honest_intercept=44.0, honest_loading=16.5),
    2022: AssignmentModel(honest_intercept=42.0, honest_loading=17.5, disengaged_frac=0.11),
    2023: AssignmentModel(honest_intercept=44.5, honest_loading=16.8, disengaged_frac=0.09),
    # ChatGPT: partial, uneven adoption.
    2024: AssignmentModel(
        honest_intercept=40.0,
        honest_loading=16.0,
        disengaged_frac=0.05,
        ai_a=2.6,
        ai_b=1.9,
        ai_ceiling=86.0,
        ai_ceiling_spread=14.0,
    ),
    # Near-universal adoption, better tools, and a hard floor at the pass mark.
    2025: AssignmentModel(
        honest_intercept=42.0,
        honest_loading=6.0,
        honest_noise=7.0,
        disengaged_frac=0.01,
        ai_a=6.0,
        ai_b=2.2,
        ai_ceiling=80.0,
        ai_ceiling_spread=13.0,
        floor=40.0,
    ),
}

EXAM = ExamModel()


def simulate_year(year: int) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(year)
    n = COHORT_SIZE[year]
    theta = rng.standard_normal(n)

    assignment, usage, disengaged = ASSIGNMENT_MODELS[year].sample(theta, rng)
    exam = EXAM.sample(theta, rng)
    # The disengaged also stop preparing for the exam.
    exam[disengaged] = rng.uniform(0.0, 3.5, size=int(disengaged.sum()))

    return {
        "student_id": np.array([f"{year}-{i:03d}" for i in range(1, n + 1)]),
        "ability": theta.round(3),
        "assignment": assignment.round(1),
        "exam": exam.round(2),
        "ai_usage": usage.round(3),
    }


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    all_rows = []
    for year in YEARS:
        cols = simulate_year(year)
        rows = [
            {"year": year, **{k: cols[k][i] for k in cols}}
            for i in range(cols["student_id"].size)
        ]
        all_rows.extend(rows)
        print(
            f"{year}: n={len(rows):3d}  "
            f"assignment mean={cols['assignment'].mean():5.1f} "
            f"min={cols['assignment'].min():5.1f}  "
            f"exam mean={cols['exam'].mean():4.2f}"
        )

    out = DATA_DIR / "grades.csv"
    with out.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["year", "student_id", "ability", "assignment", "exam", "ai_usage"]
        )
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"\nwrote {len(all_rows)} rows -> {out}")


if __name__ == "__main__":
    main()
