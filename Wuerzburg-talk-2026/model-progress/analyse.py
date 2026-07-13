"""Model capability vs time: capability, cadence, and the open-weights lag.

All numbers come from Epoch AI's Benchmarking Hub bulk export (data/epoch/),
snapshot 2026-07-12. One evaluator, one methodology, open and closed models
measured the same way. Nothing here is hand-entered from a press release.

Figures
-------
fig1_gpqa_dead        Adam Brown's plot (GPQA vs date), brought up to today.
                      Random-guess floor, PhD-expert line, and the ceiling it hit.
fig2_benchmark_ladder Each benchmark's frontier envelope. Brown's "shifted about a
                      year" device, extended past his talk: MMLU -> MATH-5 -> GPQA
                      -> FrontierMath -> HLE -> CritPt. Each made later, solved
                      later, and the gaps are shrinking.
fig3_eci_frontier     THE headline. Epoch Capabilities Index (cannot saturate) vs
                      release date, 2023-2026. Closed frontier, open-weights
                      frontier, this week's releases called out by name.
fig4_cadence          Frequency: releases per quarter, and the shrinking interval
                      between successive frontier records.
fig5_open_weight_lag  How far behind is open-weights? Measured horizontally.

Why ECI for the headline: individual benchmarks saturate and die (fig1/fig2 are
the evidence). Epoch's Capabilities Index is an IRT-style latent-ability scale
fitted across many benchmarks, so it keeps going when its constituents cap out --
like Elo, it has no ceiling. That is exactly what a "capability vs time" plot needs.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent
EPOCH = ROOT / "data" / "epoch"
FIG = ROOT / "figures"
RESULTS = ROOT / "results"

SNAPSHOT = "2026-07-12"

# --- Whitney Teal palette (TJO beamer theme) -------------------------------
INK = "#335B74"
MUTED = "#7C8B95"
GRID = "#DFE3E5"
SURFACE = "#FFFFFF"
# Validated categorical trio (dataviz validator: lightness/chroma/CVD pass;
# tritan in floor band -> every series also carries a marker shape + direct label)
CLOSED = "#2683C6"  # closed-weights models
OPEN = "#42BA97"  # open-weights models
HILITE = "#1CADE4"  # released in the last ~5 weeks

mpl.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.labelcolor": INK, "axes.labelsize": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "grid.color": GRID, "grid.linewidth": 0.8,
    "font.size": 10, "axes.unicode_minus": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["Whitney", "Helvetica", "DejaVu Sans"],
    "savefig.bbox": "tight", "savefig.dpi": 200,
})

# benchmark file -> (score column, display name, human-reference line or None)
BENCHMARKS = {
    "mmlu_external": ("EM", "MMLU", None),
    "math_level_5": ("mean_score", "MATH level 5", None),
    "gpqa_diamond": ("mean_score", "GPQA Diamond", 0.697),
    "frontiermath": ("mean_score", "FrontierMath", None),
    "hle_external": ("Accuracy", "Humanity's Last Exam", None),
    "critpt_external": ("Accuracy", "CritPt (research physics)", None),
}

# The models the talk must depict: everything from the last ~5 weeks.
THIS_WEEK_FROM = pd.Timestamp("2026-06-05")


def load_eci() -> pd.DataFrame:
    """One row per model: best config, release date, open/closed."""
    e = pd.read_csv(EPOCH / "epoch_capabilities_index.csv")
    e["date"] = pd.to_datetime(e["Release date"], errors="coerce")
    e = e.dropna(subset=["date", "ECI Score"])
    e = e[e["Model accessibility"] != "Unreleased"]
    e["open"] = e["Model accessibility"].str.contains("Open weights", na=False)
    # A model appears once per reasoning-effort config; keep its best.
    idx = e.groupby("Model name")["ECI Score"].idxmax()
    return e.loc[idx].sort_values("date").reset_index(drop=True)


def load_benchmark(stem: str) -> pd.DataFrame:
    """A benchmark CSV, with open/closed joined on from the ECI table."""
    score, name, _ = BENCHMARKS[stem]
    d = pd.read_csv(EPOCH / f"{stem}.csv")
    d["date"] = pd.to_datetime(d["Release date"], errors="coerce")
    d = d.dropna(subset=["date", score]).rename(columns={score: "score"})
    if d["score"].max() > 1.5:  # MMLU EM is 0-100, the rest are 0-1
        d["score"] /= 100.0

    acc = pd.read_csv(EPOCH / "epoch_capabilities_index.csv")[
        ["Model version", "Model accessibility", "Model name"]
    ].drop_duplicates("Model version")
    d = d.merge(acc, on="Model version", how="left")
    d["open"] = d["Model accessibility"].str.contains("Open weights", na=False)
    d["benchmark"] = name
    return d.sort_values("date")


def envelope(d: pd.DataFrame, x="date", y="score") -> pd.DataFrame:
    """Running best-so-far: the frontier."""
    d = d.sort_values(x)
    keep, best = [], -np.inf
    for _, r in d.iterrows():
        if r[y] > best:
            best = r[y]
            keep.append(r)
    return pd.DataFrame(keep)


def style_time_axis(ax, lo="2022-11-01", hi="2026-10-01") -> None:
    ax.set_xlim(pd.Timestamp(lo), pd.Timestamp(hi))
    ax.xaxis.set_major_locator(mpl.dates.YearLocator())
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonth=[4, 7, 10]))
    ax.grid(axis="both")
    ax.set_axisbelow(True)


# ---------------------------------------------------------------- figure 1
def fig_gpqa(plt) -> dict:
    """Adam Brown's plot, run forward to today. It ends in a wall."""
    d = load_benchmark("gpqa_diamond")
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    style_time_axis(ax)

    ax.axhline(0.25, color=MUTED, lw=1.0, ls=(0, (4, 3)))
    ax.annotate("random guessing (4-way multiple choice)", xy=(pd.Timestamp("2022-12-01"), 0.265),
                color=MUTED, fontsize=9)
    ax.axhline(0.697, color=INK, lw=1.2, ls=(0, (6, 3)))
    ax.annotate("PhD-level human experts, 69.7%", xy=(pd.Timestamp("2022-12-01"), 0.715),
                color=INK, fontsize=9, fontweight="bold")

    for is_open, colour, marker, label in [
        (False, CLOSED, "o", "closed weights"), (True, OPEN, "s", "open weights"),
    ]:
        s = d[d["open"] == is_open]
        ax.scatter(s["date"], s["score"], s=38, facecolor=colour, marker=marker,
                   alpha=0.55, edgecolor=SURFACE, linewidth=0.8, zorder=3, label=label)

    env = envelope(d)
    ax.plot(env["date"], env["score"], color=INK, lw=2.0, zorder=4)

    new = d[d["date"] >= THIS_WEEK_FROM]
    ax.scatter(new["date"], new["score"], s=80, facecolor="none", marker="o",
               edgecolor=HILITE, linewidth=2.2, zorder=5, label="released since June 2026")

    top = d.loc[d["score"].idxmax()]
    ax.annotate(f"best today: {top['score']:.1%}", xy=(top["date"], top["score"]),
                xytext=(pd.Timestamp("2025-06-01"), 1.02), color=INK, fontsize=9,
                fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))

    ax.set_ylim(0, 1.12)
    ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_ylabel("GPQA Diamond accuracy")
    ax.set_title("The benchmark Adam Brown showed — and why it is now useless",
                 loc="left", pad=26)
    ax.text(0.0, 1.028,
            '"GPQA is dead. It has once again suffered the fate of all benchmarks." — Adam Brown',
            transform=ax.transAxes, color=MUTED, fontsize=10, style="italic")
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig1_gpqa_dead.{ext}")
    plt.close(fig)
    return {"gpqa_top": float(d["score"].max()), "gpqa_top_model": top["Model version"]}


