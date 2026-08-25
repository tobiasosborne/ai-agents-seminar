# Four timeline slides — design specification

**Talk:** *Large Language Models: A Physicist's Perspective*, MCQST München, 27 August 2026.
**Author of this spec:** slide-design pass, 24 Aug 2026.
**Deliverables in this directory:** `timeline-slides-design.md` (this file), `mockup.html`
(visual ground truth), `renders/g1.png … g4.png` (1280×720 renders of the mockup, verified).

**Implementers:** everything below is specified in a **1280 × 720 design frame**. Both media
must reproduce the same geometry. Do not re-invent the layout from the prose — open
`mockup.html` (or the four PNGs) and match it.

---

## 0. Errata — fix before implementing

**Hook B caption is wrong.** The caption on the second press-screenshot hook slide calls
arXiv:2602.12176 a *"string theory paper"* (`slides/talk.tex` line 69 comment;
`slides-web/talk.html` line 439 comment and the caption at line 443).

It is **not** string theory. The paper is *"Single-minus gluon tree amplitudes are nonzero"*
— a tree-level **gauge-theory scattering-amplitudes** result. Authors: Guevara (Harvard),
Lupsasca (Vanderbilt), Skinner (Cambridge), Strominger (Harvard), Weil (OpenAI). Strominger
and Skinner on the author list is presumably where "string theory" came from.

Replace with **"gauge-theory scattering amplitudes"** or **"a new result in theoretical
physics"**. Suggested corrected caption (keeps the existing shape):

> arXiv:2602.12176 · Harvard, Vanderbilt, Cambridge, OpenAI · February 2026
> gauge-theory scattering amplitudes — GPT-5.2 conjectured the closed form and proved it

Note the institution list in the HTML caption also says "IAS" — no IAS author is on the
paper; drop it. Source: `research/llm-proof-results.md` (master table, Feb 2026 row) and
`research/grief-timeline.md` §6.

G3 below uses the corrected wording ("Gauge-theory amplitudes"), so the two slides will
agree once the hook caption is fixed.

---

## 1. Shared conventions

### 1.1 Coordinate system

All coordinates in this document are **pixels in a 1280 × 720 frame, origin top-left**.

| target | conversion |
|---|---|
| HTML deck (`#stage`, `container-type:size`) | `x_cqw = px/12.8`, `y_cqh = px/7.2` — or just use `px` inside a `position:relative` box of `width:100cqw;height:100cqh` and scale with a wrapper. Prefer **cqh/cqw** so it survives resizing. |
| LuaLaTeX/beamer (`aspectratio=169` ⇒ paper is exactly 16 cm × 9 cm) | `\begin{tikzpicture}[remember picture, overlay]` anchored at `current page.north west`; design point `(x, y)` ⇒ TikZ `([xshift=x/80 cm, yshift=-y/80 cm]current page.north west)`. **1 design px = 0.0125 cm.** |

### 1.2 Type scale — **read this, it is the one real trap**

The beamer deck and the HTML deck currently run at *different absolute type scales*
(beamer `normal text` is `\large` = 17 pt on a 16 cm page ≈ 48 design px; the HTML deck's
body `p` is 3.15 cqh ≈ 23 design px). These four slides are **figure slides**: the beamer
implementation must therefore set **explicit `\fontsize{}{}` inside the TikZ nodes** and
must not inherit `\large`, or nothing will fit.

Conversion: **beamer pt = design px × 0.3543**.

| role | design px | cqh (HTML) | beamer `\fontsize` |
|---|---|---|---|
| frame title | 32 | 4.44 | `\fontsize{11.3}{13}` |
| G4 payload line | 33 | 4.58 | `\fontsize{11.7}{14}` |
| G4 chip number | 37 | 5.14 | `\fontsize{13.1}{15}` |
| G3 verbatim quote (mono) | 22.5 | 3.13 | `\fontsize{8}{10}` (`\ttfamily`) |
| G2/G3 closing / summary | 22–24 | 3.06–3.33 | `\fontsize{8}{10}` |
| G4 sub-payload "Aim there." | 23 | 3.19 | `\fontsize{8.1}{10}` |
| **event / body text** | 15.5–16 | 2.15–2.22 | `\fontsize{5.6}{7}` |
| dates, lane labels, pill text | 15 | 2.08 | `\fontsize{5.3}{6.6}` |
| offset labels, tier legend | 14–14.5 | 1.94–2.01 | `\fontsize{5.1}{6.4}` |
| axis furniture, honesty notes, attributions | 13 | 1.81 | `\fontsize{4.6}{5.8}` |

