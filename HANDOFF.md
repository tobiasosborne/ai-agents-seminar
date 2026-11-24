# Handoff: AI Agents Seminar

## What this is

Materials for a 1-hour seminar: "Large Language Models: A Physicist's
Perspective." Demystifies LLMs and AI coding agents by rebuilding the
entire stack from first principles for a physics audience.

## Current focus: Collège de France symposium, Paris, Wed 25 Nov 2026

**State Tue 24 Nov 2026, 11:30: revised deck released.** `Paris-talk-2026/slides-web/talk.html`, sha1 `26f9df1a`
(built 10:31), 20 slides, 57 states, one offline file; `talk.pdf` (20 pages) is made from final-state screenshots of the
same file. Both are committed here; everything else in `Paris-talk-2026/` stays local (its `.gitignore` tracks only
those two files; `deck/` is its own local git repository with no remote).
- The speaker reviewed the 22-slide deck on Mon 23 Nov (`context/SPEAKER-VERBATIM.md` section 4) and rejected several
  slides as smug and preachy. `contracts/CHANGE-ORDER-2026-11-23.md` turned the review into a 19-slide deck (release
  `d9a919fc`, Tue 01:29). His second review on Tue 24 Nov (section 5, `contracts/CHANGE-ORDER-2026-11-24.md`) added:
  dial entries appear as the hand passes (slide 2), a thinking machine on `cognition-resource`, an illustration on
  `hard-2`, the time-machine date counter on `repos`, and a new slide `no-slop` (Dex Horthy's manifesto as reverse
  graffiti) after `learned`.
- Tone rule from the review: no aphorisms, no advice or imperatives to the audience; slide text is his own phrases,
  verbatim quotations or data labels; a context-free reader checks new slides.
- Not measured on the real GPU for release `26f9df1a`: `deck/tools/morning-gpu-check.sh` (about ten minutes, opens
  Chrome windows on the desktop, so only with the speaker's go-ahead). Unconfirmed: the fix for a seam near the dial's
  side captions on slide 2 (not reproduced headless). Known: Back from the last step of `rh` lands on its first step.
- Open, speaker's call: wording flags on `hard-1`, `hard-2`, `bitter-lesson` and `learned` listed in
  `status/STORY.md`; several design options kept beside the deck.

**State Sun 22 Nov 2026, 06:10 (superseded): the deck exists.** `Paris-talk-2026/slides-web/talk.html`, sha1 `b9c5ae82`
(built 05:50; copies of each release in `slides-web/release/`), 22 slides, 34.7 MB, one offline file (a CSP blocks all
network), `talk.pdf` (22 pages) made from the same file. Built overnight 21 to 22 Nov by two Opus orchestrators (ENG,
STORY) under the charter `Paris-talk-2026/PROJECT.md`; the speaker has not reviewed it yet. Read for him:
`narrative/FOR-THE-SPEAKER.md` (keys, options kept beside the deck, Neon's three string changes on the Riemann slide,
cut points, Neon's questions with the defaults taken) and `status/ENG-FOR-THE-SPEAKER.md` (how to open, present,
rebuild). Contact sheet of the release: `status/deck-final-b9c5ae82.jpg`.
- Words and narrative are Gemini Neon's (`narrative/pass-2.5.md`), reviewed by Muse, fact-checked by Astra including
  every word as rendered. No Claude or Codex model may write or edit slide or note prose (charter section 2).
- Three registers: woodcut (central), punk (spray and stencil intrusions), indigo and gold. Design system:
  `contracts/DESIGN-SYSTEM.md`. Running order ENG builds from: `contracts/RUNNING-ORDER.md`. Slide API:
  `contracts/SLIDE-CONTRACT.md`. Slide modules: `deck/slides/<id>/`; engine `deck/engine/`; `deck/` has its own local
  git repository.
- Rebuild: `deck/build/integrate.sh` (re-bakes the spray pictures and writes the release); check with
  `deck/tools/walk.mjs`, `gpu.mjs`, `shot.mjs`, `soak.mjs` (they take `deck/.browser.lock`; see `deck/tools/README.md`).
- Measured on this laptop in headed Google Chrome on the real GPU, every step forwards and back: median 11.1 ms, p95
  11.2 ms at 1920x1080 pixel ratio 1 and on the panel at pixel ratio 2; cold open about 0.6 s. Standing items are in
  `status/ENG.md` (frames dropped in the first 1.5 s after opening; a second WebGL context on `myoutput`; Firefox
  timed only with software rendering; physical F-key fullscreen not exercised).
- He presents in Chrome on this laptop; projector resolution unknown.


`Paris-talk-2026/` was created on 21 Nov 2026 and holds only `BRIEF.md` and
`source/LLM_symposium_abstract.pdf`. **There is no deck yet.** Symposium "Apocalyptic or
Integrated? Debating the impact of Large Language Models in Theoretical Physics"; talk
"Ground Truth: What Remains Human in LLM-Assisted Theoretical Physics", about 25 minutes
plus 15 of questions, hybrid audience of theoretical physicists, then a panel. The speaker
said this talk "will be a little different", so the form is open: do not assume a copy of
the Hannover deck. `BRIEF.md` has the event facts from the email threads, the abstract,
a table mapping each abstract claim to existing slides, what is new work (the "ground
truth" framing, teaching, leadership), and what is not known (time, room, other speakers:
the symposium website refuses automated access).

Added later on 21 Nov: `research/alpoge-2026-11-21/FACTS.md` (Alpöge's Lean-only proof of
the Riemann Hypothesis, 20 Nov, with raw pages; never write "nobody understands it", see
the brief) and `sources/` (read `sources/README.md` first): the claude.ai design handoff
with four finished slides in a woodcut and spray-can language (`ground-truth-handoff/`)
and a 569 MB copy of the "De forma scientiae" fractal-knowledge project with its six-slide
WebGL deck (`fractal-knowledge/`; the 8.2 GB original is in
`~/.t3/scratch/2026-11-20-in-a-german-lang-interview-f6c02489`). Five subagent notes in
`sources/notes/`. The speaker wants the talk "much shorter" with "lots of new design ideas
and slides"; no running order exists yet. (Since 24 Nov `Paris-talk-2026/` has a `.gitignore` that tracks only
the deck; the folder is 11 GB, so never force-add it.)