# ---------------------------------------------------------------- figure 2
def fig_ladder(plt) -> pd.DataFrame:
    """Every benchmark: born hard, dies easy. The ladder Brown walks up."""
    ramp = mpl.colors.LinearSegmentedColormap.from_list("tjo", ["#27CED7", "#1CADE4", "#2683C6", "#24476A"])
    stems = list(BENCHMARKS)
    colours = [ramp(i / (len(stems) - 1)) for i in range(len(stems))]

    fig, ax = plt.subplots(figsize=(9.4, 5.4))
    style_time_axis(ax, lo="2021-01-01")
    rows = []
    for stem, colour in zip(stems, colours):
        d = load_benchmark(stem)
        env = envelope(d)
        name = BENCHMARKS[stem][1]
        ax.plot(env["date"], env["score"], color=colour, lw=2.2, zorder=3)
        ax.scatter(env["date"], env["score"], s=16, color=colour, zorder=4)
        last = env.iloc[-1]
        ax.annotate(f"  {name}", xy=(last["date"], last["score"]), color=colour,
                    fontsize=9, fontweight="bold", va="center", ha="left")
        rows.append({
            "benchmark": name,
            "first_measured": env["date"].min().date(),
            "best_today": round(float(env["score"].max()), 3),
            "date_of_best": env["date"].max().date(),
            "dead": bool(env["score"].max() > 0.9),
        })

    ax.axhline(1.0, color=MUTED, lw=1.0)
    ax.annotate("100% — nothing left to measure", xy=(pd.Timestamp("2021-02-01"), 1.02),
                color=MUTED, fontsize=9)
    ax.set_ylim(0, 1.14)
    ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    ax.set_xlim(pd.Timestamp("2021-01-01"), pd.Timestamp("2027-06-01"))
    ax.set_ylabel("best score achieved by any model")
    ax.set_title("Each benchmark is built harder, and dies faster", loc="left", pad=26)
    ax.text(0.0, 1.028,
            "each new benchmark's curve is the last one shifted right — and only CritPt and HLE are still alive",
            transform=ax.transAxes, color=MUTED, fontsize=10, style="italic")
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig2_benchmark_ladder.{ext}")
    plt.close(fig)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- figure 3