The 13 px tier is **deliberately below the brief's 2.0 cqh floor**. Only four kinds of thing
live there — year labels on an axis, the grief-stage honesty footnote, source attributions,
and the arXiv caption. None of them needs back-row legibility; they are there so the slide is
honest and so the front rows can check. Everything the audience must actually *read from the
back* is ≥ 15 px / 2.08 cqh.

If the projected result is judged too small in the hall, **do not shrink margins — cut items**,
using the per-slide cut order below, and scale the remaining type up by the freed fraction.

### 1.3 Colour roles

Palette is unchanged (`beamercolorthemeTJO.sty` / the HTML `:root` block). New roles:

| role | hex | used for |
|---|---|---|
| `darkteal` | `#335B74` | titles, structure, the "measured" capability line, G2 maths-lane dates |
| `cyan` | `#1CADE4` | title rules, "you are here", extrapolation, big numbers |
| `medblue` | `#2683C6` | tier T2 badge; grief stage *bargaining* |
| `green` | `#42BA97` | tier T1 badge; grief stage *acceptance* |
| `red` | `#a33` (`red!70!black`) | tier T3 badge; grief stage *anger*; the words "zero referees". **Nowhere else.** |
| `lightgrey` | `#DFE3E5` | spines, rules, lane separators |
| `rule` | `#C7CFD3` | dashed year separators, chevrons |
| `muted` | `#5b6b74` | secondary text |
| `faint` | `#8a969c` | axis furniture, honesty notes |
| `codebg` | `#F0F2F3` | the Jacobian quote box |

**The five-stage grief ramp** (G1 only, echoed nowhere else — this is deliberate; see §2.5):

| stage | hex | rationale |
|---|---|---|
| shock | `#1CADE4` cyan | the bright jolt |
| anger | `#a33` red | the one sanctioned use of red |
| bargaining | `#2683C6` medblue | |
| depression | `#335B74` darkteal | deep, heavy |
| acceptance | `#42BA97` green | resolution |

### 1.4 Slide chrome (all four)

* Frame title: 32 px, `darkteal`, weight 650, at **(40, 38)**.
* Title rule: 66 × 4 px `cyan`, radius 2, at **(40, 94)**.
* Right kicker (G1, G2) or left subtitle (G4): 15–16 px `muted`.
* Slide padding for these four slides is **reduced to ~40 px** (≈ 3.1 cqw), not the deck's
  usual 8 cqw. They are figure slides; the figure needs the width.

### 1.5 Deck positions

| slide | where |
|---|---|
| **G3** | Part 1 — immediately after Hook B (the amplitudes press screenshot), before *"A control experiment, run on us"* (`talk.tex` ≈ line 84) |
| **G1** | Part 1 — immediately after *"Four moments"* (`talk.tex` ≈ line 199), before the `\statementslide{LLMs are incredibly capable…}` |
| **G2** | immediately after G1 |
| **G4** | closing — immediately before the *"slop cannon is charged"* statement slide (`talk.tex` ≈ line 1369) |

---

## 2. G1 — The five stages of AI grief

### 2.1 Title and chrome

* **Title:** `The five stages of AI grief`
* **Kicker** (right-aligned at x = 1240, y = 60, 16 px muted, two lines):
  `software engineering` / `Nov 2022 → Jul 2026`

### 2.2 Exact content — 10 events

Alternating lanes above/below one spine. Rank = chronological order; ranks 1,3,5,7,9 go
**above**, ranks 2,4,6,8,10 go **below**.

| rank | lane | tick x | date (in stage colour) | line (verbatim) | stage |
|---|---|---|---|---|---|
| 1 | up | 128 | **Nov 2022** | ChatGPT launches — everyone can try it | shock |
| 2 | down | 242 | **Feb 2024** | Huang: "nobody should learn to code" | anger |
| 3 | up | 356 | **Mar 2024** | Devin — "the first AI software engineer" | anger |
| 4 | down | 470 | **Apr 2024** | Devin debunked — fails 85% of tasks | bargaining |
| 5 | up | 584 | **Feb 2025** | Claude Code ships; Karpathy: "vibe coding" | shock |
| 6 | down | 698 | **Mar 2025** | Amodei: "90% of code in six months" | anger |
| 7 | up | 812 | **Jul 2025** | METR trial: experienced devs 19% slower | bargaining |
| 8 | down | 926 | **Dec 2025** | Stack Overflow questions −78% in a year | depression |
| 9 | up | 1040 | **Feb 2026** | METR retires it — no counterfactual left | acceptance |
| 10 | down | 1154 | **Jul 2026** | Review time +441%; hiring returns, bifurcated | acceptance |

