# Handoff: AI Agents Seminar

## What this is

Materials for a 1-hour seminar: "Large Language Models: A Physicist's
Perspective." Demystifies LLMs and AI coding agents by rebuilding the
entire stack from first principles for a physics audience.

## Current focus: QuSoft seminar, Amsterdam (Fri 4 Sep 2026, 11:00-12:00)

`QuSoft-talk-2026/` is a copy of the München talk (research, pipelines, decks)
adapted on 2 Sep 2026 for the Special QuSoft Seminar "The industrialization of
theoretical sciences" at CWI (Turing Room, Amsterdam Science Park; chair Jonas
Helsen; other speakers Holmes, Guo, Dominik, Renaud, Evers). **Present from
`QuSoft-talk-2026/slides-web/talk.html`** (68 slides, render-verified 4 Sep).

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
now the 68-page QuSoft export).

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
