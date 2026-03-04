# Remediation Plan (v2 — includes voice memo)

Changes derived from all four sources:
1. Annotated slides (`annotatedslides.pdf`)
2. Handwritten notes (`seminarnotes.pdf`)
3. Voice memo (`Ai seminar notes.m4a` — transcribed)
4. Official title/abstract

**Official title**: "Large Language Models: A Physicist's Perspective"

---

## GAP ANALYSIS: Abstract vs. Current Slides

| Abstract topic | Current coverage | Gap |
|---|---|---|
| "transformer as a stateless function whose output is made stochastic by sampling" | Section 01 — good | Minor: add "sampling" emphasis |
| "raw cURL call to an API" | Section 02 HTTP reality — partial | Needs: actual `curl` command on slide |
| "chat as scaffolded API calls" | Section 02 — good | OK |
| "agents as while loops with tool calls" | Section 03 — good | OK |
| "**context management as the reason chat interfaces silently ruin your results**" | One slide on context window | **MAJOR GAP**: needs 2–3 slides on context rot |
| "**bash polling loops as infrastructure**" | Not in slides at all | **MAJOR GAP**: new content needed |
| "**multi-agent orchestration as the natural endpoint**" | Not in slides at all | **MAJOR GAP**: new content needed |
| "deliberate practice + understanding limitations" | "1000+ hours" (being replaced) | Being addressed |
| "gap between 'tried ChatGPT' and 'force multiplier'" | Not explicit | Need statement slide |
| "closed by technique and domain expertise, not better models" | Not stated | Need statement slide |
| "live coding, no promises" | LIVE DEMO slide exists | Soften + freestyle |

---

## GLOBAL STYLE FIX: Remove trailing punctuation

**From voice memo** (repeated multiple times): "I don't like full stops. Get rid of those full stops."

This applies to ALL statement slides. Remove trailing periods from:
- "Chat is a loop**.**" → "Chat is a loop"
- "Memory is an illusion maintained by the client**.**" → same without period
- "The LLM never executes anything**.**" → same
- "That is enough to do useful work**.**" → same
- "Watch the agent work**.**" → same
- Every other statement slide with trailing punctuation

---

## Phase 0: Title and framing

### 0.1 — Title slide (`section00.tex` slide 1)
- **Title**: "Large Language Models"
- **Subtitle**: "A Physicist's Perspective"
- **Author**: Tobias J. Osborne
- **Affiliation**: Leibniz Universität Hannover
- **Logos**: LUH logo (`slides/assets/Logo-Paket/RGB/luh_logo_rgb_0_81_158.png`) + InnovAILia logo (`slides/assets/Innovailia_logo_2.png`)
- Requires: update `\title`, `\subtitle`, `\author` in section00.tex, and add logo placement to title page (may need `beamerinnerthemeTJO.sty` update)

---

## Phase 1: Structural cuts and replacements

### 1.1 — Replace "1000+ hours" slide (`section00.tex` slide 8)
**Voice memo**: "I just don't like that it looks boastful. I definitely don't want to give off that sense of humble brag."
**Replace with** three-point slide:
1. **Deliberate practice is required** — alien tech, completely different workflow
2. **You need to pay** — free chat is not enough
3. **Install a coding agent** — Claude Code, Cline, etc. for full power

### 1.2 — Rework "What I built" slides (`section00.tex` slides 9–10)
**Voice memo**: "I don't want to have a list of like, oh look how cool I am."
- **Keep first project table** (slide 9) but reframe: "With the correct workflow, amazing things are possible"
- **Cut second project table** (slide 10) entirely
- **Replace with focus on formalization**: "Auto formalization is real. Writing new science is now possible."
- Add: "All with basic tooling — no extra subscriptions"

### 1.3 — Replace "All of this was built with AI coding agents" (`section00.tex` slide 11)
**Replace with**: "Accelerating research is possible — with correct tooling and expert guidance"
**Voice memo adds**: "human = ground truth" — the human-in-the-loop provides the ground truth

### 1.4 — Replace "Let me show you the entire trick" (`section00.tex` slide 12)
**Voice memo**: "I hate magic and mystery" / "LLMs can be understood" / "ground up to coding agents"
**Replace with**: "LLMs can be understood" as statement slide
Speaker note: purpose is to explain how LLMs work so physicists can exploit them and understand strange behaviors

### 1.5 — Gut Section 04
**Voice memo**: "I don't like that. It's good to go. These examples, just like that couple that crap. Don't want it. I'm going to freestyle that. And definitely no raise your hand."
- **Cut** the section divider (WHAT SHOULD WE TRY?)
- **Cut** Option 1 (LaTeX lint) — crossed out on annotated slides
- **Cut** "Raise your hand" vote slide — crossed out
- **Keep** Options 2–6 as available backup if needed during freestyle
- Freestyle the live demo section

---

## Phase 2: New slides to insert