Other text on the slide, verbatim:

* METR callout, two lines centred at x = 926: `19 months of comfort —` (13.5 px muted) /
  **`retired by its own authors`** (15.5 px, darkteal, bold)
* Year labels under the spine, 13 px faint: `2022–23` (x≈114), `2024` (x≈290),
  `2025` (x≈755), `2026` (x≈1110)
* Rail lead-in at (60, 530), 13 px muted, letter-spaced: `reading the colours —`
* Five stage pills, uppercase, letter-spacing .13em: `SHOCK` `ANGER` `BARGAINING`
  `DEPRESSION` `ACCEPTANCE`
* Honesty footnote, centred at y = 626, 13 px faint italic:
  `The stages overlap and run concurrently — the colour marks the dominant public register, not anyone's actual mood.`

### 2.3 Geometry

```
spine            y = 366, x 44 → 1236, 3 px, lightgrey
dots             r = 6.5 at (tick x, 366), filled in the event's stage colour,
                 3 px white ring (draw white circle r=8 underneath)
upper stems      (x, 334) → (x, 366), 1.6 px, stage colour
lower stems      (x, 366) → (x, 398), 1.6 px, stage colour
upper text block left = tick x − 104, top = 266, width = 208, centre-aligned
lower text block left = tick x − 104, top = 400, width = 208, centre-aligned
   date line     15 px bold, stage colour, 4 px below-margin
   event line    16 px, ink #1a1e21, line-height 1.3, wraps to exactly 2 lines
year separators  dashed 1.4 px #C7CFD3, x = 185, 527, 983, from y 344 → 390
METR arc         quadratic: M(812,250) Q(926,198) → (1038,244); 2.2 px darkteal,
                 dash 6/5; arrowhead triangle (1040,254)(1029,240)(1043,236)
METR label       centred x 926: line 1 baseline ≈ y 170, line 2 ≈ y 192
stage rail       5 pills, y 556, height 46, width 208, gap 30,
                 lefts = 60, 298, 536, 774, 1012; radius 10;
                 border 1.6 px stage colour; fill = stage colour at 9–13 % alpha;
                 text 15 px bold in stage colour
chevrons "›"     20 px #C7CFD3 at x = 277, 515, 753, 991, y ≈ 576
```

### 2.4 Build / reveal order (HTML `.build` steps; beamer `\onslide<n->`)

| step | reveals |
|---|---|
| 0 (always) | title, kicker, spine, year separators, year labels, rail lead-in, the five pills **in grey outline** (border `#C7CFD3`, text `#8a969c`, no fill) |
| 1 | events 1–3 (Nov 2022, Feb 2024, Mar 2024) + **activate** the SHOCK and ANGER pills |
| 2 | events 4–6 (Apr 2024, Feb 2025, Mar 2025) + **activate** BARGAINING |
| 3 | event 7 (Jul 2025, METR) — alone. This is "the great comfort" |
| 4 | events 8–9 + the METR arc and its label + **activate** DEPRESSION and ACCEPTANCE |
| 5 | event 10 + the honesty footnote |

"Activate" = swap the grey pill for the coloured one. In beamer:
`\only<1-1>{grey node}\only<2->{coloured node}` at identical coordinates. If that is too
fiddly, the **fallback** is: pills appear fully coloured at step 5. State it as a fallback,
not the default — the progressive rail is the slide's payoff.

### 2.5 Content decisions (and why)

* **Dropped from research §5 Slide A:** *May 2025 Klarna rehires* (customer service, not
  software engineering — weakest link to the arc) and *Nov 2025 Opus 4.5 past 80% SWE-bench*
  (already carried by the preceding "Four moments" slide, moment 3).
* **Added, not in §5 Slide A:** *Dec 2025 Stack Overflow −78%*. Without it the **depression**
  stage has no event and the five-pill rail is a lie. It is also, per the research file, "the
  most legible single number in the whole disruption".
