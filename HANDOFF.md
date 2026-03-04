# Handoff: AI Agents Seminar

## What this is

Materials for a 1-hour seminar: "Large Language Models: A Physicist's
Perspective." Demystifies LLMs and AI coding agents by rebuilding the
entire stack from first principles for a physics audience.

## Current state

**Slides are fully rebuilt** from review notes (annotated slides,
handwritten notes, voice memo) with a custom LaTeX Beamer system.

### Build system

- **Engine**: LuaLaTeX (TeX Live 2023)
- **Theme**: Custom `TJO` Beamer theme (`slides/beamer*TJO.sty`)
- **Fonts**: Whitney (text), MathTime Pro 2 (math), Iosevka Custom (code)
- **Colors**: Whitney Teal palette (dk2=#335B74, accent1=#1CADE4)
- **Build**: `make` at project root builds `slides/seminar.pdf`

### Sections (6 sections, 53 slides total)

| Section | Slides | Content |
|---------|--------|---------|
| 00: Why this talk? | 16 | GPT-5.2 headline, timeline, survey, personal story, skepticism, evidence, mental model, "the gap", three requirements, projects, formalization, transition |
| 01: What is an LLM? | 10 | From outside looking in, stateless, nondeterministic, probability distribution, temperature/Boltzmann, limits, tokens, inference, closing statement |
| 02: The illusion of chat | 10 | Single API call, cURL reality, HTTP reality, how chat works, no memory, context window (bar chart), context rot, system prompt, closing statement |
| 03: From function to agent | 9 | Two ways in (web vs terminal), agent loop (code + diagram), tools, LLM never executes, two tools, production equivalence, live demo |
| 04: Beyond the loop | 6 | Real workflow, bash polling loop, multi-agent orchestration diagram, natural endpoint, be skeptical |
| 05: Live coding | 2 | Section divider + "No promises" |

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
  section0[0-5].tex           # Individual section files
  assets/
    gpt52pr.PNG               # GPT-5.2 press release screenshot
    Innovailia_logo_2.png     # InnovAILia logo
    Logo-Paket/               # LUH logos (RGB, CMYK, S-W, Pantone)
Makefile                      # Build system
notes/
  REMEDIATION_PLAN.md         # Full change plan derived from review
  REVIEW_SYNTHESIS.md         # Slide-by-slide annotation extraction
  voice_memo_transcript.txt   # Whisper transcription of voice memo
  annotatedslides.pdf         # Original annotated slides
  seminarnotes.pdf            # Handwritten notes
  Ai seminar notes.m4a        # Voice memo
```

### Demo code

- `01-*/demo.py` — Temperature sweep showing nondeterminism (fun prompt about fictional particles)
- `02-*/single_call.py` — Raw API call with JSON payload
- `02-*/chat_loop.py` — Terminal chat showing history growth
- `02-*/curl_call.sh` — Standalone cURL demo matching the slide (`KEY` env var required)
- `03-*/agent.py` — 124-line agent with read/write tools
- `03-*/tools.py` — Sandboxed file tools
- `03-*/workspace/data.csv` — Sample data file for agent demo

### Changes from v1

Major rework based on review (annotated slides + handwritten notes + voice memo):

- **Title**: "Large Language Models: A Physicist's Perspective" (was "AI Coding Agents: A reductive account")
- **Logos**: LUH + InnovAILia on title slide
- **Section 00**: GPT-5.2 headline, personal confession, mental model ("deranged MSc student"), "the gap" thesis (technique > models), three requirements, formalization message. Cut: second project page, boastful punchlines.
- **Section 01**: New "probability distribution → sample" slide, renamed "From outside, looking in", Token* correction, removed "Summary" heading.
- **Section 02**: Added cURL slide, redesigned context window as bar chart with underbrace, added context rot slide, added system prompt URL.
- **Section 03**: Added "Two ways in" (web vs terminal), fixed agent loop diagram arrows, renamed "Tool definition" → "Tools".
- **Section 04**: Entirely new — bash polling loops, multi-agent orchestration, "be skeptical".
- **Section 05**: New — freestyle live coding section.
- **Global**: Removed all trailing punctuation from statement slides.

### Known issues

Minor overfull hbox warnings on some code blocks (inherent to verbatim in beamer). No content clipping.

### Style guide

A comprehensive style guide lives at `~/Projects/presentations/STYLE_GUIDE.md`.

## What to do next

- Find a humorous image for the "deranged MSc student" mental model slide
- Rehearse with timing — 53 slides for 60 minutes is comfortable
- Prepare live demo environment (Claude Code terminal + web interface)
- The old `build_slides.py` can be removed

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