## Previous focus: Hannover DQ-mat Jour Fixe, Thu 5 Nov 2026

**Deck: `Hannover-talk-2026/slides-web/talk.html`, 75 slides, `talk.pdf` the 75-page
export (render.mjs 0 findings, walk.mjs 75 visited, no errors, no network requests).
Nothing from 3 or 4 Nov is committed.** DQ-mat Jour Fixe, Leibniz Universität Hannover,
HiTec Room 317, 10:15 to 12:00 (recorded), then a hands-on session 13:00 to 15:00 in
the same room. Title from the invitation (Anke Schmidt, 3 Nov): "Large Language Models:
A physicist's perspective on science after the AI summer of 2026". Brief, event and
abstract: `Hannover-talk-2026/staging-2026-11-03/BRIEF.md`.

Built on 3 Nov from the Melbourne deck of 16 Oct (kept as `slides-web/talk.html.pre-1103`).
**The deck is generated: run `staging-2026-11-03/integrate/build.sh`**, which copies the
backup and applies the three pipeline ops files (`epoch/`, `ack/`, `cost-md/`), then
`integrate/ops.json` (restored and new fragments) and `integrate/edits.py` (asserted
string edits). Edit a fragment or `edits.py` and re-run; never hand-edit the deck.
- Data refreshed to 3 Nov: Epoch ECI (refit by Epoch: 269 models, +14.6 per year,
  GPT-6 Astra 169.1 leads within error of Opus 5.5 and GPT-6.1 Terra; open-weight median
  lag 5.5 months, DeepSeek V4.1 Flash ties Kimi K3), arXiv acknowledgments (complete
  October: quant-ph 28%, math-ph 38%, doubling 2.7 months), openai/math at commit 4eaee87
  (721 manuscripts, 373 families, 29.8M lines of Lean). `s-cost` stays frozen at the
  12 Oct snapshot (Artificial Analysis moved to Index v5.0 without history; label says so).
- Restored for the longer slot, leaned per the 13 Oct verdict: `s-curl`; the failure
  interlude `s-divfail`, `s-zoo` (the Melbourne flip cards, back on 4 Nov in place of
  `s-zooarch` and `s-zoopost` at the speaker's request), `s-archfacts`; `s-correctable` and
  `s-errorcorr`; the structured-proof block `s-whystructure`,
  `s-lamport`, `s-adversarial`, `s-vibefeld` in front of `s-ladder`; `s-breaks`.
  Not restored: `s-defense` (s-ladder is its redraw), `s-deepblue`, `s-bench`, grades.
- New: trickle step 4 (26 Oct); `s-oct26` (Kakeya, ETH, Yang-Mills with verification
  status); `s-checked` (quasi-RH, Siegel rewrites, Hodge sign error, Axiom CFSG with 34
  deviations); `s-echo` step 4 (Hacker News reply to Derek Thompson); `s-strain` (six
  probability journals closed to 8 Nov, 75.5% early-career survey); `s-physloop` (Lukin
  group circuits, nine-loop amplitude checked by Dixon); `s-hg-tasaki`; `s-handson`.
  Every quote string-checked on 3 Nov against raw pages saved in `integrate/fetch/`.
- 4 Nov fixes (edits.py sections 9 to 15, all after speaker review): worldlines labels no longer
  rotate with the grid; both displacement-map filters removed from the Haldane block (staircase
  at device pixel ratio 1); the hatched disc on `s-hg-flow` redrawn as clipped lines (proof sheet
  and pixel counts in `renders/s58proof/`, scripts `design/proof-hatch.{mjs,py}`); PicoGPT.jl
  link on `s-defn`. Playwright Firefox is installed for cross-engine checks.
- Documents: `SPEAKER-NOTES-2026-11-05.md` (clock, keys, slide map, cues, caveats, cuts),
  `CHANGELOG-2026-11-03.md` (every edit and source), `HANDS-ON-2026-11-05.md` (afternoon
  handout).

Not done or open: the 26 Oct statuses must be re-checked on the morning of 5 Nov (chips in
`integrate/s-oct26.html`); Anthropic's ETH paper read only via OfficeChai; the demo scripts in
`02-illusion-of-chat/` and `03-primitive-agent/` still name `claude-sonnet-4-6` and were
not run (the handout says to change the model string); Antigravity install command and
Cursor plan names unconfirmed ("check on the day"); new slides untested on the lecture
laptop, projector and clicker; the 26 Oct label on the trickle sits close to the right edge.

The backup restore of 3 Nov put the uncommitted USyd, CQT, DAW and Melbourne working
folders back on this machine; the Hannover folder (created 3 Nov) takes its deck and pipelines from them.

## Also current: Theoretische Physik C, lecture 1 opener (Thu 22 Oct 2026, German)

`TheoC-Vorlesung-2026/slides-web/talk.html`, 14 slides, German, `talk.pdf` the 14-page
export (render.mjs 0 findings, walk.mjs no errors). Slides 13-14 (lane `bildung`, sources
in its apply.py docstring): Nds. Verfassung Art. 4 Abs. 1 "Jeder Mensch hat das Recht auf
Bildung", BVerfG 19 Nov 2021 (1 BvR 971/21) Recht auf schulische Bildung from Art. 2 Abs. 1
i. V. m. Art. 7 Abs. 1 GG; then "Bildung war nie wichtiger. Daran zu arbeiten ist unsere
Aufgabe." Audience: third-semester Lehramt
students, Hannover. Built on 22 Oct: `design/make_base.py` makes the English base
`talk-en.html` (Melbourne subset: title, four story slides, survey, md-trickle, md-flood,
mathslag, outsource; plus s-control and s-scatter with their script from the CQT deck);
`design/integrate.py` applies the German lanes `staging/<lane>/apply.py` in order (engine,
story1, story2, md, lag, grades, proof). Edit a lane's apply.py and re-run integrate, never
the output. Each lane's `NOTES.md` and `staging/proof/REPORT.md` list deviations and open
calls (closer wording, "Programmiertest" for SWE-bench, Gowers "zur Annahme empfehlen").
The German scatter PNGs come from `staging/grades/analyse_de.py` on the Würzburg
`grades.csv` (synthetic data, b and r checked against the README table). The render and
walk scripts take `DECK=<path>`. Data snapshots stay dated 12 Oct. Uncommitted.

## Also current: University of Melbourne seminar (Fri 16 Oct 2026)

`Melbourne-talk-2026/slides-web/talk.html`, 59 slides, `talk.pdf` the 59-page
export (render.mjs 0 findings on the two edited slides, walk.mjs 59 visited,
no errors). Seminar to Lloyd Hollenberg's group, IBM Quantum Hub, School of
Physics, The University of Melbourne (email thread "visit 16th of Oct", 21 to
28 Sep 2026; room and time were left to his postdocs, no later email). Title
and abstract as sent 25 Sep: "Large Language Models: A Physicist's
Perspective". It is a verbatim copy of the USyd deck as of 14 Oct (commit
`6d1f3fa`) with only the venue and date changed: title-slide eyebrow and date
("16 October 2026"), and the "You are here" sub-label on `s-mathslag`
("Melbourne, 16 October 2026"). Data snapshots (Epoch, Artificial Analysis,
openai/math, arXiv acknowledgments) are deliberately NOT refreshed: all still
dated 12 Oct 2026 on the slides. `design/` holds copies of the four USyd
Playwright scripts. Uncommitted.