def fig_eci(plt, eci: pd.DataFrame, lag: pd.DataFrame) -> dict:
    """The headline: a capability scale that cannot saturate."""
    fig, ax = plt.subplots(figsize=(10.6, 6.2))
    style_time_axis(ax, lo="2023-01-01", hi="2027-03-01")

    d = eci[eci["date"] >= pd.Timestamp("2023-01-01")]
    for is_open, colour, marker, label in [
        (False, CLOSED, "o", "closed weights (API only)"),
        (True, OPEN, "s", "open weights"),
    ]:
        s = d[d["open"] == is_open]
        ax.scatter(s["date"], s["ECI Score"], s=30, facecolor=colour, marker=marker,
                   alpha=0.45, edgecolor=SURFACE, linewidth=0.7, zorder=3, label=label)

    fc = envelope(d[~d["open"]], y="ECI Score")
    fo = envelope(d[d["open"]], y="ECI Score")
    ax.plot(fc["date"], fc["ECI Score"], color=CLOSED, lw=2.4, zorder=5)
    ax.plot(fo["date"], fo["ECI Score"], color=OPEN, lw=2.4, ls=(0, (5, 2)), zorder=5)

    # The trend claim is about the FRONTIER, so fit the frontier -- not the cloud
    # of all closed models, which is dragged down by small/cheap releases.
    x = mpl.dates.date2num(fc["date"])
    coef = np.polyfit(x, fc["ECI Score"], 1)
    xs = np.linspace(mpl.dates.date2num(pd.Timestamp("2023-01-01")),
                     mpl.dates.date2num(pd.Timestamp("2027-02-01")), 50)
    ax.plot(mpl.dates.num2date(xs), np.polyval(coef, xs), color=MUTED, lw=1.2,
            ls=(0, (2, 2)), zorder=2)
    per_year = coef[0] * 365.25

    # The open-weights lag, drawn as the horizontal distance it actually is.
    if len(lag):
        L = lag.iloc[-1]
        y = L["eci"]
        ax.annotate("", xy=(L["open_date"], y), xytext=(L["closed_first_reached"], y),
                    arrowprops=dict(arrowstyle="<->", color=INK, lw=1.4))
        mid = L["closed_first_reached"] + (L["open_date"] - L["closed_first_reached"]) / 2
        ax.annotate(f"open weights are {L['lag_days'] / 30.44:.1f} months behind",
                    xy=(mid, y), xytext=(mid, y - 9), color=INK, fontsize=9.5,
                    fontweight="bold", ha="center",
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))

    # Name EVERY release from the last five weeks -- the whole point of the plot.
    new = d[d["date"] >= THIS_WEEK_FROM].sort_values("ECI Score", ascending=False)
    ax.scatter(new["date"], new["ECI Score"], s=95, facecolor="none", marker="o",
               edgecolor=HILITE, linewidth=2.2, zorder=6,
               label=f"released since {THIS_WEEK_FROM:%d %b %Y}")
    # Label ladder: the releases are stacked within a few index points of each other,
    # so put the names in the right margin, evenly spaced, with leaders back to the dots.
    top, bot = new["ECI Score"].max() + 3.5, new["ECI Score"].min() - 5.0
    ys = np.linspace(top, bot, len(new))
    xlab = pd.Timestamp("2026-09-20")
    for (_, r), ylab in zip(new.iterrows(), ys):
        ax.annotate(r["Model name"], xy=(r["date"], r["ECI Score"]), xytext=(xlab, ylab),
                    fontsize=8.5, fontweight="bold", va="center", ha="left",
                    color=OPEN if r["open"] else INK,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7,
                                    shrinkA=0, shrinkB=4,
                                    connectionstyle="angle,angleA=0,angleB=90,rad=0"))

    # Released, but arriving faster than the evaluators can score them. We refuse to
    # guess a y-value for these: they get a rug mark at their release date instead.
    unscored = [("Muse Spark 1.1", "Meta", pd.Timestamp("2026-07-09"))]
    ylo = ax.get_ylim()[0]
    for label, org, when in unscored:
        ax.axvline(when, color=HILITE, lw=1.0, ls=(0, (2, 2)), alpha=0.8, zorder=2)
        ax.annotate(f"{label} ({org}) released —\nno independent score yet",
                    xy=(when, ylo + 2), xytext=(-8, 0), textcoords="offset points",
                    fontsize=8.5, color=HILITE, fontweight="bold", ha="right", va="bottom")

    ax.set_ylabel("Epoch Capabilities Index  (Elo-like: no ceiling)")
    ax.set_title("Capability is still a straight line — and it has no ceiling to hit",
                 loc="left", pad=26)
    ax.text(0.0, 1.028,
            f"all {len(d)} models released since 2023 · frontier gains {per_year:.1f} index points/year",
            transform=ax.transAxes, color=MUTED, fontsize=10, style="italic")
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig3_eci_frontier.{ext}")
    plt.close(fig)
    return {"eci_points_per_year": round(float(per_year), 2),
            "n_models_since_2023": int(len(d))}


