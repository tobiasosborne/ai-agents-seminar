# SPEC — Würzburg Physikalisches Kolloquium talk

**Deliverable**: `Wuerzburg-talk-2026/slides/talk.tex` (+ `demo/demo_prompt.md`),
compiling clean with `make` (lualatex, two passes) in this directory.

**HARD CONSTRAINT**: Another agent is working elsewhere in `Wuerzburg-talk-2026/`.
Write ONLY inside `Wuerzburg-talk-2026/slides/`. Everything else in the repo is
read-only reference material. Do not regenerate figures; reference them in place.

## The engagement

- Physikalisches Kolloquium, Julius-Maximilians-Universität Würzburg
- Monday **13 July 2026**, 14:15, Röntgen-Hörsaal + Zoom
- Speaker: Prof. Dr. Tobias J. Osborne, Leibniz Universität Hannover
- Title: **Large language models: A physicist's perspective**
- Duration: ~60 minutes (colloquium). Target **~36–40 slides**.

The abstract (must be honored by the deck): transformer as a stateless function
made stochastic by sampling; rebuild the agent stack from first principles from
a raw cURL call — chat as scaffolded API calls, agents as while loops with tool
calls, context management as the reason chat interfaces silently ruin results,
multi-agent orchestration as the natural endpoint; skepticism — the gap between
"I tried ChatGPT and it hallucinated" and "powerful force multiplier" is closed
by technique and domain expertise, not better models; a little live coding.

## Sources (all read-only)

- **Base deck to adapt**: `gc-conference-2026/slides/talk.tex` (27 slides, same
  theme, same TikZ styles — reuse frames verbatim where the outline says so).
- **Seminar deck** (54 slides, richer material): `slides/seminar.tex` at repo
  root — take the audience survey, cURL/single-API-call, how-chat-works,
  tokens, and context-rot frames from here (adapt to this preamble's macros;
  check what `slides/preamble.tex` defines vs our local `preamble.tex` and
  inline anything missing rather than editing the theme).
- **Style guide**: `~/Projects/presentations/STYLE_GUIDE.md`.
- **Grade-decorrelation figures**: `../grade-decorrelation/figures/scatter_2020.pdf`
  … `scatter_2025.pdf`, `scatter_grid.pdf`, `gradient_by_year.pdf`,
  `distributions.pdf`. Numbers in `../grade-decorrelation/README.md` and
  `../grade-decorrelation/results/regression_summary.md`.
- **Model-progress figures**: `../model-progress/figures/fig1_gpqa_dead.pdf`,
  `fig2_benchmark_ladder.pdf`, `fig3_eci_frontier.pdf`, `fig4_cadence.pdf`,
  `fig5_open_weight_lag.pdf`. Numbers in `../model-progress/results/key_numbers.md`.
- Local `assets/`: `gpt52pr.PNG` (OpenAI string-theory paper press screenshot),
  LUH logos, InnovAILia logo. A second image `assets/unitdistance_pr.png` is
  being produced by another agent IN PARALLEL — it will likely NOT exist while
  you work. Include it via an `\IfFileExists` guard with a visible placeholder
  box in the else-branch, so the deck compiles either way.

## Slide-by-slide outline

Section dividers use `\sectiondivider{...}`; big claims use `\statementslide{...}`
(both defined by the theme — see how the GC deck uses them).

### Title
1. `\titlepage` with `\date{Physikalisches Kolloquium, Universität Würzburg — 13 July 2026}`.

### Part 1 — Why this talk? (`\sectiondivider{Why this talk?}`)
2. **Hook A — unit-distance problem**: full-bleed screenshot slide,
   `assets/unitdistance_pr.png` (IfFileExists guard). Small caption line under
   it (source/date) — mirror the GPT-5.2 slide layout. Leave the caption text
   as `\unitdistancecaption` — define this macro near the top of talk.tex with
   placeholder text `TODO: source line` so it is easy to patch later.
