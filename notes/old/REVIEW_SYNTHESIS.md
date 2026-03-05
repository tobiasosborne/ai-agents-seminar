# Review Synthesis: All Sources

Compiled from three sources:
1. **Annotated slides** (`annotatedslides.pdf`) — 48 pages of printed slides with red handwritten annotations
2. **Handwritten notes** (`seminarnotes.pdf`) — 1 page of dense speaker notes
3. **Voice memo** (`Ai seminar notes.m4a`) — ~15 min audio (transcription pending)

---

## Source 1: Annotated Slide Markup (slide-by-slide)

### Section 00 — "Why this talk?"

| Slide | Current content | Annotation | Interpretation |
|-------|----------------|------------|----------------|
| 1 (Title) | "AI Coding Agents / A reductive account for physicists" | "Change title"; "reductive" circled/struck; "Add affiliation, LUH + logo, InnovAILig" | Drop "reductive" from subtitle. Add LUH affiliation and InnovAILig project logo. |
| 2 (Section divider) | WHY THIS TALK? | — | No change |
| — (new) | — | "Put here the GPT 5.2 Physics Result press release" | **INSERT** new slide after divider: screenshot/headline of GPT-5.2 physics result |
| 3 (Timeline) | Three moments: Nov 2022 / Q1 2025 / Q4 2025 | "launches" circled; "Copilot" circled; "threshold" circled; "Eliminate dots" | Remove cyan timeline dots. Minor text review. |
| 4 (Survey) | "Quick survey" — raise hand bullets | Title → "Quick survey: Experience"; "move up" the "Raise your hand" prompt; add "Gemini or Chat?" to first bullet; "IDE + LLM" on second bullet; "what agent?" on third bullet | Rework survey slide with broader tool list and reorder |
| — (new) | — | "If experimented with chat in Q1 2025, dismissed LLMs! I did." | **INSERT** personal confession slide before "I was a skeptic" |
| 5 (Skeptic) | "I was a skeptic." | "I am still annoyed at models of Q1 2025" | Add qualification or make it two-beat: skeptic → still annoyed at Q1 2025 models |
| 6 (Quote) | "LLMs are incredibly capable but maximally untrustworthy" | "→ They lie, cheat, steal, flatter"; "→ All terrible for hard repro science" | Add speaker-note elaboration or bullet elaboration below quote |
| 7 (Evidence) | "Seductively correct equations..." | "LLM" underlined near "and it finds" | Minor emphasis: underline that the LLM is what finds the fake bug |
| — (new) | — | "Good mental model of LLMs: slightly deranged hypermotivated MSc student. Picture?" | **INSERT** new slide: mental model metaphor. Find a suitable image. |
| 8 (1000+ hours) | "1000+ hours of deliberate practice. Nov 2025–today." | **BIG X through entire slide**. "LLMs ARE useful, BUT"; "deliberate practice req't"; "1. <, 2. pay $, 3. Need to install coding agent; full auto" | **REPLACE** this slide. New content: "LLMs are useful, BUT you must: (1) practice deliberately, (2) probably pay, (3) install a coding agent (Claude Code, Cline, etc.)" |
| 9 (What I built p1) | Project table: vibefeld, Lyr.jl, af-tests, convexfeld, Nano MIPS | "Correct workflow → amazing things are possible"; "Pray" crossed out | Keep project table. Add framing: "With the correct workflow..." |
| 10 (What I built p2) | PicoGPT.jl, vectorfeld, datapipeline, alethfeld | **BIG X through slide**. "Showcase later"; "vibefeld formalisation (Lean)"; "write new science"; "All with basic tooling, no extra subscription" | **CUT** this slide (or move to backup). Replace with brief statement: showcase later, highlight Lean formalisation, emphasize basic tooling. |
| 11 (Punchline) | "All of this was built with AI coding agents." | **BIG X**. "Accelerating research is possible"; "ERA of automated research is possible with correct tools and expert guidance (human-in-loop)" | **REPLACE** with: "Accelerating research is possible — with correct tools and expert guidance" |
| 12 (Transition) | "Let me show you the entire trick." | Crossed out. "I hate magic & mystery"; "→ LLMs can be understood"; "ground up → coding agents" | **REPLACE** with: "LLMs can be understood. Let me build up from the ground." (Remove magician framing) |