## Also current: Data & Analytics Wednesday Sydney (Wed 14 Oct 2026, 18:00, 30 minutes)

`DAW-talk-2026/slides-web/talk.html`, 29 slides, `talk.pdf` the 29-page export
(render.mjs 0 findings, walk.mjs no errors). Title "Science in the era of
cognitive abundance". It is a strict subset of the USyd deck, GENERATED by
`python3 design/make_subset.py ../USyd-talk-2026/slides-web/talk.html slides-web/talk.html`
(run inside `DAW-talk-2026/`): edit the `KEEP` list there, never the output.
Beyond deletions it changes only the title slide, guards four shared
scripts that looked up cut slides, and splices `design/s-whoami-b.html`
("Open lectures": YouTube channel, views vs citations dot animation, 12 Oct
numbers from USyd `.pre-1013`) in as slide 2 (added 14 Oct; pre-insert deck
kept as `slides-web/talk.html.pre-whoami`). Kept: title, five story slides, md-trickle,
md-flood, md-cascade, three acknowledgment slides, mathslag, echo, zoo,
ladder, dagx, hg-intro, hg-worldlines, hg-fineprint, cost, myoutput, explore,
repos, beck-math, learned, outsource, mission, lastpage. Cut: all dividers, the
LLM, chat and agent-loop sections, ECI and open-weight slides. First cuts if
time runs short: hg-worldlines, hg-fineprint, acksing. Uncommitted.

## Previous focus: University of Sydney talk (October 2026, day not yet set)

**State after the 13 Oct 2026 tightening pass: `USyd-talk-2026/slides-web/talk.html`
is 60 slides, `talk.pdf` the matching 60-page export (render.mjs 0 findings,
walk.mjs no errors). Nothing from 12 or 13 Oct is committed.** The 12 Oct
description below is superseded where it conflicts with this block. Backup of
the 12 Oct state: `slides-web/talk.html.pre-1013`. Staging, briefs, notes and
renders: `USyd-talk-2026/staging-2026-10-13/` (`BRIEF.md` records the speaker's
verdict: no interpretive comment lines or taglines on slides, less text, no
gimmick animation; `orchestrator_edits.py` is the deletion and text-cut script).

- Deleted: `s-story-letter`, `s-hookA`, `s-hookB`, `s-curl`, `s-bench`, `s-beck`,
  `s-voxel`, `s-breaks`, `s-absorb` and all backup slides. `s-mission` is second
  last, `s-lastpage` (Maclaurin) is the final slide.
- Comment lines removed on `s-acksing`, `s-mathslag`, `s-echo` (retitled
  "Déjà vu"), `s-ctxwindow`, `s-hg-intro`. `s-mathslag` has the wedge
  extrapolated into the 6 Oct column as dots (log-linear fit, about 6 months).
  `s-beck-math` is titled "Output ≠ mission", credit "adapted from Kent Beck".
- Story (`staging-2026-10-13/story/`, script `STORY-2026-10-13.md`):
  `s-story-hand` is formula, term counter and curves only; `s-story-machine`
  opens on 64,000 computers; `s-story-reveal` keeps only the Buchan drawing and
  says "my clansman"; no ancestry is claimed anywhere (the reason and the
  source material are in the local story folder, which is never shown).
  `s-lastpage` now shows the full final sentence of the 1748 Account, p. 392;
  no source says it was the last sentence dictated, so that caption is gone.
- `s-md-trickle` to `s-md-flood` is a zoom (window "10 Sep to 6 Oct", inset
  mini-timeline on the flood); see `staging-2026-10-13/zoom/NOTES.md`.
- New after `s-myoutput`: `s-explore` (voxel exploration vs exploitation, three
  builds) and `s-repos` (94 repositories, one block per active week; alethfeld
  and vibefeld merged as one lineage; "4 papers, Oct 2025 to Sep 2026"). Data
  and scripts: `staging-2026-10-13/repostats/`.