### 2.1 — GPT 5.2 physics result (`section00.tex`, after "Why this talk?" divider, BEFORE "Three moments")
**Voice memo**: "insert a screen cap of a press release by OpenAI... should be enough to make theoretical physicists go, uh-huh, and be somewhat existentially concerned"
- Use `slides/assets/gpt52pr.PNG` as a full-slide or near-full-slide image
- Headline: "GPT-5.2 derives a new result in theoretical physics"
- Subtitle: arXiv:2602.12176 — "Single-minus gluon tree amplitudes are nonzero"
- Feb 13, 2026 — IAS, Harvard, Cambridge, Vanderbilt, OpenAI

### 2.2 — Personal confession (`section00.tex`, after survey, before "I was a skeptic")
**Voice memo**: "if you experimented with chat in Q1 2025, you may have dismissed LLMs as being useful for anything but a very limited set of use cases. And I did."
Statement slide: "If you experimented with chat in Q1 2025, you probably dismissed LLMs. I did."

### 2.3 — Mental model slide (`section00.tex`, after "The evidence")
**Voice memo**: "it's good to have a mental model of LLM and mine is slightly deranged hypermotivated MSc student. It'll be kind of fun to have a picture here."
- Statement slide with image
- **TODO**: find a suitable humorous image

### 2.4 — "The gap" statement slide (`section00.tex`, near the "three requirements")
From abstract: "The gap between 'I tried ChatGPT and it hallucinated' and 'this is a powerful force multiplier for research' is not closed by better models. It is closed by technique and domain expertise."

### 2.5 — "LLM outputs a distribution" (`section01.tex`, between Nondeterministic and Temperature)
**Voice memo**: "there's a kind of missing slide here. An LLM produces a probability distribution and it samples from it."
Statement/diagram slide bridging nondeterminism → Boltzmann formula

### 2.6 — cURL slide (`section02.tex`, after or enhancing HTTP reality)
Abstract says "raw cURL call to an API" — make this literal:
```
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $KEY" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-6",
       "messages":[{"role":"user",
                    "content":"What is a quark?"}]}'
```

### 2.7 — Context window visual (`section02.tex`, replacing current text-only slide)
**Voice memo**: "I need a bar chart with an underbrace, tokens, context length"
- Redesign as a TikZ bar/rectangle with `\underbrace` showing token count
- Label regions: system prompt, conversation history, latest message
- Show what happens when it overflows

### 2.8 — Context rot / amnesia (`section02.tex`, after context window)
**Voice memo**: "that's why they get amnesia. There needs to be a context rot slide."
New slide(s):
- "Context rot" — as conversation grows, older information degrades
- This is why chat interfaces silently ruin your results (abstract language)
- Statement: "This is why ChatGPT 'hallucinates' on long tasks — it's not the model, it's the context"

### 2.9 — Web interface vs terminal (`section03.tex`, before agent loop)
**Voice memo**: "extra slide. Web interface as a demonstration. Demo is chat. And then I'll have a terminal open for the API call."
- Slide setting up the demo: web UI (chat interface) vs terminal (raw API)
- Bridges Section 02 → Section 03

### 2.10 — Bash polling loops (NEW — required by abstract)
Abstract: "bash polling loops as infrastructure"
Possible slides:
1. Section divider or statement: "INFRASTRUCTURE" or "THE REAL WORKFLOW"
2. Show a bash loop that launches an agent, polls for completion, checks results
3. Statement: "A bash loop is the simplest orchestrator"

### 2.11 — Multi-agent orchestration (NEW — required by abstract)
Abstract: "multi-agent orchestration as the natural endpoint"
Possible slides:
1. Diagram: multiple agents with different roles coordinated by a supervisor
2. Statement: "One agent writes code. Another reviews it. A third runs the tests."
3. "The natural endpoint" — from single function → agent → multi-agent

---

## Phase 3: Minor edits and polish

### 3.1 — Timeline: eliminate dots (`section00.tex` slide 3)
**Voice memo**: "three blue dots that need to be eliminated, they don't look correct"
Remove the `\foreach` loop drawing cyan dots.

### 3.2 — Survey slide rework (`section00.tex` slide 4)
**Voice memo**: clear three-tier hierarchy:
1. "used ChatGPT, Claude, Gemini in chat"
2. "used an IDE + LLM to write code (Cursor, Copilot)"
3. "used Claude Code or a coding agent"
Title → "Quick survey: Experience" (drop "Raise your hand if you have..." — say it aloud instead)

### 3.3 — "I was a skeptic" elaboration (`section00.tex` slide 5)
Add: "I am still annoyed at the models of Q1 2025"

### 3.4 — "Maximally untrustworthy" elaboration (`section00.tex` slide 6)
Add: "They lie, cheat, steal, and flatter — all terrible for reproducible science"

### 3.5 — "The observable interface" rename (`section01.tex` slide 2)
**Voice memo**: "I don't like the word observable interface. Just say a large language model. From the outside, looking in."
Rename to: "From outside, looking in" or similar