3. **Hook B — OpenAI string theory paper**: the existing GPT-5.2 press slide
   from the GC deck (`assets/gpt52pr.PNG`, arXiv:2602.12176 caption), verbatim.
4–7. **Hook C — grade decorrelation** (4 slides):
   - "A control experiment run on us" framing slide: first-year theoretical
     physics; weekly assignments (out of 100) vs invigilated final exam (out
     of 10); 2020–2023 the two agree (gradient ≈ 0.10 = perfect agreement in
     percentage terms).
   - `scatter_2020.pdf` next to `scatter_2022.pdf` OR just `scatter_2020.pdf`
     full width, gradient 0.099, r = 0.79.
   - `scatter_2025.pdf`: gradient 0.015, r = 0.08, n.s. — "the assignment
     stopped measuring anything the exam measures".
   - `scatter_grid.pdf` OR `gradient_by_year.pdf` as the punchline: the
     collapse in one image. Pooled interaction d = −0.063, p ≈ 1e−7.
   - **Every one of these slides must carry a small grey caption:
     "Synthetic data, illustrative — reproduces the structure of the real
     six-year analysis."** This is non-negotiable (see the README's honesty
     section). The exam is the control: its distribution is stationary; AI
     adoption is uncorrelated with ability — that is the whole mechanism.
8. **Audience survey** — adapt from seminar deck (hands-up questions: who has
   used ChatGPT? who uses it for research? who has used a coding agent?).