### Section 01 — "What is an LLM?"

| Slide | Current | Annotation | Interpretation |
|-------|---------|------------|----------------|
| 1 (Section div) | WHAT IS AN LLM? | — | No change |
| 2 (Observable interface) | Title: "The observable interface"; f : String -> String | Title struck; "From outside looking at a Large Language model" | **RENAME** title. Reframe: "From outside, a Large Language Model is..." |
| 3 (Stateless) | Stateless diagram | — | No change |
| 4 (Nondeterministic) | Fan-out diagram | "missing dots!"; P(next token|context) circled | Add ellipsis dots ("...") to outputs. Emphasize the probability expression |
| — (new) | — | "slide in between" arrow on Temperature slide; "LLM → prob dist → samples from it" | **INSERT** new slide before Temperature formula: "An LLM outputs a probability distribution. Then it samples from it." |
| 5 (Temperature) | Boltzmann formula | "then samples" | Keep, but comes after the new conceptual slide |
| 6 (Temperature limits) | T→0, T→∞ | — | No change |
| 7 (Tokens) | "Not characters. Not words." | "Actually, not String → String. But rather [Token]^n" | **ADD** clarification: correct the String→String to [Token]^n. Perhaps a note or subtitle. |
| 8 (Inference) | "One forward pass through a frozen neural network." | "LLM =" prefix | Add "An LLM call =" or similar framing |
| 9 (Summary) | Summary with f : String → String | Red mark through "Summary" title | Possibly **REMOVE** the "Summary" heading or restyle |

### Section 02 — "The illusion of chat"

| Slide | Current | Annotation | Interpretation |
|-------|---------|------------|----------------|
| 1 (Section div) | THE ILLUSION OF CHAT | — | No change |
| 2 (Single API call) | Client ↔ API diagram | "You interact with LLM via" above title | Add context framing above the title or as speaker note |
| 3 (HTTP reality) | POST /v1/messages JSON | — | No change |
| 4 (How chat works) | Turn 1/2/3 code block | — | No change |
| 5 (No memory) | "The LLM has no memory..." | — | No change |
| 6 (Context window) | Sizes: 8k, 128k, 200k | "context length" label; 8k→"free chat"; 200k→"frontier model"; "Another slide: context rot / amnesia" | **ANNOTATE** sizes with labels. **INSERT** new slide: "Context rot / amnesia" |
| 7 (System prompt) | "A hidden preamble..." | "webpage address"; "leaked"; "→ link to Anthropic prompt" | **ADD** reference to leaked/published Anthropic system prompt |
| 8 (Summary) | "Chat is a loop..." | — | No change |

### Section 03 — "From function to agent"

| Slide | Current | Annotation | Interpretation |
|-------|---------|------------|----------------|
| 1 (Section div) | FROM FUNCTION TO AGENT | — | No change |
| — (new) | — | "Extra slide: Web interface demos chat. Terminal open for API call" | **INSERT** slide: show web interface vs. terminal for API call |
| 2 (Agent loop code) | while not done: pseudocode | — | No change |
| 3 (Agent loop diagram) | TikZ flow diagram | "append", "results" clarifications around loop arrows | Possibly improve arrow labels |
| 4 (Tool definition) | "Tool definition" title | Title struck → "Tools" | **RENAME** to "Tools" |
| 5 (Key insight) | "The LLM never executes anything." | — | No change |
| 6 (Two tools) | read_file, write_file | — | No change |
| 7 (Production equiv) | "Claude Code, Cursor, Copilot: same loop..." | — | No change |
| 8 (Live demo) | "LIVE DEMO" | — | No change |