* **Merged:** §5's two 2026 closing rows ("Review time +441%, throughput +34%" and "Hiring
  returns, bifurcated") into one line. Both mechanism and landing, one item.
* **Background stage *zones* rejected in favour of coloured dates + a legend rail.** The
  grief stages are not monotone in time (Amodei's Mar 2025 anger sits *after* Apr 2024's
  bargaining), so hard background bands would have been a false claim, and the bands would
  have been of wildly unequal width and unlabellable. Colouring the **date** by stage puts
  the stage information where it is most legible, and the non-monotonicity becomes visible
  and speakable ("notice the red dot after the blue one").
* **Feb 2025 is coloured *shock*, not "the turn".** Deliberate: the second cyan dot is the
  real shock. Worth a sentence from the podium.
* Ticks are **evenly spaced (ordinal), not to scale.** True chronological spacing puts
  Feb/Mar/Apr 2024 within 30 px of each other and is unusable. Every item is dated and year
  separators mark the real boundaries, so nothing is misrepresented.

### 2.6 Cut first, in this order

1. Merge ranks 3 + 4 into one lower-lane item:
   **Mar 2024** · `Devin, "the first AI software engineer" — debunked in a month` → 9 items.
2. Drop rank 1 (Nov 2022 ChatGPT) — the preceding "Four moments" slide already carries it →
   8 items, and the ranks re-space to 145 px, allowing type up ~15 %.
3. Drop rank 6 (Mar 2025 Amodei) — the quote survives in the speaker's narration.

---

## 3. G2 — Mathematics is eighteen months behind

### 3.1 Title and chrome

* **Title:** `Mathematics is eighteen months behind`
  (Alternate if the exactness bothers you: *"The same arc, one field later"*. Keep the
  eighteen-months version — it is memorable, and the kicker plus the closing line supply the
  correction.)
* **Kicker** (right, y = 60, 16 px muted, two lines):
  `the same arc, one field later` / `2021 → 2026`

### 3.2 Exact content — 6 paired beats

Six columns; centres at **x = 140, 340, 540, 740, 940, 1140**; cell width 184, left =
centre − 92.

| col | SWE lane (upper) | offset label | Maths/physics lane (lower) |
|---|---|---|---|
| 1 | **Jun 2021** · Copilot: a machine / writes plausible code | `37 months` | **Jul 2024** · IMO silver: AlphaProof |
| 2 | **Nov 2022** · ChatGPT: / everyone tries it | `32 months` | **Jul 2025** · IMO gold, in natural / language |
| 3 | **Mar 2024** · Devin hyped, / then debunked | `19 months` | **Oct 2025** · "Ten Erdős problems" / — retracted |
| 4 | **Feb 2025** · Claude Code: / the tooling loop closes | `11 months` | **Jan 2026** · Erdős #728: / model → Lean → human |
| 5 | **Q2 2025** · "Better than I expected / — at my job" | `12 months` | **May 2026** · Unit distance falls; Gowers: / "Annals, no hesitation" |
| 6 | **Nov 2025** · Opus 4.5 first past / 80% SWE-bench | `9 months` | **Aug 2026** · Astra: ten decade-open / problems, $2k each |

`/` marks a **hard line break** — set them explicitly (`<br>` / `\\`). Left to auto-wrap
these produce single-word orphan lines.

Other text, verbatim:

* Lane labels, 14 px darkteal bold, uppercase, letter-spacing .19em, at x = 40:
  `SOFTWARE ENGINEERING` (y ≈ 118) and `MATHEMATICS & THEORETICAL PHYSICS` (y ≈ 356)
* Badge: **`You are here`** (white on cyan) with sub-line
  `27 August 2026 — this room` (13.5 px darkteal bold)
* Closing line 1, centred y = 600, 22 px darkteal bold:
  `Offset ~3 years in 2024 · ~9 months now · closing at about a year per year`
* Closing line 2, centred y = 636, 18 px muted:
  `Mathematics never had to build the tooling. It inherited the one built for code — and Lean is code.`

### 3.3 Geometry