### 3.6 — Nondeterministic: fix missing text (`section01.tex` slide 4)
**Voice memo**: "missing text" after "the model samples from"
Add `"..."` to output boxes and ensure the P(next token|context) text is complete

### 3.7 — Tokens: [Token]^n correction (`section01.tex` slide 7)
Add: "More precisely: $f : \text{Token}^* \to \text{Token}^*$"

### 3.8 — Inference: add "LLM =" (`section01.tex` slide 8)
"An LLM call = one forward pass through a frozen neural network"

### 3.9 — Section 01 Summary: remove heading (`section01.tex` slide 9)
**Voice memo**: "I can't read a summary. We're not summarizing."
Remove the "Summary" title. Keep the content as a closing statement slide.

### 3.10 — "A single API call": add framing (`section02.tex` slide 2)
**Voice memo**: "you interact with LLM via a single API call"
Add context above or as subtitle.

### 3.11 — Context window labels (`section02.tex` slide 6)
8k = "free chat interface", 200k = "paid frontier model"
(Being redesigned as bar chart — see Phase 2.7)

### 3.12 — System prompt: add link (`section02.tex` slide 7)
**Voice memo**: "link to the Anthropic prompt that was leaked, just a webpage address"
Add URL reference.

### 3.13 — "Tool definition" → "Tools" (`section03.tex` slide 4)
Rename frame title.

### 3.14 — Agent loop diagram: fix arrow (`section03.tex` slide 3)
**Voice memo**: "the arrow coming from execute tools should come back in around and into the LLM box"
Fix the TikZ arrow routing so results feed back into the LLM node properly.

### 3.15 — LIVE DEMO: soften + freestyle (`section03.tex` slide 8)
"LIVE DEMO" / "Let's try some live coding — no promises"
No structured vote. Freestyle.

### 3.16 — Remove trailing punctuation (GLOBAL)
Remove full stops from all statement slides:
- `section02.tex`: "Chat is a loop." → "Chat is a loop"
- `section02.tex`: "maintained by the client." → "maintained by the client"
- `section03.tex`: "The LLM never executes anything." → remove period
- `section03.tex`: "That is enough to do useful work." → remove period
- `section03.tex`: "better prompts." → remove period
- `section03.tex`: "Watch the agent work." → remove period
- All others with trailing periods on statement/large-text slides

---

## Phase 4: Assets

| Asset | File | Status |
|-------|------|--------|
| LUH logo (RGB PNG) | `slides/assets/Logo-Paket/RGB/luh_logo_rgb_0_81_158.png` | READY |
| InnovAILia logo | `slides/assets/Innovailia_logo_2.png` | READY |
| GPT-5.2 press release screenshot | `slides/assets/gpt52pr.PNG` | READY |
| "Deranged MSc student" image | TBD | TODO |
| Anthropic system prompt URL | TBD (find the leaked/published URL) | TODO |

---

## Implementation order

1. **Phase 0** — Title/subtitle/affiliation/logos
2. **Global** — Remove trailing punctuation from all statement slides
3. **Phase 1** — Structural cuts and replacements (1000hrs, project pages, punchlines, section 04)
4. **Phase 2.1–2.4** — New Section 00 slides (GPT-5.2, confession, mental model, "the gap")
5. **Phase 2.5** — Insert distribution slide in Section 01
6. **Phase 2.6–2.8** — Section 02 expansion (cURL, context bar chart, context rot)
7. **Phase 2.9** — Web vs terminal slide in Section 03
8. **Phase 3** — All minor edits and polish
9. **Phase 2.10–2.11** — Bash polling + multi-agent (new content, may need new section file)
10. **Phase 1.5** — Rework Section 04 for freestyle
11. Build full deck, review, rehearse

---

## Proposed final structure

| Section | File | Est. slides | Content |
|---------|------|-------------|---------|
| 00 | `section00.tex` | ~15 | WHY: GPT-5.2 headline, timeline, survey, personal story, skepticism, evidence, mental model, "the gap", three requirements, projects (brief), formalization, transition |
| 01 | `section01.tex` | ~10 | LLM: from outside looking in, stateless, nondeterministic, prob distribution, temperature, limits, tokens, inference, closing statement |
| 02 | `section02.tex` | ~12 | CHAT: single API call, cURL, HTTP reality, how chat works, no memory, context window (bar chart), context rot/amnesia, system prompt, closing statement |
| 03 | `section03.tex` | ~10 | AGENT: web vs terminal, agent loop (code), agent loop (diagram, fixed), tools, LLM never executes, two tools, production equivalence, live demo |
| 04 | `section04.tex` | ~6 | BEYOND: bash polling loops, multi-agent orchestration, "the natural endpoint" |
| 05 | `section05.tex` | ~2 | LIVE: freestyle demo, backup options |
| **Total** | | **~55** | Comfortable for 60 min |