9. **Timeline — four moments** (extend GC deck's three-moment TikZ timeline):
   Nov 2022 ChatGPT · Q1 2025 Claude Code/Cursor/Copilot · Q4 2025 Opus 4.5,
   GPT-5.2 cross a threshold · Q2 2026 Fable 5, GPT-5.6, GLM-5.2.
10. Statement: LLMs are **incredibly capable** but **maximally untrustworthy**
    (GC deck, verbatim).
11. **The gap** slide (GC deck, verbatim).

### Part 2 — What is an LLM? (`\sectiondivider{What is an LLM?}`)
12. Statement: LLMs supply (somewhat) **general-purpose intelligence** — new;
    keep it short, e.g. "A new kind of resource: general-purpose intelligence,
    bought by the token" with the caveat "(somewhat)".
13. `f : String -> String` (GC deck).
14. Nondeterministic (GC deck).
15. Temperature / Boltzmann (GC deck).
16. Tokens (from seminar deck — the tokenization slide).
17. Closing definition statement (GC deck: stateless, nondeterministic,
    samples from P(next token | context), frozen network).

### Part 3 — The illusion of chat (`\sectiondivider{The illusion of chat}`)
18. **A single API call** — the cURL slide from the seminar deck (abstract
    explicitly promises "the foundation of a raw cURL call").
19. **How chat works** — history re-sent every turn (seminar deck).
20. **Context window** diagram (GC deck version, which merged window+rot).
21. **Context rot** (seminar deck version) — degradation as context fills.
22. **Compaction** — NEW slide: when the window fills, the conversation is
    summarized and the summary replaces the history; lossy by construction;
    you don't control what survives. Simple TikZ: long bar → small bar labeled
    "summary" + fresh space. Closing line: "Chat interfaces do this silently —
    this is why long chats go off the rails."

### Part 4 — From function to agent (`\sectiondivider{From function to agent}`)
23. Agent loop code (GC deck).
24. Agent loop diagram (GC deck).
25. Statement: The LLM never executes anything (GC deck).
26. **Feedback stabilises — closing the loop** — NEW: tool results flow back
    into context; errors become corrections; physics framing welcome (open-loop
    vs closed-loop / feedback stabilises an unstable system). Keep honest and
    plain.
27. **Filesystem = permanent memory** — NEW, this is the talk's core new claim:
    the filesystem gives (i) memory that survives the context window, (ii)
    ground truth that stabilises hallucination — the model can re-read what is
    actually there instead of half-remembering it. Punchline: **the radical
    unlock vs. chat**. Suggested layout: two-column tjo boxes "Chat: context is
    the only state (evaporates, rots)" vs "Agent: filesystem is the state
    (persistent, checkable, versioned)".
28. **Subagents** — adapt GC deck's multi-agent orchestration slide: supervisor
    delegates to fresh-context workers; each subagent gets a clean context
    window; results return as short reports. One line: "context isolation is
    the point".
29. Adversarial verification (GC deck, verbatim or lightly adapted).

### Part 5 — Live demo (`\sectiondivider{Live demo}`)
30. Demo slide: "Let's try something — no promises." plus one line: the prompt
    is pre-written; paste into Claude Code. Also write `demo/demo_prompt.md`
    containing 2–3 candidate pre-written prompts, physics-flavoured, each
    completable in ~3–5 minutes by a coding agent live (e.g. damped driven
    pendulum phase portrait from scratch + png; fetch/plot something offline-safe;
    small data-analysis task on a CSV it generates itself). Mark one as the
    primary. No API keys in the file.

### Part 6 — Intelligence growth (`\sectiondivider{The trend}`)
31. `fig3_eci_frontier.pdf` full-width: capability is a straight line,
    13 ECI points/year; open weights 6.9 months behind (GLM-5.2).
32. `fig2_benchmark_ladder.pdf` or `fig1_gpqa_dead.pdf`: benchmarks saturate
    and are replaced; GPQA (PhD-level science QA) is dead at 94.6%; research
    physics (CritPt) still at 32% — "the frontier is now research-grade work".
33. `fig5_open_weight_lag.pdf`: open-weight models — you can run
    frontier-minus-7-months physics locally; no vendor lock-in.
    (Source line on each: Epoch AI Benchmarking Hub, CC-BY, snapshot 2026-07-12.)

### Part 7 — The harder problem / closing (`\sectiondivider{The harder problem}`)
34. Why LLMs fail at research (GC deck: undergraduate vs research phase
    transition).
35. The renaissance expert (GC deck — it's in the current working-tree version).
36. The single point of failure / structural taste (GC deck, working-tree).
37. Limitations statement (GC deck: every layer has failure modes; human in
    the loop is not optional).
38. Automation spectrum (GC deck).
39. Summary (GC deck's 4-line table, adjust line 3 to include "filesystem as
    ground truth").
40. **Call to action** — NEW final slide: "Try it this week." Three concrete
    tools in tjo boxes: **Claude Code** (terminal agent), **Codex** (OpenAI),
    **Pi via OpenRouter** (open-weight/open-router option). One closing line
    inviting them to bring a real research problem, not a toy.

## Style rules

- Follow `~/Projects/presentations/STYLE_GUIDE.md` and the existing decks: one
  idea per slide, generous whitespace, `\vfill` sandwiches, statement slides
  for the load-bearing claims, Whitney Teal palette (`tjo@darkteal`,
  `tjo@cyan`, `tjo@lightgrey`), no bullet walls.
- Frames containing `codeblock` need `[fragile]` and `\begin{codeblock}` at
  column 0 (no leading whitespace) — see existing decks.
- External figures: `\includegraphics[height=0.78\textheight]{...}` typically;
  PDFs preferred over PNGs.
- Keep German out; the talk is in English.
- You may deviate from this outline where something clearly works better —
  note any deviation in a comment `% SPEC-DEVIATION: ...` at the frame.

## Build & verify

```bash
cd Wuerzburg-talk-2026/slides && make
```

Must complete with exit 0, two passes, no missing figures (the
unitdistance_pr.png guard handles the one legitimately-missing asset). Check
the log for overfull hboxes > 20pt and fix layout where they occur (verbatim
codeblock overfulls are tolerated). Render a few pages to PNG
(`pdftoppm -png -r 60 -f N -l N talk.pdf page`) and eyeball the new slides
(grade-decorrelation sequence, filesystem slide, compaction diagram, call to
action) for overlap/clipping.