```
column highlight  rounded rect (1032, 146) 216 × 346, radius 12, fill cyan @ 7 %
                  — spans BOTH lanes of column 6; drawn first, behind everything
lane A label      x 40, y 118        lane A rule  y 140, x 40 → 1240, 1.5 px lightgrey
lane A cells      top 154   (date 15 px muted-bold; text 15.5 px, colour #4a575e)
offset labels     top 244, 14 px bold muted, centred on each column
converging wedge  filled polygon, centre-line y = 310, half-heights = 29, 26, 15.4,
                  8.9, 9.75, 7.3 px (∝ 37 : 32 : 19 : 11 : 12 : 9), extended flat to
                  x = 40 and x = 1240.  Fill darkteal @ 16 %, stroke darkteal 1.2 px @ 55 %.
                  Exact path in mockup.html.
lane C label      x 40, y 356        lane C rule  y 378
lane C cells      top 394   (date 15 px darkteal bold — col 6's date is CYAN;
                            text 15.5 px full ink)
you-are-here      pill (1040, 506) 200 × 44, radius 10, cyan fill, 17 px white bold,
                  letter-spacing .11em; up-pointing triangle (1140,494)(1132,506)(1148,506)
                  sub-line centred at y 558
```

**The SWE lane is deliberately recessive** (muted dates, text `#4a575e`); the maths lane is
full ink; column 6's maths date is cyan. That is the whole "you are here" reading, done with
colour weight before the badge is even shown.

### 3.4 Build / reveal order

| step | reveals |
|---|---|
| 0 | title, kicker, both lane labels + rules |
| 1 | all six SWE cells — *"here is the arc you already know"* |
| 2 | maths cells 1–3 |
| 3 | maths cells 4–6 + the column-6 highlight |
| 4 | offset labels + the converging wedge |
| 5 | "You are here" badge + sub-line |
| 6 | closing lines 1 and 2 |

Steps 2 and 3 may be merged into one if the talk is running long (→ 5 steps).

### 3.5 Content decisions (and why)

* **The lanes are ordinal beats, not two time axes.** Research §3's pairing table is not
  monotone in both fields simultaneously (Amodei Mar 2025 ↔ Astra Aug 2026 crosses three
  other pairs), so straight connectors between two real time axes would produce a tangle.
  Six numbered beats + a numeric offset per beat removes the problem *and* makes the
  convergence quantitative rather than merely suggested.
* **Astra is paired with Opus 4.5 crossing 80 % SWE-bench (Nov 2025), not with Amodei's
  "90 % of code" (Mar 2025)** as in §5 Slide B. Reasons: (a) Astra is a *capability
  threshold*, not a proclamation, so the analogy is truer; (b) it makes the pairing
  chronologically monotone; (c) the resulting offset is **9 months**, which is exactly the
  number in the closing line. Flag if the talk-owner disagrees — it is the one substantive
  re-pairing.
* **Merged** §5's Devin-hype and Devin-debunk rows into one beat (they share a maths
  analogue: the same Weil claim, made and retracted in the same month).
* **Dropped** four §5 pairs to reach six: METR ↔ Tao "speed not difficulty" (duplicates G1's
  hinge); Stack Overflow ↔ arXiv bans; bottleneck-to-review ↔ Tao's digestion; job-redefined
  ↔ Tao's five stages. The last two are carried later in the deck by the Tao material.
* **No grief-stage colouring on this slide.** Reusing G1's five-colour ramp here was tried
  and rejected: the stage of a *beat* differs between the two fields, so a shared column
  colour would be wrong and a per-cell colour would produce 12 coloured dates and visual
  noise. Lane weight does the job instead.
* The wedge has one honest **bump** (11 → 12 months, cols 4 → 5). Leave it. A perfectly
  monotone curve would be a fabrication and this audience will notice either way.

### 3.6 Cut first, in this order

1. Drop column 5 (Q2 2025 "better than I expected" ↔ May 2026 unit distance). The SWE side
   is undated and subjective; the maths side already appears as Hook A. → 5 columns, cells
   widen to 224 px.
2. Drop column 2 (ChatGPT ↔ IMO gold) — duplicates column 1's flavour (second medal, second
   "everyone can try it"). → 4 columns.
3. Drop closing line 2 and put it in the speaker's mouth.

---

## 4. G3 — The flurry, and how much of it is checked

### 4.1 Title and chrome

* **Title:** `The flurry — and how much of it is checked`
* No kicker; the tier legend occupies that row.

### 4.2 Exact content

**Tier legend**, one row at y = 110, three groups, 14.5 px muted, badges 58 × 22:

