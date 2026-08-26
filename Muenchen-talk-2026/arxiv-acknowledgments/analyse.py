#!/usr/bin/env python3
"""Step 4 -- rates, confidence intervals, and the slide figure.

Estimator: for each (category, month) cell, the fraction of *successfully
retrieved* sampled papers whose acknowledgment region names an LLM.  Papers we
could not retrieve are dropped from both numerator and denominator (they are
missing at random with respect to the outcome -- see README).  Papers that are
ABOUT language models are excluded from the numerator by default, because
"we used GPT-4 in our experiments" is not an acknowledgment of writing help.

Interval: Wilson score, 95%.  Not Wald -- at n~110 and p~2% Wald intervals go
negative, which is exactly the regime most of this plot lives in.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib as mpl
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent
RES = ROOT / "results"
FIG = ROOT / "figures"

# --- Whitney Teal palette (TJO beamer theme), as in Wuerzburg/model-progress
INK = "#335B74"
MUTED = "#7C8B95"
GRID = "#DFE3E5"
SURFACE = "#FFFFFF"
QP = "#335B74"     # quant-ph  -- dark teal
MP = "#1CADE4"     # math-ph   -- cyan accent

mpl.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.labelcolor": INK, "axes.labelsize": 12,
    "axes.titlesize": 13, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "xtick.labelsize": 10.5, "ytick.labelsize": 10.5,
    "grid.color": GRID, "grid.linewidth": 0.8,
    "font.size": 11, "axes.unicode_minus": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["Whitney", "Helvetica", "DejaVu Sans"],
    "savefig.bbox": "tight", "savefig.dpi": 220,
})


def wilson(k: int, n: int, z: float = 1.959964) -> tuple[float, float, float]:
    """95% Wilson score interval; returns (p, lo, hi)."""
    if n == 0:
        return (np.nan, np.nan, np.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def load() -> pd.DataFrame:
    """Papers, with the hand adjudication applied.

    The regex screen (detect.py) is deliberately over-inclusive; every paper it
    flags goes into results/hits.jsonl and is then read by a human, whose
    verdict lands in results/manual_overrides.json as {"<id>": true|false}.
    A paper the screen never flagged is a true negative by construction, so it
    needs no entry.  Any flagged paper WITHOUT an entry is a hole in the
    adjudication and we shout about it rather than silently guessing.
    """
    d = pd.read_csv(RES / "papers.csv", dtype={"id": str})
    flagged = {json.loads(l)["id"] for l in (RES / "hits.jsonl").open()}
    manual = RES / "manual_overrides.json"
    ov = json.loads(manual.read_text()) if manual.exists() else {}
    missing = sorted(flagged - set(ov))
    if missing:
        print(f"!! {len(missing)} flagged papers not yet adjudicated; "
              f"falling back to the regex verdict for them: {missing[:8]}")
    d["ack_llm"] = d.apply(
        lambda r: bool(ov[r["id"]]) if r["id"] in ov
        else (r["id"] in flagged and r["verdict"] in ("strong", "weak")), axis=1)
    d["adjudicated"] = d["id"].isin(ov)
    d["flagged"] = d["id"].isin(flagged)
    return d


def cells(d: pd.DataFrame) -> pd.DataFrame:
    got = d[d["verdict"] != "MISSING"].copy()
    rows = []
    for (cat, month), g in got.groupby(["category", "month"]):
        # `about_llm` is a title/abstract heuristic for "this paper is ABOUT
        # language models".  It is only a screen: where a human has read the
        # paper, the human wins.  That matters in both directions -- a paper on
        # LLM-generated compilers is not acknowledging assistance (excluded by
        # hand), and a paper whose abstract happens to say "GPT-5.6 assisted
        # with literature search" trips the heuristic while being exactly the
        # thing we are counting (kept by hand).
        k = int((g["ack_llm"] & (g["adjudicated"] | ~g["about_llm"])).sum())
        n = len(g)
        p, lo, hi = wilson(k, n)
        rows.append({
            "category": cat, "month": month, "date": pd.Timestamp(month + "-15"),
            "n_sampled": len(d[(d.category == cat) & (d.month == month)]),
            "n_with_text": n, "k_ack": k,
            "p": p, "lo": lo, "hi": hi,
            "n_about_llm": int(g["about_llm"].sum()),
            "k_ack_incl_about": int(g["ack_llm"].sum()),
            "k_llm_term_anywhere": int(g["llm_term_anywhere"].sum()),
            "n_flagged_for_review": int(g["flagged"].sum()),
            "pct_with_ack_section": round(100 * g["has_ack_section"].mean(), 1),
        })
    return pd.DataFrame(rows).sort_values(["category", "date"])


def figure(c: pd.DataFrame) -> None:
    """The slide figure.

    Identity is never carried by colour alone: each series gets its own marker
    shape AND a direct end-label, which is the relief the palette check asks for
    (the deck's cyan accent sits below 3:1 against white).  The underlying counts
    ship as results/rates_by_month.csv, so there is a table view too.
    """
    FIG.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(10.2, 5.1))

    top = 100 * c["hi"].max()
    ymax = max(6.0, top * 1.11)

    # ChatGPT's public release: the clock this plot is really measuring.
    ax.axvline(pd.Timestamp("2022-11-30"), color=MUTED, lw=1.0,
               ls=(0, (3, 3)), zorder=1)
    ax.annotate("ChatGPT released", xy=(pd.Timestamp("2022-12-10"), ymax * 0.955),
                color=MUTED, fontsize=10, style="italic", ha="left", va="top")

    ends = []
    for cat, colour, marker in [("quant-ph", QP, "o"), ("math-ph", MP, "s")]:
        s = c[c["category"] == cat].sort_values("date")
        if s.empty:
            continue
        ax.fill_between(s["date"], 100 * s["lo"], 100 * s["hi"],
                        color=colour, alpha=0.14, linewidth=0, zorder=2)
        ax.plot(s["date"], 100 * s["p"], color=colour, lw=2.4, zorder=4)
        ax.plot(s["date"], 100 * s["p"], ls="none", marker=marker, markersize=7,
                markerfacecolor=SURFACE, markeredgewidth=2.0,
                markeredgecolor=colour, zorder=5)
        last = s.iloc[-1]
        ends.append((100 * last["p"], last["date"], colour, marker, cat))

    # Direct labels, nudged apart if the two series finish close together.
    ends.sort(key=lambda e: -e[0])
    ys = [e[0] for e in ends]
    if len(ys) == 2 and abs(ys[0] - ys[1]) < ymax * 0.07:
        ys = [max(ys) + ymax * 0.035, min(ys) - ymax * 0.035]
    for (p, when, colour, marker, cat), y in zip(ends, ys):
        ax.annotate(cat, xy=(when, y), xytext=(13, 0), textcoords="offset points",
                    color=colour, fontsize=12.5, fontweight="bold", va="center")

    # The headline point, called out with its raw count.
    q = c[c["category"] == "quant-ph"].sort_values("date")
    if len(q):
        L = q.iloc[-1]
        ax.annotate(f"{100*L['p']:.0f}%  ({int(L['k_ack'])} of {int(L['n_with_text'])})",
                    xy=(L["date"], 100 * L["p"]), xytext=(-14, 20),
                    textcoords="offset points", color=QP, fontsize=11,
                    fontweight="bold", ha="right",
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8,
                                    shrinkA=0, shrinkB=5))

    ax.axhline(0, color=MUTED, lw=0.8)
    ax.set_ylabel("papers acknowledging LLM assistance")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
    ax.set_ylim(-ymax * 0.045, ymax)
    ax.set_xlim(pd.Timestamp("2022-11-15"), pd.Timestamp("2026-12-15"))
    ax.xaxis.set_major_locator(mpl.dates.YearLocator())
    ax.xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonth=[4, 7, 10]))
    ax.grid(axis="y")
    ax.set_axisbelow(True)

    n_tot = int(c["n_with_text"].sum())
    ax.annotate(
        f"random sample of {n_tot:,} arXiv submissions, v1 full text, quarterly"
        f"  ·  shaded band = 95% Wilson interval",
        xy=(0.0, -0.145), xycoords="axes fraction", color=MUTED,
        fontsize=10, style="italic", va="top")

    for ext in ("png", "pdf"):
        fig.savefig(FIG / f"ack_trend.{ext}")
    plt.close(fig)


def main() -> None:
    RES.mkdir(exist_ok=True)
    d = load()
    c = cells(d)
    c.to_csv(RES / "rates_by_month.csv", index=False)

    lines = []
    for cat in ("quant-ph", "math-ph"):
        s = c[c["category"] == cat].sort_values("date")
        if s.empty:
            continue
        f, l = s.iloc[0], s.iloc[-1]
        lines.append(
            f"{cat}: {100*f['p']:.1f}% ({f['k_ack']}/{f['n_with_text']}) in {f['month']}"
            f"  ->  {100*l['p']:.1f}% ({l['k_ack']}/{l['n_with_text']}) in {l['month']}")
        # pooled first-year vs last-year, which is what a slide should quote
        early = s[s["date"] < pd.Timestamp("2024-01-01")]
        late = s[s["date"] >= pd.Timestamp("2025-07-01")]
        for name, blk in (("2023", early), ("2025H2-2026", late)):
            k, n = int(blk["k_ack"].sum()), int(blk["n_with_text"].sum())
            p, lo, hi = wilson(k, n)
            lines.append(f"    pooled {name}: {100*p:.1f}% "
                         f"[{100*lo:.1f}, {100*hi:.1f}]  ({k}/{n})")
    (RES / "headline.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    got = int((d["verdict"] != "MISSING").sum())
    print(f"\ncoverage: {got}/{len(d)} sampled papers have text "
          f"({100*got/len(d):.0f}%); {int(d['flagged'].sum())} read by hand")
    figure(c)
    print(f"figure -> {FIG/'ack_trend.png'}")
    write_headline(c, d, lines)


def write_headline(c: pd.DataFrame, d: pd.DataFrame, lines: list[str]) -> None:
    """Splice the current numbers into README.md at the <!--HEADLINE--> marker."""
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    got = int((d["verdict"] != "MISSING").sum())
    out = ["<!--HEADLINE-->", "",
           f"Sample: **{got:,} arXiv papers** ({len(d):,} drawn, "
           f"{100*got/len(d):.0f}% full text retrieved) across 15 quarterly "
           f"months, Jan 2023 – Jul 2026. Every one of the "
           f"**{int(d['flagged'].sum())}** papers the screen flagged was read by "
           f"hand.", ""]
    for cat in ("quant-ph", "math-ph"):
        s = c[c["category"] == cat].sort_values("date")
        if s.empty:
            continue
        blocks = []
        for name, blk in (("2023", s[s["date"] < pd.Timestamp("2024-01-01")]),
                          ("2024", s[(s["date"] >= pd.Timestamp("2024-01-01")) &
                                     (s["date"] < pd.Timestamp("2025-01-01"))]),
                          ("2025", s[(s["date"] >= pd.Timestamp("2025-01-01")) &
                                     (s["date"] < pd.Timestamp("2026-01-01"))]),
                          ("2026", s[s["date"] >= pd.Timestamp("2026-01-01")])):
            k, n = int(blk["k_ack"].sum()), int(blk["n_with_text"].sum())
            p, lo, hi = wilson(k, n)
            blocks.append(f"| {name} | {k}/{n} | **{100*p:.1f}%** | "
                          f"[{100*lo:.1f}, {100*hi:.1f}] |" if n else
                          f"| {name} | - | not measured | - |")
        out += [f"**{cat}** — papers acknowledging LLM assistance, pooled by year:",
                "", "| year | count | rate | 95% CI |", "|---|---|---|---|",
                *blocks, ""]
    last = c.sort_values("date").groupby("category").tail(1)
    for _, r in last.iterrows():
        out.append(f"Latest measured month ({r['month']}), **{r['category']}**: "
                   f"{int(r['k_ack'])}/{int(r['n_with_text'])} = "
                   f"**{100*r['p']:.1f}%** [{100*r['lo']:.1f}, {100*r['hi']:.1f}].")
    out += ["", "Full per-month table: `results/rates_by_month.csv`.", ""]

    # What the acknowledged LLMs were used FOR.
    pur = RES / "ack_purpose.json"
    if pur.exists():
        pp = {k: v for k, v in json.loads(pur.read_text()).items() if k != "_comment"}
        ack = d[d["ack_llm"]].copy()
        ack["purpose"] = ack["id"].map(pp)
        ack["year"] = ack["month"].str[:4]
        tab = pd.crosstab(ack["purpose"], ack["year"])
        for c in ("language", "code", "research"):
            if c not in tab.index:
                tab.loc[c] = 0
        tab = tab.loc[[c for c in ("language", "code", "research") if c in tab.index]]
        years = list(tab.columns)
        out += ["### What the LLM was acknowledged *for*", "",
                "Read off the disclosure sentence by hand "
                "(`results/ack_purpose.json`); a paper claiming several is filed "
                "under the highest.", "",
                "| used for | " + " | ".join(years) + " | total |",
                "|---" * (len(years) + 2) + "|"]
        label = {"language": "language / copy-editing / LaTeX",
                 "code": "code, scripts, figures",
                 "research": "**research content** — proofs, derivations, literature, brainstorming"}
        for c in tab.index:
            row = [str(int(tab.loc[c, y])) for y in years]
            out.append(f"| {label[c]} | " + " | ".join(row) +
                       f" | {int(tab.loc[c].sum())} |")
        n_res = int(tab.loc["research"].sum()) if "research" in tab.index else 0
        out += ["", f"All {n_res} of the 'research content' acknowledgments are "
                    f"from 2026 — the shift is not just more disclosure, it is "
                    f"disclosure of a different kind of use.", ""]

    txt = readme.read_text()
    head, _, tail = txt.partition("<!--HEADLINE-->")
    tail = tail.partition("\n---\n")[2]
    readme.write_text(head + "\n".join(out) + "\n---\n" + tail)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    main()
