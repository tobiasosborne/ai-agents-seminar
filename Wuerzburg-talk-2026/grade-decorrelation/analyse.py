"""Regression analysis and figures for the assignment/exam decorrelation.

For each year we fit, by OLS,

    exam = a + b * assignment          exam out of 10, assignment out of 100

and report b with a heteroskedasticity-robust (HC3) standard error, its 95%
confidence interval, R^2, Pearson r, Spearman rho (rank-based, so it does not
care about the ceiling effects the AI channel introduces), and the p-value for
H0: b = 0.

We additionally test the headline claim directly, by fitting the pooled model

    exam = a + b * assignment + c * post + d * (assignment x post)

with post = 1 for 2024-25.  The interaction coefficient d is the change in the
gradient after ChatGPT; the story stands or falls on d < 0.

Outputs: results/regression_summary.{csv,md} and figures/*.{pdf,png}
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

ROOT = Path(__file__).parent
FIG_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"

YEARS = [2020, 2021, 2022, 2023, 2024, 2025]
POST_YEARS = [2024, 2025]

# --- Whitney Teal palette, matching the TJO beamer theme -------------------
INK = "#335B74"  # tjo@darkteal   -- data marks, primary text
ACCENT = "#1CADE4"  # tjo@cyan     -- the fitted line
GRID = "#DFE3E5"  # tjo@lightgrey -- recessive grid
MUTED = "#7C8B95"  # secondary ink
SURFACE = "#FFFFFF"

# Categorical hues for the three-era distribution plot. Validated with the
# dataviz palette checker: passes lightness band, chroma floor and CVD
# separation (deutan dE 46.5). Tritan separation sits in the 8-12 floor band,
# so each series also carries a distinct line style and a direct label.
GROUP_PRE = "#2683C6"  # tjo@medblue -- 2020-2023
GROUP_2024 = "#42BA97"  # tjo@green
GROUP_2025 = "#1CADE4"  # tjo@cyan

PASS_MARK = 40.0  # 40% is the Studienleistung pass mark

mpl.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": MUTED,
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.labelcolor": INK,
        "axes.labelsize": 11,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlecolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "font.size": 10,
        # Whitney has no U+2212; fall back to the ASCII hyphen for negatives.
        "axes.unicode_minus": False,
        "font.family": "sans-serif",
        "font.sans-serif": ["Whitney", "Helvetica", "DejaVu Sans"],
        "savefig.bbox": "tight",
        "savefig.dpi": 200,
    }
)


def fit_year(df: pd.DataFrame) -> dict:
    """OLS of exam on assignment, with HC3 robust errors."""
    x = df["assignment"].to_numpy()
    y = df["exam"].to_numpy()
    model = sm.OLS(y, sm.add_constant(x)).fit(cov_type="HC3")

    slope = model.params[1]
    lo, hi = model.conf_int(alpha=0.05)[1]
    rho, rho_p = stats.spearmanr(x, y)

    return {
        "year": int(df["year"].iloc[0]),
        "n": len(df),
        "slope": slope,
        "slope_se": model.bse[1],
        "slope_lo": lo,
        "slope_hi": hi,
        "intercept": model.params[0],
        "r": float(np.sign(slope) * np.sqrt(max(model.rsquared, 0.0))),
        "r2": model.rsquared,
        "p": model.pvalues[1],
        "spearman": rho,
        "spearman_p": rho_p,
        "assignment_mean": x.mean(),
        "assignment_median": float(np.median(x)),
        "assignment_sd": x.std(ddof=1),
        "frac_below_pass": float((x < PASS_MARK).mean()),
        "exam_mean": y.mean(),
        "exam_sd": y.std(ddof=1),
        "model": model,
    }


def difference_in_slopes(data: pd.DataFrame) -> sm.regression.linear_model.RegressionResults:
    """Pooled interaction model: does the gradient change after ChatGPT?"""
    d = data.copy()
    d["post"] = d["year"].isin(POST_YEARS).astype(float)
    d["interaction"] = d["assignment"] * d["post"]
    X = sm.add_constant(d[["assignment", "post", "interaction"]])
    return sm.OLS(d["exam"], X).fit(cov_type="HC3")


def panel(ax, df: pd.DataFrame, fit: dict, *, show_ylabel=True, show_xlabel=True) -> None:
    """One year: scatter + OLS fit + 95% band. One series, so no legend."""
    x = df["assignment"].to_numpy()
    y = df["exam"].to_numpy()
    significant = fit["p"] < 0.05

    ax.grid(axis="both", zorder=0)
    ax.set_axisbelow(True)
    ax.axvline(PASS_MARK, color=MUTED, lw=1.0, ls=(0, (4, 3)), alpha=0.55, zorder=1)

    # 2px white ring on each marker so overlapping points stay countable.
    ax.scatter(
        x, y, s=34, facecolor=INK, alpha=0.55, edgecolor=SURFACE, linewidth=0.8, zorder=3
    )

    # Fit only over the range where students actually exist -- no extrapolation
    # into empty space (2025 has nobody below the pass mark at all).
    xs = np.linspace(x.min(), x.max(), 200)
    pred = fit["model"].get_prediction(sm.add_constant(xs)).summary_frame(alpha=0.05)
    ax.fill_between(
        xs, pred["mean_ci_lower"], pred["mean_ci_upper"], color=ACCENT, alpha=0.16, zorder=2
    )
    ax.plot(
        xs,
        pred["mean"],
        color=ACCENT,
        lw=2.0,
        ls="-" if significant else (0, (5, 3)),
        zorder=4,
    )

    label = f"gradient = {fit['slope']:.3f}\n$r$ = {fit['r']:.2f}"
    label += f",  $p$ = {fit['p']:.0e}" if significant else ",  n.s."
    ax.text(
        0.035,
        0.965,
        label,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        color=INK,
        bbox=dict(facecolor=SURFACE, edgecolor=GRID, boxstyle="round,pad=0.4", alpha=0.92),
    )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 10)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.set_title(f"{fit['year']}   (n = {fit['n']})", loc="left", pad=10)
    if show_xlabel:
        ax.set_xlabel("Assignment aggregate  /100")
    if show_ylabel:
        ax.set_ylabel("Final exam  /10")


def main() -> None:
    FIG_DIR.mkdir(exist_ok=True)
    RESULTS_DIR.mkdir(exist_ok=True)

    data = pd.read_csv(ROOT / "data" / "grades.csv")
    fits = {y: fit_year(data[data["year"] == y]) for y in YEARS}

    # --- 1-6: one standalone figure per year -------------------------------
    for year in YEARS:
        fig, ax = mpl.pyplot.subplots(figsize=(5.4, 4.2))
        panel(ax, data[data["year"] == year], fits[year])
        for ext in ("pdf", "png"):
            fig.savefig(FIG_DIR / f"scatter_{year}.{ext}")
        mpl.pyplot.close(fig)

    # --- 7: the 2x3 grid, for a single slide -------------------------------
    fig, axes = mpl.pyplot.subplots(2, 3, figsize=(14.5, 8.4), sharex=True, sharey=True)
    for ax, year in zip(axes.flat, YEARS):
        panel(
            ax,
            data[data["year"] == year],
            fits[year],
            show_ylabel=(year in (2020, 2023)),
            show_xlabel=(year in (2023, 2024, 2025)),
        )
    fig.suptitle(
        "Assignment grade vs. final exam grade, first-year theoretical physics",
        color=INK,
        fontsize=15,
        fontweight="bold",
        x=0.5,
        y=0.995,
    )
    fig.text(
        0.5,
        0.952,
        "The exam distribution is unchanged. The assignment stopped measuring anything.",
        ha="center",
        color=MUTED,
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.935])
    for ext in ("pdf", "png"):
        fig.savefig(FIG_DIR / f"scatter_grid.{ext}")
    mpl.pyplot.close(fig)

    # --- 8: the gradient itself, year by year ------------------------------
    fig, ax = mpl.pyplot.subplots(figsize=(7.2, 4.2))
    slopes = np.array([fits[y]["slope"] for y in YEARS])
    lo = np.array([fits[y]["slope_lo"] for y in YEARS])
    hi = np.array([fits[y]["slope_hi"] for y in YEARS])

    ax.axhline(0.0, color=MUTED, lw=1.0, zorder=1)
    ax.annotate(
        "no predictive power",
        xy=(2019.75, 0.003),
        color=MUTED,
        fontsize=9,
        ha="left",
        va="bottom",
    )
    ax.axvline(2023.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.annotate(
        "ChatGPT in\nwidespread use",
        xy=(2023.55, 0.125),
        color=MUTED,
        fontsize=9,
        ha="left",
        va="top",
    )
    ax.errorbar(
        YEARS,
        slopes,
        yerr=[slopes - lo, hi - slopes],
        fmt="o",
        ms=8,
        color=INK,
        ecolor=ACCENT,
        elinewidth=2,
        capsize=4,
        markeredgecolor=SURFACE,
        markeredgewidth=1.0,
        zorder=3,
    )
    ax.plot(YEARS, slopes, color=ACCENT, lw=2.0, alpha=0.5, zorder=2)
    ax.grid(axis="y")
    ax.set_axisbelow(True)
    ax.set_xticks(YEARS)
    ax.set_xlim(2019.6, 2025.4)
    ax.set_ylim(-0.04, 0.14)
    ax.set_xlabel("Year")
    ax.set_ylabel("OLS gradient  (exam pts / assignment pt)")
    ax.set_title("The assignment stops predicting the exam", loc="left", pad=10)
    for ext in ("pdf", "png"):
        fig.savefig(FIG_DIR / f"gradient_by_year.{ext}")
    mpl.pyplot.close(fig)

    # --- 9: the marginal distributions, which is where the story starts -----
    # Six overlaid histograms is spaghetti. Pool the four stationary pre-AI
    # years into one band and show 2024 and 2025 against it: three series, each
    # with its own line style as well as its own hue, and direct labels.
    pre = data[~data["year"].isin(POST_YEARS)]
    groups = [
        ("2020-2023", pre, GROUP_PRE, "-", 1.8, True),
        ("2024", data[data["year"] == 2024], GROUP_2024, (0, (5, 2)), 2.0, False),
        ("2025", data[data["year"] == 2025], GROUP_2025, "-", 2.6, False),
    ]

    fig, axes = mpl.pyplot.subplots(2, 1, figsize=(7.8, 6.6))
    specs = [
        ("assignment", np.linspace(0, 100, 21), "Assignment aggregate", "Score /100"),
        ("exam", np.linspace(0, 10, 21), "Final exam", "Score /10"),
    ]
    for ax, (col, bins, title, xlabel) in zip(axes, specs):
        for label, sub, colour, ls, lw, fill in groups:
            dens, edges = np.histogram(sub[col], bins=bins, density=True)
            centres = 0.5 * (edges[:-1] + edges[1:])
            if fill:
                ax.fill_between(
                    centres, dens, color=colour, alpha=0.16, step="mid", zorder=1
                )
            ax.step(
                centres, dens, where="mid", color=colour, ls=ls, lw=lw,
                label=label, zorder=3,
            )
        ax.set_title(title, loc="left", pad=8)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("density")
        ax.grid(axis="y")
        ax.set_axisbelow(True)
        ax.set_xlim(bins[0], bins[-1])
        ax.margins(y=0.18)

    ax = axes[0]
    ax.axvline(PASS_MARK, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=2)
    ax.annotate(
        "pass mark",
        xy=(PASS_MARK - 1.5, ax.get_ylim()[1] * 0.97),
        color=MUTED,
        fontsize=9,
        ha="right",
        va="top",
    )
    # Direct labels: identity is never carried by colour alone.
    for label, xy, xytext in [
        ("2020-2023", (35, 0.0225), (17, 0.031)),
        ("2024", (95, 0.0075), (90, 0.017)),
        ("2025", (56, 0.0355), (44, 0.038)),
    ]:
        ax.annotate(
            label, xy=xy, xytext=xytext, color=INK, fontsize=9, fontweight="bold",
            ha="center",
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8, shrinkA=2, shrinkB=2),
        )
    axes[1].legend(frameon=False, fontsize=9, ncol=3, loc="upper right")
    axes[1].annotate(
        "the exam never moved",
        xy=(0.02, 0.93),
        xycoords="axes fraction",
        color=MUTED,
        fontsize=10,
        style="italic",
    )
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG_DIR / f"distributions.{ext}")
    mpl.pyplot.close(fig)

    # --- summary table -----------------------------------------------------
    cols = [
        "year", "n", "slope", "slope_se", "slope_lo", "slope_hi", "r", "r2", "p",
        "spearman", "spearman_p", "assignment_mean", "assignment_median",
        "assignment_sd", "frac_below_pass", "exam_mean", "exam_sd",
    ]
    summary = pd.DataFrame([{k: f[k] for k in cols} for f in fits.values()])
    summary.to_csv(RESULTS_DIR / "regression_summary.csv", index=False)

    did = difference_in_slopes(data)
    d_coef = did.params["interaction"]
    d_lo, d_hi = did.conf_int().loc["interaction"]
    d_p = did.pvalues["interaction"]

    lines = [
        "# Assignment/exam decorrelation — regression summary",
        "",
        "Synthetic data. `exam = a + b * assignment`, OLS with HC3 robust errors.",
        "Assignment out of 100, exam out of 10, so `b = 0.10` means the two",
        "instruments agree exactly in percentage terms.",
        "",
        "| Year | n | gradient b | 95% CI | r | R² | p | Spearman ρ | mean assign. | % below pass | mean exam |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for f in fits.values():
        p_str = f"{f['p']:.1e}" if f["p"] < 0.05 else f"{f['p']:.2f} (n.s.)"
        lines.append(
            f"| {f['year']} | {f['n']} | {f['slope']:.3f} | "
            f"[{f['slope_lo']:.3f}, {f['slope_hi']:.3f}] | {f['r']:.2f} | {f['r2']:.2f} | "
            f"{p_str} | {f['spearman']:.2f} | {f['assignment_mean']:.1f} | "
            f"{100 * f['frac_below_pass']:.0f}% | {f['exam_mean']:.2f} |"
        )
    lines += [
        "",
        "## Did the gradient actually change?",
        "",
        "Pooled model `exam = a + b·assignment + c·post + d·(assignment × post)`,",
        "with `post = 1` for 2024–25:",
        "",
        f"- gradient before ChatGPT: **b = {did.params['assignment']:.3f}**",
        f"- change in gradient after: **d = {d_coef:.3f}**  "
        f"(95% CI [{d_lo:.3f}, {d_hi:.3f}], p = {d_p:.1e})",
        f"- gradient after ChatGPT: **b + d = {did.params['assignment'] + d_coef:.3f}**",
        "",
        "The interaction is large, negative and highly significant: the assignment",
        "grade has lost essentially all of its predictive power over the exam.",
    ]
    (RESULTS_DIR / "regression_summary.md").write_text("\n".join(lines) + "\n")

    print("\n".join(lines[6:14]))
    print(f"\ninteraction d = {d_coef:.4f}  p = {d_p:.2e}")
    print(f"\nfigures -> {FIG_DIR}")


if __name__ == "__main__":
    import matplotlib.pyplot  # noqa: F401  (rcParams set before pyplot import)

    main()