| badge | text |
|---|---|
| `T1` (green) | machine-checked or officially graded |
| `T2` (medblue) | arXiv — named humans read it |
| `T3` (red) | announced only, no referee |

**The eight items**, one row each, 43 px pitch, first row top y = 150:

| badge | date | line (verbatim) |
|---|---|---|
| `T1` | Jul 2025 | IMO gold, in natural language, officially graded |
| `T1` | Jan 2026 | Erdős #728 — first autonomous solve, with a Lean certificate |
| `T2` | Feb 2026 | Gauge-theory amplitudes — GPT-5.2 and five named physicists |
| `T2` | Mar 2026 | Bethe ansatz, two new integrable chains — checked vs exact diagonalisation |
| `T2` | May 2026 | Unit distance disproved — nine mathematicians read it line by line |
| `T1` | May 2026 | AlphaProof Nexus: 9 Erdős + 44 OEIS, Lean, a few hundred $ each |
| `T3` | Jul 2026 | Jacobian conjecture false in dim ≥ 3 — announced in one post on X |
| `T1*` | Aug 2026 | "Astra": ten decade-open problems, Lean, < $2k each — **zero referees** |

Rows 3 and 4 are the **physics rows**: light cyan fill `#F2FAFE`, 3 px cyan left edge, and
the tag `PHYSICS` (12 px cyan, uppercase, letter-spacing .16em) right-aligned at x = 836 on
row 3. This is an MCQST audience; make the two rows that are *their* field impossible to miss.

`zero referees` is `#a33` and bold — the only red text on the slide besides the T3 badge.
The `T1*` badge is green (the certificates are real) with the asterisk cashed out by
"zero referees" in the line.

**The Jacobian quote box** — the slide's best object, give it its own frame:

```
"hello there the jacobian conjecture is false thanx"
the entire public announcement, 20 Jul 2026 — an 87-year-old conjecture, checked by hand within days
```
Quote in **monospace**, 22.5 px, darkteal, weight 600. Caption 13.2 px muted.

**Right column — "…and the denominator"** (verbatim):

* Header: `…and the denominator` (19 px darkteal bold)
* Sub: `The community's own tracker marks every AI contribution:` (14 px muted)
* Four marker rows, 14.5 px, 15 px circles:
  * green filled — `full resolution`
  * half-filled green (left half green, right half white, 1.6 px green ring) — `partial progress`
  * red filled — **`incorrect work`** (bold)
  * white with 2 px grey ring — **`unverified — never read`** (bold)
* Rule, then pull-quote (15 px darkteal italic):
  `"AI is being used a lot by people who aren't mathematicians… no human has read it."`
  attribution 13 px muted: `— Thomas Bloom, curator, erdosproblems.com`
* Stat: **`1 in 277`** (30 px cyan bold) + `arXiv submissions flagged as unvetted LLM output, early 2026. Now a one-year ban.` (13.5 px muted)

**Summary line**, centred, y = 600, 24 px darkteal bold, two lines:

```
Generation has been automated faster than verification —
and the gap is the whole story.
```

**Do not use emoji** for the tracker markers (🟢🟡🔴⚪). LuaLaTeX emoji support is a trap and
the colour-blind reading is better with shape+fill. Draw circles.

### 4.3 Geometry

```
legend row      y 110, left 40, three groups, gap 34
list rows       left 34, width 802, height 43, radius 7, tops at
                150, 193, 236, 279, 322, 365, 408, 451
   badge        58 × 22, radius 6, white 13 px bold, at row left + 6
   date         96 px column, 14.5 px darkteal bold
   text         15.8 px ink, one line each (all eight fit in 638 px)
vertical rule   x 848, y 150 → 578, 1 px lightgrey
right column    left 862, width 378
quote box       (34, 504) 802 × 76, fill #F0F2F3, 5 px cyan left border, radius 8,
                padding 12/18
summary         centred, top 600
```

### 4.4 Build / reveal order

| step | reveals |
|---|---|
| 0 | title, tier legend |
| 1 | rows 1–2 (the two clean T1 anchors) |
| 2 | rows 3–4 + the `PHYSICS` tag — *"and here is your field"* |
| 3 | rows 5–6 |
| 4 | row 7 + the Jacobian quote box |
| 5 | row 8 (Astra) — including `zero referees` |
| 6 | the whole right-hand "denominator" column |
| 7 | the summary line |