Open, speaker's call (13 Oct): "my clansman" or "my kinsman"; whether the full quote is too
long; unrequested cuts by the story agent (HP-35 running display, "the
calculating"/"the proving" on `s-story-now`); Boston Globe quote on
`s-story-after`; `s-repos` says 4 papers in the year (rate unchanged over 25
years), not "few to none"; zoom cross-fade overlaps titles for 0.3 s; new
slides untested on the lecture laptop, Firefox, or with a clicker.

### 12 Oct reboot (as written then)

**Deck: `USyd-talk-2026/slides-web/talk.html`, 71 slides (67 in the running
order plus a divider and three backup slides); `talk.pdf` is the matching
71-page export.** Rebooted on 12 Oct 2026 from the 67-slide copy of
the CQT deck (kept as `slides-web/talk.html.pre-reboot`; the CQT state is
`.pre-usyd`). Stance: the disruption has happened, accept it, think
optimistically. Less on failure modes and Vibefeld; no dread, grief or slop
framing; the 25 Fields Medallists' statement is deliberately not cited.

The talk now OPENS WITH A STORY, built on the narrative device of DHH's Rails
World keynote (calm history, family reveal, map to one date). Six slides after
the title: `s-story-letter` (Newton's 1725 letter offering twenty pounds a
year), `s-story-hand` (the series by hand, Berkeley's "Ghosts", 763 pages),
`s-story-machine` (a computer was a job, Richardson's 64,000, the HP-35 of
January 1972 as the Kodak Brownie counterpart), `s-story-reveal` ("my
ancestor": Colin Maclaurin; the speaker introduces himself here),
`s-story-after` (2,661 to 124,917 publications a year; the 1976 four colour
complaint, planted for `s-echo`), `s-story-now` (6 October 2026 is the HP-35
of proof). The callback `s-lastpage` (Maclaurin's last dictated sentence) sits
before `s-mission`. **The spoken script with clicker cues, alternatives,
plants and pay-offs, and the status of every fact is
`USyd-talk-2026/staging-2026-10-12/story/STORY.md`: read it before touching
the opening.** Research: `staging-2026-10-12/research-maclaurin/FACTS.md` and
`research-computing/FACTS.md`. `s-whoami-a` and the Part Six `s-maclaurin`
are gone; `s-brownie`, `s-dhh` and `s-whoami-b` are backup slides after
`s-backup` at the very end.

Running order: 1 Why this talk? (title, the six story slides, survey, hooks, five md slides,
three acknowledgment slides, `s-mathslag`, `s-echo`, `s-capable`); 2 What is
an LLM?; 3 The illusion of chat (two slides); 4 From function to agent
(`s-zoo` replaces six failure-mode slides, `s-ladder` replaces five
structured-proof slides, then `s-dagx` and the Haldane block); 5 The trend
(`s-eci`, `s-bench`, new `s-cost`, `s-openweight`, all live SVG); 6 What is
it for? (`s-myoutput`, `s-beck`, `s-beck-math`, `s-voxel`, `s-breaks`,
`s-absorb`, `s-instruments`, `s-learned`, `s-outsource`, `s-lastpage`,
`s-mission`). Cut: deepblue, control, scatter,
grief, slopcannon.

How it was built: 15 subagents (3 Sonnet research, 12 Opus), each delivering
fragments, `ops.json` and `NOTES.md` under
`USyd-talk-2026/staging-2026-10-12/<name>/` (local only). `BRIEF.md` there
holds the rules; `master-ops.json` plus `ack/ops.json` and
`maclaurin/ops.json` and then `story/ops.json` reproduce the integration
from `.pre-reboot`
(`integrate/` is the test copy). Per-slide sources, speaker cues and open
issues are in each `NOTES.md`; research in `research-beck/`,
`research-mathnews/`, `research-misc/` (each `FACTS.md`). Source material for
the new part: `research/reboot-2026-10-12/src/` (DHH transcript and analysis,
productivity audit) and `staging-2026-10-12/beck-meditation.md`.

Data state, 12 Oct: openai/math is 719 manuscripts, 372 families, 242 with a
Lean artefact (three withdrawn on 7 Oct); Epoch export unchanged since 8 Oct;
arXiv acknowledgments extended to 1 to 8 Oct (pooled 33.1%, now consistent
with the fitted line, doubling 2.8 months); Artificial Analysis price fit
refreshed (divide by 23, 20, 130 per year at index 10, 20, 30).

Tooling: `design/render.mjs`, `render-steps.mjs`, `print-pdf.mjs` in the USyd
folder now pass an explicit Chromium path (the global Playwright wants build
1212, only 1248 is installed; the other talk folders still have the unpatched
scripts). New `design/walk.mjs` walks the deck with real key presses and
reports page errors and network requests. Animated slides need longer waits
than `render-steps.mjs` gives (see the dhh and myoutput notes).

Open, speaker's call:
- `s-mathslag` title is now "from three years to ten months": the "+441%
  review time" beat could not be sourced and was dropped.
- Beck's wording is paraphrase only (no transcript; YouTube blocked captions).
  The speaker confirmed the content from having watched the talk.
- DHH: "30,000 lines" is per year (his "about 60 times" needs that); the
  Tuxen ancestor reveal is unverified and off the slides. Maclaurin kinship is
  not stated on the slide.
- Opening story, spoken with a hedge because only secondary sources were
  found: ENIAC February 1946, the last Keuffel and Esser slide rule (11 July
  1976), Feigenbaum's pocket calculator. The Boston Globe quotation on
  `s-story-after` is string-checked but from a 2013 obituary. "1725" for
  Newton's letter is inferred (Murdoch prints no date). The HP-35 key legends
  were drawn from memory. The script says "six days ago" and "twenty-five
  years": adjust to the talk date.
- `s-voxel` needs GPU acceleration (60 fps on Iris Xe, about 8 fps without);
  test on the presentation machine. Not tested in Firefox or Safari.
- `s-bench` shows FrontierMath v2 at 94% (in Epoch's export) beside the
  original tiers at 52%; `s-ctxwindow` still says "200k to 1M tokens";
  `s-whoami-b` keeps 157 papers (Scholar shows 145); `s-cost` credits the fit
  to the speaker although it was refitted on 12 Oct with his estimator;
  `s-instruments` writes [4, infinity] closed and takes its dates from
  Evans and Kawahigashi.
- Convex panel transcript still covers 0:00 to 30:00 only, with guessed
  speaker labels; the Browne quote on `s-learned` is not checked against video.
- No USyd speaker notes or changelog. No education-ROI slide. Nothing from
  12 Oct is committed.
- The speaker has a signed reaction on the Proofs and Prompts "100 reactions"
  page; do not cite it as independent evidence.

## Previous focus: CQT Singapore talk (Thu 8 Oct 2026)

`CQT-talk-2026/` was created on 7 Oct 2026 by copying `Magdeburg-talk-2026/`.
**Present from `CQT-talk-2026/slides-web/talk.html`** (64 slides, final 8 Oct
11:09; `talk.pdf` is the 64-page export). Read first:
`CQT-talk-2026/SPEAKER-NOTES-2026-10-08.md` (changed message, keys, full slide
map, per-slide notes) and `CHANGELOG-2026-10-08.md` (every edit, sources,
verification, open issues).

8 Oct rework (morning of the talk, one Workflow run of 6 Opus + 1 Sonnet
builders, an Opus ECI agent and an Opus integrator; the Sonnet verifier died
on a network outage and its checks were re-run by hand, all clean): venue set
to CQT; 13 slides deleted (ackcontrol, gap, lyapunov, euhosted, budget,
limits, summary, cta, afternoon, extended, kontorovich, flurry, md-close);
`s-capable` and `s-defense` retitled; new `s-md-trickle` (the old s-flurry
rows in the particle styling), `s-deepblue` (Simon Willison's "Deep Blue"
adapted to openai/math), Haldane interlude `s-hg-intro` + five option C
slides after `s-dagx`; arXiv acknowledgment survey extended to 1 to 7 Oct
(out-of-sample test of the 22 Sep line: predicted 28%, observed 36% in
quant-ph); `s-grief` and `s-mathslag` ("The lag collapsed: from three years to
three months") updated; Epoch refresh to 8 Oct (272 models, 14.1 pts/yr,
Opus 5.5 leader 167.3; all former estimates now measured) with a speculative
marker for the unreleased openai/math model (about 171, band 168 to 175).

Pipeline fix worth knowing: Epoch moved the ECI table to
`epoch_capabilities_index/eci_scores.csv`; `model-progress/analyse.py` now
reads it via `eci_table()` (the stale flat file silently froze the 22 Sep
numbers). Tooling added: `design/splice.py` (deterministic slide splicer
driven by ops.json), used so parallel agents never edit the deck directly;
their fragments and test copies are in `staging-2026-10-08/` (untracked,
can be deleted after the talk). Backups: `slides-web/talk.html.pre-1008`
(start of 8 Oct), `.pre-integrate-1008`, `.pre-cqt` (Magdeburg base).

Committed as `6a0c4a7`. Not done: minor render nits listed in the
changelog section 5 (ackexp in-plot note touches a marker, two Haldane labels
crowd the hatched disc, Deep Blue chess glyphs depend on the laptop font);
Cursor $60B and the 1997 match facts not re-verified today.

## Previous focus: MPI Magdeburg talk (Wed 23 Sep 2026)

`Magdeburg-talk-2026/` is a copy of the QuSoft deck adapted on 22 Sep 2026 for
the Max Planck Institute for Dynamics of Complex Technical Systems (host Luís
Pires, Nueske group). **Present from `Magdeburg-talk-2026/slides-web/talk.html`**
(68 slides, all render-verified 22 Sep; `talk.pdf` is the 68-page export; economics backup slides removed).

Read first: `Magdeburg-talk-2026/SPEAKER-NOTES-2026-09-23.md` (room, what to
say per changed slide, rumours, reserves) and `CHANGELOG-2026-09-22.md` (every
edit). Audience and guiding-problem research:
`Magdeburg-talk-2026/research/magdeburg-2026-09-22/`.

Main changes vs QuSoft: title and venue; `s-lyapunov` replaces no-cloning; new
`s-here` (institute problems by bottleneck) and `s-ackcontrol` (eess.SY
acknowledgments, 12% in Sep, mostly language); Navier-Stokes row on
`s-flurry`; registry counts, Cortecs prices, Epoch 22 Sep snapshot (GPQA
95.8%) and arXiv September data refreshed; SURF/Dutch items replaced by GWDG.
`model-progress/analyse.py` now hides four new estimates from fig3 via
`"plot": False`.

Not done: nothing committed (the folder's `.gitignore` tracks only
`slides-web/talk.html` and `talk.pdf`); Opus 5.5 and "GPT-6 Sol" were only
rumours as of 22 Sep afternoon; Palomar and openproblem.ai counts not re-read.

## Previous focus: QuSoft seminar, Amsterdam (Fri 4 Sep 2026, 11:00-12:00)

`QuSoft-talk-2026/` is a copy of the München talk (research, pipelines, decks)
adapted on 2 Sep 2026 for the Special QuSoft Seminar "The industrialization of
theoretical sciences" at CWI (Turing Room, Amsterdam Science Park; chair Jonas
Helsen; other speakers Holmes, Guo, Dominik, Renaud, Evers). **Present from
`QuSoft-talk-2026/slides-web/talk.html`** (70 slides, render-verified 4 Sep).

Read first: `QuSoft-talk-2026/SPEAKER-NOTES-2026-09-04.md` (what to say, caveats,
reserves, the HAWK/CWI sensitivity, the DAG explorer), `CHANGELOG-2026-09-04.md`
(morning-of edits), `CHANGELOG-2026-09-02.md` (the 2 Sep adaptation, every edit
with sources), `SPEC-QUSOFT.md` (the decided edit list). Research for the 2 Sep
pass is in `QuSoft-talk-2026/research/updates-2026-09-02/`.

4 Sep morning edits (speaker review): hooks swapped ("It started as a drop" is
slide 3); `s-hawk`, `s-div5`, `s-demo` cut (HAWK stays as a row on `s-flurry`;
the live demo runs outside the deck); Part Six renumbered to Five; Jeffery
closer line removed; new interactive slide `s-dagx` (proof-DAG explorer of
`../almost-idempotent-stochastic-maps`, 364 nodes, click-to-highlight closure,
presets on build steps) after `s-referee`; GPT-6 Astra (released 3 Sep) added to
`s-eci` as a black estimated marker (ECI about 163.8, ARC-AGI-3 99.9% in
OpenAI's harness, 62.7% in ARC Prize's). Backups: `slides-web/talk.html.pre-0904`
(before 4 Sep), `slides-web/talk.html.pre-qusoft` (München). Tooling:
`design/render.mjs` (all slides), `design/render-steps.mjs <id>` (one slide per
build step, page errors), `design/print-pdf.mjs` (print export; `talk.pdf` is
now the 70-page QuSoft export). Late-morning additions: `s-ackexp` (slide 8), the
acknowledgment hockey stick on a log axis with a Poisson exponential fit,
doubling every 2.9 months (`arxiv-acknowledgments/analyse_log.py`), and
`s-acksing` (slide 9), the same line extended to a satirical Singularity, 100%
in March 2027 (`analyse_singularity.py`).

What changed vs München on 2 Sep: title and venue; hooks reordered (maths first);
`s-flurry` rows swapped (HAWK-256/CWI, Riemann zeta 2/3, Holevo-Shirokov in;
Schiffer/Pompeiu out as misattributed, Bethe ansatz and elliptic rank out);
`s-floodstats` recounted (2 Sep); arXiv acknowledgment survey extended to Aug 2026
(quant-ph 20.4%, math-ph 18.1%); Epoch snapshot 2026-09-02 (221 models, 13.1
pts/yr, Fable 5.1 as an estimated marker); new slides `s-euhosted`
(Cortecs prices), `s-sovereign`, `s-budget`, `s-referee`, `s-jeffery`;
`s-context` cut. Kontorovich slide kept.

Not done: beamer `slides/talk.tex` not synced (present from HTML); the QuSoft
directory has never been committed (the whole 2 Sep and 4 Sep work is untracked;
empty `.git`, `.agents`, `.codex` folders left by the codex run should be removed
before `git add`); München recording not yet public (MCQST YouTube channel, or
info@mcqst.de for the Zoom recording).

## Previous focus: MCQST München talk (Thu 27 Aug 2026)

`Muenchen-talk-2026/` — same title/abstract as Würzburg, built by
extending the Würzburg deck with slop-cannon content plus timeline
slides. **The HTML deck is the presentation copy** (speaker prefers
it; interactive builds). The beamer deck is now OUT OF SYNC (see
below).

### 26 Aug rework (this session) — HTML deck only

Big multi-agent rework of `slides-web/talk.html` from the speaker's
per-slide notes. Now **66 slides** (was 70): all em dashes removed
(56 rewritten), slides reordered, retitled, deleted, plus fresh
research content. Highlights:

- Deleted: four-moments timeline, context-rot statement, "harder
  problem" divider, s-fail, Dutch proverb, unhinged-MSc statement.
- Reorder: failure-modes block (divider, zoo ×2, archfacts) now
  right after the context slide; s-filesystem follows s-errorcorr;
  the structured-proof/error-correction block (whystructure …
  defense) moved before the live demo; s-renaissance joined the
  closing timeline block before s-extended.
- Retitles: hookA "It started as a drop"; flurry "The trickle is
  becoming a flood"; grief slide is now just "The timeline" (stage
  dictionary removed, colours kept implicit); "Theoretical sciences
  are 18 months behind"; s-capable rewritten as transition into
  architecture section. New statement slide s-correctable ("There is
  a way to correct for these errors … This room has done that
  before.") after s-archfacts.
- s-flurry reworked: 10 rows all inside 2026, new entries
  Parisi+Zamponi jamming identity (new T2+ "refereed journal" chip),
  S⁶/Hopf-problem claim (T3), Schiffer+Pompeiu Lean-verified (T1),
  elliptic rank record broken twice in a week ≥30→≥31 (T3).
  Jacobian upgraded T3→T2 (verified within days; Lean-checked
  instance in DeepMind formal-conjectures PR #4474). Dropped: IMO
  gold row, AlphaProof Nexus row. Red colour-clash fixed by removing
  the erdosproblems swatch legend.
- NEW slide s-floodstats "Now somebody has to count it": registry
  ecosystem stats (aimath 506 results, 267 in last 8 weeks;
  vibemathed 630→445→98 Lean-verified funnel; mathdb/theoremdb/
  proofatlas/Palomar/openproblem cards). Punchline: "Nine ways to
  count the flood. Not one of them is peer review."
- s-strategies figure-(b)/caption overlap fixed (viewBox padding),
  render-verified. Divider renumbered 4½→3½.
- All changes render-verified via Playwright at 1920×1080, zero
  overflows/collisions on touched slides; renders in
  `design/renders/rework/` (incl. full build sequences).

Research (all sourced, in `research/updates-2026-08-26/`):
trackers-A/B.md (registry ecosystem), alpoge-s6.md (the S⁶ PDF),
jacobian-elliptic.md (verification status), socials-sweep.md,
new-models.md (Epoch ECI data). `research/llm-proof-results.md`
gained a "## Deck updates 26 Aug" audit section (every new row with
tier + URLs, drop decisions, reserves).

Figures regenerated (pipeline cloned to `model-progress/`, Würzburg
copy untouched): fig3_eci_frontier + fig5_open_weight_lag rebuilt
from Epoch's live 26 Aug export (198 scored models). Kimi K3 is the
new open-weights record (157.49); frontier leader is Claude Fable 5
162.49 (NOT Opus 5 — new-models.md's headline is wrong, Epoch
refit). Qwen 3.8 27B has no Epoch ECI; estimated 153.7 ± 3.9 by 2PL
IRT inversion of vendor-reported GPQA/HLE (documented in
`model-progress/results/key_numbers.md`), drawn as hollow dashed
diamond marked "estimated". Same-snapshot refreshes of fig1/2/4 are
parked in `model-progress/figures-refreshed/`.

### NEXT STEPS (updated after resume, 26 Aug)

1. ~~Embed regenerated figures~~ **DONE**: fig3 → s-eci (caption:
   13.7 pts/yr, 4.4 months behind via Kimi K3), refreshed fig2 →
   s-bench (GPQA dead at 94.8%), fig5 → s-openweight, reframed
   around Qwen 3.8 27B ("first truly capable model that fits one
   consumer GPU, RTX 3090 24 GB"; Qwen ECI flagged as estimated).
   All snapshot captions now 2026-08-26. Em dashes also purged from
   the matplotlib titles in `model-progress/analyse.py` and all
   figures regenerated dash-free. Spoken caveats: Kimi K3 licence
   is non-commercial; Qwen ECI estimated from vendor-reported
   scores (153.7 ± 3.9).
2. ~~arXiv acknowledgment figure~~ **DONE**: embedded as fullbleed
   slide s-arxivack (slide 7, right after s-floodstats). Deck is
   now **67 slides**. Headline on slide: quant-ph 0% through 2023
   → 14% Jul 2026 (math-ph 10.8%). Spoken lines: of 59
   acknowledgments 16 credit the LLM for RESEARCH CONTENT
   ("GPT-5.6 Pro suggested Lemma 4.6"), all 16 from 2026; it is a
   disclosure rate, not a usage rate (stylometric estimates run
   far higher, see `arxiv-acknowledgments/README.md`).
   All four touched slides render-verified (Playwright, zero
   overflow/overlap; renders `design/renders/rework/embed-*.png`).
3. **Beamer `slides/talk.tex` is NOT synced** — still the old
   74-page structure/content. Decide whether to port or present
   from HTML only.
4. Manual pre-talk checks: Tao blog quotes (fetches were 403'd,
   only secondary sources); arXiv:2608.00222 author line; slide 5
   reserves if a row needs swapping (ω < 2.371177 matrix-mult is
   the strongest reserve; also Crouzeix, Kourovka, Carathéodory).
   Kept off slides deliberately: Yau–Tian–Donaldson claim (failed
   reproduction), Sendov (conflicting tracker info), IMO 2026 42/42
   (only Celia + dots-note 3.0 officially graded).
5. Rehearse with timing — 66–67 slides for 60 min.
6. Pre-existing minor render findings (predate rework, benign):
   s-context edge segment, s-agent/s-nocloning SVG text metrics,
   s-defense, s-outsource, s-becon-margin.

Errata fixed in the München decks only: arXiv:2602.12176 is
"Single-minus gluon tree amplitudes are nonzero" (gauge-theory
amplitudes, no IAS author) — NOT string theory. **The Würzburg deck
still carries the wrong caption.**

Other deliberate overrules: "18 months behind" title vs ~9-month
data line (speaker's choice); Astra paired with Opus 4.5's
SWE-bench threshold; unverified Faros "+441.5%" rounded on slide.

## Current state (earlier seminar material)

**Slides rebuilt twice** — first from v1 review notes, then refined
from v2 annotations (annotated PDF + two voice memo transcripts).

### Build system

- **Engine**: LuaLaTeX (TeX Live 2023)
- **Theme**: Custom `TJO` Beamer theme (`slides/beamer*TJO.sty`)
- **Fonts**: Whitney (text), MathTime Pro 2 (math), Iosevka Custom (code)
- **Colors**: Whitney Teal palette (dk2=#335B74, accent1=#1CADE4)
- **Build**: `make` at project root builds `slides/seminar.pdf`

### Sections (5 sections + freestyle, 54 slides total)

| Section | Slides | Content |
|---------|--------|---------|
| 00: Why this talk? | 14 | GPT-5.2 headline, timeline, survey, personal confession, skepticism, evidence, mental model ("unhinged MSc student"), the gap, three requirements, formalization, accelerating research, transition |
| 01: What is an LLM? | 12 | From outside looking in, stateless, nondeterministic, probability distribution, temperature/Boltzmann, limits, tokens, inference, Transformers references, closing statement |
| 02: The illusion of chat | 10 | Single API call, cURL reality, HTTP reality, how chat works, no memory, context window (bar chart), context rot, system prompt, closing statement |
| 03: From function to agent | 11 | Two ways in (web vs terminal), coding agents intro, agent loop (code + diagram), tools (+ Thorsten Ball ref), LLM never executes, two tools, production equivalence, live demo |
| 04: Beyond the loop | 8 | Real workflow, bash polling loop, multi-agent orchestration, natural endpoint, limitations (3 points), automation spectrum (Labour→Cognition) |
| 05: Live demo — FeO | — | Audience challenge: compute FeO potential energy curves (see `05-live-demo-feo/README.md`) |
| Freestyle | 1 | "Let's try something / No promises" |

### Key files

```
slides/
  beamerthemeTJO.sty          # Master theme (loads 4 sub-themes)
  beamercolorthemeTJO.sty     # Whitney Teal color palette
  beamerfontthemeTJO.sty      # Whitney + MathTime Pro 2 + Iosevka
  beamerinnerthemeTJO.sty     # Title page (with logos), section dividers, statement slides, codeblock
  beamerouterthemeTJO.sty     # Frame title + cyan accent line, footline
  preamble.tex                # Shared packages, TikZ styles, math shortcuts, logo paths
  seminar.tex                 # Unified deck (all sections)
  assets/
    gpt52pr.PNG               # GPT-5.2 press release screenshot
    Innovailia_logo_2.png     # InnovAILia logo
    Logo-Paket/               # LUH logos (RGB, CMYK, S-W, Pantone)
Makefile                      # Build system
notes/
  old/                        # v1 review materials (archived)
    REMEDIATION_PLAN.md
    REVIEW_SYNTHESIS.md
    voice_memo_transcript.txt
    annotatedslides.pdf
    seminarnotes.pdf
  seminar.pdf                 # Current annotated slides (v2)
  Seminar v2.m4a              # Voice memo (v2)
  Seminar_v2_transcript.md    # Whisper transcript (tiny model)
  Seminar v2 transcripts .txt # Second transcript (alternative ASR)
```

### Demo code

- `01-*/demo.py` — Temperature sweep showing nondeterminism (fun prompt about fictional particles)
- `02-*/single_call.py` — Raw API call with JSON payload
- `02-*/chat_loop.py` — Terminal chat showing history growth
- `02-*/curl_call.sh` — Standalone cURL demo matching the slide (`KEY` env var required)
- `03-*/agent.py` — 124-line agent with read/write tools
- `03-*/tools.py` — Sandboxed file tools
- `03-*/workspace/data.csv` — Sample data file for agent demo
- `05-*/smoke_test_feo.py` — Single-point CASSCF+NEVPT2 validation
- `05-*/compute_feo_pec.py` — Production PEC scan (SA-CASSCF(12,12) + SC-NEVPT2, X2C, DK basis)
- `05-*/plot_feo_pec.py` — PEC plotting and spectroscopic constants extraction

### Changes in v2 (from v1)

Applied from annotated slides PDF + two voice memo transcripts:

- **Survey slide**: Removed "used" prefix, added question marks
- **Personal confession**: "tried" → "experimented", added "for research", comma → colon
- **Untrustworthy**: Removed italic and quote marks
- **Evidence**: Left-aligned bullet text, teal conclusion stays centered
- **Mental model**: "deranged" → "unhinged", removed trailing comma
- **Project showcase slide**: Deleted (felt like bragging)
- **Formalization**: TODO placeholder for auto-formalization screenshot
- **From outside, looking in**: Removed "From" and "entire", left-aligned text
- **Probability distribution**: "over tokens" merged into first line, added "one after another"
- **Two ways in**: Moved "same API underneath" label below arrow to avoid overlap
- **New "Coding agents" slide**: Intro slide before agent loop ("Empowering LLMs with autonomous tool use")
- **Tools slide**: Added Thorsten Ball "How to Build an Agent" reference (ampcode.com)
- **Be skeptical**: Removed title bar, kept 3 content points as plain slide
- **New "Automation" slide**: Labour→Cognition spectrum (Calculator, CAS, Automated proving, AI tools)
- **Removed "Live coding" section divider**: Kept "Let's try something" slide
- **Context rot**: Left-aligned the three body statements
- **Timeline**: Rebalanced box spacing
- **Transformers slide**: New references slide (Vaswani, Karpathy, Alammar, PicoGPT.jl)

### Known issues / TODOs

- Insert screenshot of auto-formalization project after the formalization slide
- Add picture of transformer architecture to the Transformers references slide
- Check Nondeterministic slide for text overflow (P(next token|context) may clip)
- Minor overfull hbox warnings on some code blocks (inherent to verbatim in beamer)

### Style guide

A comprehensive style guide lives at `~/Projects/presentations/STYLE_GUIDE.md`.

### LaTeX talk script

A full written script of the talk, typeset as lecture notes using the
same `amsart` + custom style template as `~/Projects/quantum-noise-and-decoherence/`.

- **Engine**: pdfLaTeX (TeX Live 2023), Computer Modern fonts (portable)
- **Master doc**: `latex/LLMSeminar.tex`
- **Style**: `latex/talk-style.sty` (adapted from `qnd-style.sty` — same color palette, boxes, theorem environments, plus `audience` box and `listings` for code)
- **Macros**: `latex/talk-macros.sty` (LLM-specific: `\Str`, `\Tok`, `\Prob`, TikZ component styles)
- **Bibliography**: `latex/references.bib`
- **Build**: `cd latex && pdflatex LLMSeminar && bibtex LLMSeminar && pdflatex LLMSeminar && pdflatex LLMSeminar`

| Section file | Title | Content |
|---|---|---|
| `sections/sec00.tex` | Why this talk? | GPT-5.2, timeline, survey, skeptic's confession, the paradox, mental model, the gap, requirements |
| `sections/sec01.tex` | What is an LLM? | f: String→String, stateless, nondeterministic, temperature/Boltzmann, tokens, inference, summary |
| `sections/sec02.tex` | The illusion of chat | API calls, how chat works, context window, context rot, system prompt |
| `sections/sec03.tex` | From function to agent | Agent loop, tools, key insight, feedback, live demo narrative |
| `sections/sec04.tex` | Beyond the loop | Bash orchestration, multi-agent, limitations, automation spectrum |
| `sections/sec05.tex` | Applications and discussion | Examples, FeO computation, Q&A highlights (lit reviews, security, reasoning, correctness, formalisation) |

### Transcript

YouTube auto-captions downloaded and cleaned: `transcripts/talk_clean.txt`
(90 paragraphs, 87 minutes). Raw VTT at `transcripts/talk_audio.en.vtt`.

## What to do next

- Provide auto-formalization screenshot and transformer architecture image
- Rehearse with timing — 54 slides for 60 minutes is comfortable
- Prepare live demo environment (Claude Code terminal + web interface)

## Technical notes

- `codeblock` uses `tcblisting` (verbatim) — frames containing it need
  `[fragile]`, and `\begin{codeblock}` / `\end{codeblock}` must start
  at column 0 (no leading whitespace)
- Font loading order in `beamerfontthemeTJO.sty` is critical:
  `luatex85` → `mtpro2[lite]` → `fontspec[no-math]`
- Whitney font path: `/usr/share/fonts/opentype/whitney/` (system install)
- Iosevka: loaded via fontconfig name lookup (no hardcoded path)
- All demo scripts use model ID `claude-sonnet-4-6` (no date suffix)
- Logo paths defined in `preamble.tex` via `\luhlogo` and `\innovailialogo`
- TikZ decorations library (`decorations.pathreplacing`) loaded for context window brace