# ---------------------------------------------------------------- figure 4
def fig_cadence(plt, eci: pd.DataFrame) -> dict:
    """Not just better. More often."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.0, 6.6), sharex=True)

    d = eci[eci["date"] >= pd.Timestamp("2022-07-01")]
    q = d.set_index("date").resample("QE").size()
    q = q[q.index <= pd.Timestamp("2026-06-30")]  # drop the partial quarter
    qo = d[d["open"]].set_index("date").resample("QE").size().reindex(q.index, fill_value=0)

    # Stacked: open drawn over the full-height bar, so the blue remainder is the closed count.
    ax1.bar(q.index, q.values, width=70, color=CLOSED, alpha=0.85,
            edgecolor=SURFACE, linewidth=2, label="closed weights")
    ax1.bar(q.index, qo.values, width=70, color=OPEN, alpha=0.95,
            edgecolor=SURFACE, linewidth=2, label="open weights")
    ax1.set_ylabel("models released per quarter")
    ax1.set_title("More capable — and arriving faster", loc="left", pad=26)
    ax1.text(0.0, 1.035,
             f"{q[q.index.year == 2023].mean():.0f} models per quarter in 2023  -->  "
             f"{q[q.index.year == 2026].mean():.0f} per quarter in 2026",
             transform=ax1.transAxes, color=MUTED, fontsize=10, style="italic")
    ax1.grid(axis="y")
    ax1.set_axisbelow(True)
    ax1.set_ylim(0, q.max() * 1.18)
    ax1.legend(frameon=False, fontsize=9, loc="upper left", ncol=2)

    # Interval between successive frontier records: is the frontier moving more often?
    fc = envelope(d[~d["open"]], y="ECI Score")
    gaps = fc["date"].diff().dt.days.dropna()
    # How often does the record actually fall? Counting records per half-year is
    # robust; the raw gap series has same-day ties (0 days) and one huge early gap.
    dates = fc["date"].iloc[1:]
    recent = gaps[dates.values >= np.datetime64("2025-07-01")]
    early = gaps[dates.values < np.datetime64("2024-07-01")]

    rec = fc.set_index("date").resample("2QE").size()
    rec = rec[rec.index <= pd.Timestamp("2026-06-30")]
    ax2.bar(rec.index, rec.values, width=140, color=HILITE, alpha=0.9,
            edgecolor=SURFACE, linewidth=2, zorder=3)
    for when, n in rec.items():
        if n:
            ax2.annotate(str(n), xy=(when, n), xytext=(0, 4), textcoords="offset points",
                         ha="center", color=INK, fontsize=9, fontweight="bold")
    ax2.set_ylabel("new best-ever models\nper half-year")
    ax2.set_ylim(0, rec.max() * 1.35)
    ax2.grid(axis="y")
    ax2.set_axisbelow(True)
    ax2.annotate(f"the record for 'best model ever built' now falls every {recent.median():.0f} days\n"
                 f"(median gap was {early.median():.0f} days before mid-2024)",
                 xy=(0.015, 0.93), xycoords="axes fraction", color=MUTED,
                 fontsize=9.5, va="top")
    style_time_axis(ax2, lo="2022-07-01", hi="2026-10-01")
    ax1.set_xlim(pd.Timestamp("2022-07-01"), pd.Timestamp("2026-10-01"))
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig4_cadence.{ext}")
    plt.close(fig)

    return {
        "median_days_between_records_before_jul2024": float(early.median()),
        "median_days_between_records_since_jul2025": float(recent.median()),
        "models_per_quarter_2023": float(q[q.index.year == 2023].mean()),
        "models_per_quarter_2026": float(q[q.index.year == 2026].mean()),
    }


# ---------------------------------------------------------------- figure 5
def compute_lag(eci: pd.DataFrame) -> pd.DataFrame:
    """How long until the closed frontier's capability shows up in open weights?

    For each open-weights record, find the date the CLOSED frontier first reached
    that same ECI. The gap is a horizontal lag in days -- the honest way to say
    "N months behind", because it is measured in the units the claim is made in.
    """
    fc = envelope(eci[~eci["open"]], y="ECI Score")
    fo = envelope(eci[eci["open"]], y="ECI Score")
    rows = []
    for _, r in fo.iterrows():
        earlier = fc[fc["ECI Score"] >= r["ECI Score"]]
        if len(earlier):
            first = earlier.iloc[0]
            rows.append({
                "open_date": r["date"], "open_model": r["Model name"],
                "eci": round(float(r["ECI Score"]), 2),
                "closed_first_reached": first["date"], "closed_model": first["Model name"],
                "lag_days": int((r["date"] - first["date"]).days),
            })
    return pd.DataFrame(rows)


def fig_lag(plt, lag: pd.DataFrame) -> dict:
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    months = lag["lag_days"] / 30.44

    ax.plot(lag["open_date"], months, color=OPEN, lw=2.0, zorder=3)
    ax.scatter(lag["open_date"], months, s=52, facecolor=OPEN, edgecolor=SURFACE,
               linewidth=1.0, zorder=4)
    med = float(months[lag["open_date"] >= pd.Timestamp("2025-01-01")].median())
    ax.axhline(med, color=INK, lw=1.4, ls=(0, (5, 3)), zorder=2)
    ax.annotate(f"median since 2025: {med:.1f} months",
                xy=(pd.Timestamp("2024-11-01"), med + 0.25), color=INK,
                fontsize=9.5, fontweight="bold")

    for _, r in lag.tail(4).iterrows():
        ax.annotate(r["open_model"], xy=(r["open_date"], r["lag_days"] / 30.44),
                    xytext=(0, 11), textcoords="offset points", fontsize=8.5,
                    color=INK, ha="center", fontweight="bold")

    ax.set_ylim(0, max(months) * 1.45)
    ax.set_ylabel("months behind the closed frontier")
    style_time_axis(ax, lo="2024-10-01", hi="2026-10-01")
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator(bymonth=[1, 7]))
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%b %Y"))
    ax.set_title("Open weights trail the frontier by about six months", loc="left", pad=26)
    ax.text(0.0, 1.028,
            "how long the closed frontier had already been at the level each new open model reaches",
            transform=ax.transAxes, color=MUTED, fontsize=10, style="italic")
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"fig5_open_weight_lag.{ext}")
    plt.close(fig)
    return {"median_lag_months_since_2025": round(med, 1),
            "latest_lag_months": round(float(months.iloc[-1]), 1),
            "latest_open_model": lag.iloc[-1]["open_model"]}


def main() -> None:
    import matplotlib.pyplot as plt

    FIG.mkdir(exist_ok=True)
    RESULTS.mkdir(exist_ok=True)

    eci = load_eci()
    lag = compute_lag(eci)

    stats = {"snapshot": SNAPSHOT, "n_models_total": int(len(eci))}
    stats |= fig_gpqa(plt)
    ladder = fig_ladder(plt)
    stats |= fig_eci(plt, eci, lag)
    stats |= fig_cadence(plt, eci)
    stats |= fig_lag(plt, lag)

    ladder.to_csv(RESULTS / "benchmark_ladder.csv", index=False)
    lag.to_csv(RESULTS / "open_weight_lag.csv", index=False)
    eci[["Model name", "date", "ECI Score", "Organization", "Model accessibility", "open"]] \
        .to_csv(RESULTS / "models_eci.csv", index=False)

    lines = ["# Model progress — key numbers", "",
             f"Source: Epoch AI Benchmarking Hub (CC-BY), snapshot {SNAPSHOT}. "
             f"{len(eci)} distinct models.", ""]
    for k, v in stats.items():
        lines.append(f"- **{k}**: {v}")
    lines += ["", "## Benchmark ladder (is it dead?)", "",
              ladder.to_markdown(index=False), "",
              "## Open-weights lag", "", lag.tail(8).to_markdown(index=False)]
    (RESULTS / "key_numbers.md").write_text("\n".join(lines) + "\n")

    print("\n".join(f"{k}: {v}" for k, v in stats.items()))
    print(f"\nfigures -> {FIG}")


if __name__ == "__main__":
    main()