Dramaturgy matters here: the flurry lands first and looks *well checked* — eight famous
results, six of them T1/T2. Only at step 6 does the denominator arrive and reframe it.
Steps 3 and 5 may be merged if time is short (→ 6 steps).

### 4.5 Content decisions (and why)

* Item list is research `llm-proof-results.md` §"Slide-ready distillation" **verbatim in
  selection**, with wording tightened to fit one line each.
* Item 5's Gowers quote ("would have recommended *Annals* acceptance") was **removed from
  the row** and replaced by "nine mathematicians read it line by line" — because *that* is
  what makes it T2, and the Gowers quote already appears on Hook A's caption. Don't run the
  quote twice.
* Item 7's tier is shown as **T3** (not "T3→T2"); the promotion is carried by the quote-box
  caption "checked by hand within days". A two-state badge is unreadable at 58 px.
* Item 3's wording is **"Gauge-theory amplitudes"** — see the errata in §0.
* IMO 2026's 42/42 is **not** on this slide. Research flags it single-source (SCMP). Keeping
  a "verification tiers" slide honest means not putting an unverified item on it as though it
  were T1.
* The "1,217 problems, 565 solved" denominator line was cut for space; it is the first thing
  to restore if the right column looks thin.

### 4.6 Cut first, in this order

1. Drop row 1 (Jul 2025 IMO gold) — the oldest, the least surprising, and competition maths
   is the weakest evidence of research capability. → 7 rows.
2. Drop row 6 (AlphaProof Nexus) — its T1/cost point is repeated by row 8. → 6 rows.
3. Drop the `1 in 277` stat block from the right column (keep the four markers and Bloom).
4. **Never cut** the quote box, the `zero referees` red, or the summary line.

---

## 5. G4 — The timeline, extended

### 5.1 Title and chrome

* **Title:** `The timeline, extended`
* **Subtitle**, left-aligned at (40, 106), 15 px muted:
  `Left of today: measured. Right of today: extrapolation, clearly labelled.`
  (It must be **left**-aligned under the title — a top-right kicker collides with the
  extrapolated line. This was found in render, not in theory.)

### 5.2 Exact content

**The axis and the line:**

* Year labels, 13 px: `2023` `2024` `2025` `2026` in faint; `2027` `2028` `2029` in
  `#b6c0c5` (lighter — they are the future)
* Rotated label along the solid segment, 15 px darkteal bold:
  `measured capability — 179 frontier models since 2023`
* `today` (13 px darkteal bold) just left of the today rule
* Three `?` (19 px cyan bold) above the three hollow circles on the dashed segment
* `the slope has not bent yet` (16 px cyan bold italic) under the dashed segment

**Six number chips** (2 rows × 3, big number 37 px cyan, caption 15.5 px ink, hard line
break as shown):

| number | caption |
|---|---|
| `+13.0 / yr` | Epoch Capabilities Index — / still linear, no ceiling in sight |
| `94.6%` | GPQA Diamond, saturated — / the expert humans sit at 69.7% |
| `32.3%` | CritPt research physics — / **your** frontier is still wide open |
| `~1000×` | Cheaper per attempt than 2023 — / so run it a hundred ways and check |
| `$2,000` | Price of a decade-open / conjecture, August 2026 |
| `2 s → 12 h` | Autonomous task horizon — / doubling every 4–7 months |

**Bridge line**, centred y = 534, 17 px muted, two lines:

```
Who did well in software: not the people who denied it, not the people who surrendered to it —
the people who learned to specify, to check, and to own the result.
```

**Payload**, centred y = 590, 33 px darkteal bold:

```
What would you attempt if the tedious 90% were free?
```

**Sub-payload**, centred y = 648, 23 px cyan bold:

```
Aim there.
```

### 5.3 Geometry