### Section 04 — "What should we try?"

| Slide | Current | Annotation | Interpretation |
|-------|---------|------------|----------------|
| 1 (Section div) | WHAT SHOULD WE TRY? | **Red line / X** through it | **CUT** section divider |
| 2 (Option 1: LaTeX lint) | Parse .tex, find broken refs | **Red line** through it | **CUT** this option |
| 3-7 (Options 2-6) | Data to figure, DOI to BibTeX, etc. | No annotations | Keep these options |
| 8 (Vote: Raise your hand) | "Raise your hand." | **BIG X** | **CUT** this slide. Rethink vote mechanism. |

---

## Source 2: Handwritten Speaker Notes (seminarnotes.pdf)

### Narrative flow for Section 00 (spoken):

1. **Start with WHY**: LLMs have been improving dramatically. Key moments: Q1 2025, Q4 2025. ChatGPT → Claude Code → OpenAI's GPT 5.2.
2. **Insert GPT 5.2 headline** on physics.
3. **Personal story**: "If you experimented with chat interface in Q1 2025, you may well have dismissed LLMs as being useful for anything but small short of tasks."
4. **Insert the "maximally unreliable" commentary**: LLMs lie, cheat, steal, fawn & flatter.
5. **Mental model**: "Slightly deranged MSc student."
6. **Key turning point**: "I am not sure that you have experienced, but by Q4 2025 LLMs had become genuinely useful for nearly all knowledge work."
7. **BUT — three requirements**:
   1. LLM requires **deliberate practice**. It is alien tech requiring a completely different way of working/reasoning. You won't be good straight away.
   2. You probably need to **pay** $.
   3. You need to **install Claude Code** (or Cline/etc.).
8. **Correct workflow → automation**: "With correct workflow you can truly automate many scientific processes. E.g. it is now possible to file/put out/publish many papers."
9. **Basic tooling only**: "Absolutely no need for any additional subscription to AIstudio, etc."
10. **Hyper-personalised software era**: "Cheaper & easier (cognitively) to build it yourself!"
11. **Transition to technical content**: "As a scientifically trained audience you will likely appreciate an explanation of how LLMs work → this will explain their strange behaviours."

### Key concepts to cover (from notes):
1. LLM as stateless nondeterministic function
2. Context window
3. **Context rot** (NEW — not in current slides)
4. Tool use
5. Demo with python scripts

---

## Source 3: Voice Memo

*(Transcription in progress — will append when available)*

---

## Key Themes Across All Sources

### Things to ADD (not currently in slides):
1. **GPT 5.2 physics result** — headline/screenshot slide
2. **Personal confession** — "I dismissed LLMs in Q1 2025"
3. **"Slightly deranged MSc student"** mental model + image
4. **Three requirements** (practice, pay, install agent) — replaces "1000+ hours" slide
5. **Context rot / amnesia** — new slide in Section 02
6. **"Hyper-personalised software"** message
7. **LLM → probability distribution → sample** conceptual slide before Temperature formula
8. **Web interface vs terminal** demo slide before agent loop
9. **Link to leaked Anthropic system prompt**

### Things to CUT:
1. "reductive" from the subtitle
2. Timeline cyan dots
3. "1000+ hours of deliberate practice" slide (replaced)
4. "What I built (continued)" second project page (move to backup)
5. "All of this was built with AI coding agents" (replaced)
6. "Let me show you the entire trick" (replaced)
7. Section 04 divider
8. Option 1: LaTeX lint
9. "Raise your hand" vote slide

### Things to RENAME/REPHRASE:
1. Title slide subtitle
2. "The observable interface" → something about "From outside..."
3. "Tool definition" → "Tools"
4. [Token]^n correction on Tokens slide
5. "LLM =" prefix on inference slide

### Things to ADD (affiliation/branding):
1. LUH affiliation on title slide
2. InnovAILig logo/mention