```
axis                y 286, x 60 → 1240, 2 px lightgrey
year ticks          1.4 px #C7CFD3, y 286 → 294, at x = 90, 260, 430, 600, 770, 940, 1110
                    (170 px per year; 2023 at x = 90)
year labels         top 298, 13 px, centred on tick
measured line       (90, 270) → (710, 183), 3.4 px darkteal; dot r 4.5 at the start;
                    dot r 6 with 2.5 px white ring at the "today" end
today rule          (710, 183) → (710, 286), 1.4 px cyan, dash 3/4, 80 % opacity
extrapolated line   (710, 183) → (1180, 117), 3 px cyan, dash 9/7
"?" circles         r 7, white fill, 2.4 px cyan stroke, at (860,162) (1010,141) (1160,120)
                    — all exactly on the dashed line
rotated label       origin (146, 200), rotate −7.97° (matches the line slope)
chips               width 380, 4 px cyan left border, 16 px left padding
                    lefts = 40, 450, 860;  tops = 336 and 432
```

The whole picture is one statement: **the measured segment ends at today, the dashed segment
keeps the same slope, and the open space to the upper right is where the audience's next ten
years live.** Do not add a ceiling, a saturation curve, or an error band — the point is that
the slope has not bent, and any decoration weakens it.

### 5.4 Build / reveal order

| step | reveals |
|---|---|
| 0 | title, subtitle, axis, year ticks and labels |
| 1 | the measured (solid) line + its rotated label + the `today` marker and rule |
| 2 | the dashed extrapolation + the three `?` + `the slope has not bent yet` |
| 3 | chips 1–3 (top row) |
| 4 | chips 4–6 (bottom row) |
| 5 | the bridge line |
| 6 | the payload |
| 7 | `Aim there.` |

Steps 6 and 7 must be **separate**. The pause between the question and the answer is the
whole emotional move, and it hands directly to the "slop cannon is charged" statement slide.

### 5.5 Content decisions (and why)

* Six chips, not the ten rows of research §5 Slide C. **Dropped:** the `49 days / open weights
  6.9 months` row (already a slide of its own — *"You can run the frontier locally"*,
  `talk.tex` ≈ line 868) and the `Feb 2026 "AI slows devs" withdrawn` row (it is the hinge of
  G1; repeating it here weakens both).
* The `2026 — thrived: those who adopted orchestration and verification early` row was
  promoted from a chip to the **bridge line** — it is prose, it is the argument, and it is
  what turns six numbers into an instruction.
* The `~1000×` caption gained "*so run it a hundred ways and check*". The number alone is
  trivia; with the clause it is a research method, and it rhymes with G3's verification theme.
* `32.3%` is the most important chip for this audience and is placed top-right (end of the
  first reading line) with **your** in bold. It is the slide's only bold word inside a caption.
* The rotated line label deliberately does **not** repeat "+13.0" — that number is chip 1.

### 5.6 Cut first, in this order

1. Drop chip 5 (`$2,000`) — the number recurs on G2 column 6 and on G3 row 8. → 5 chips,
   re-lay as 3 + 2 or widen to 3 × 390.
2. Drop chip 2 (`94.6%` GPQA) — saturation is covered by the deck's existing
   *"Benchmarks saturate, then get replaced"* slide.
3. Drop the bridge line (speak it).
4. **Never cut** the payload or `Aim there.`

---

## 6. Global notes for both implementers

1. **Character escaping (beamer):** `Erdős` (`Erd\H{o}s` or UTF-8 under LuaLaTeX — fine),
   `−78%` (use `\textminus` or `$-$`), `≥ 3` (`$\geq 3$`), `→` (`$\to$`), `$2,000`
   (`\$2{,}000`), `%` (`\%`), `#728` (`\#728`), `"…"` (use `` `` `` and `''`).
   The Jacobian quote must be **verbatim and lowercase**: `hello there the jacobian
   conjecture is false thanx` — do not let a spell-checker or `\MakeUppercase` near it.
2. **Nothing on these four slides animates beyond appearing.** Every build step is a plain
   opacity/`\onslide` reveal, so the beamer and HTML versions are genuinely equivalent. The
   only state-swap is G1's grey→coloured stage pills, and it has a documented fallback.
3. **The four slides share one visual grammar**: coloured dot/date, thin stem, spine or lane
   rule, and one bottom band carrying the interpretation. G1 establishes it, G2 varies it,
   G4 closes it. G3 is the odd one out (a ranked list, not a timeline) and that is deliberate
   — it is a *verification ledger*, and it should not look like a timeline.
4. **Red budget:** G1 has three red dates, G3 has one badge colour plus two words, G2 and G4
   have none. Do not add more.
5. Verify against `renders/g1.png … g4.png`. If a rendered implementation looks busier than
   those PNGs, an item has crept in — remove it rather than shrinking type.
