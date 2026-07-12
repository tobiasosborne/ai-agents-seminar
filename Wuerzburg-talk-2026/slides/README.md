# Large Language Models: A Physicist's Perspective

**Physikalisches Kolloquium, Universität Würzburg**: Monday 13 July 2026,
14:15, Röntgen-Hörsaal + Zoom. ~60 minutes, 50 slides (43 content + 7 dividers).

Adapted from `gc-conference-2026/` (same TJO Beamer theme) per `SPEC.md`;
extended with the Würzburg-specific material.

## Build

```bash
make          # lualatex ×2 → talk.pdf
```

Figures are referenced in place from `../grade-decorrelation/figures/` and
`../model-progress/figures/`: rebuild those projects first if they change.

## Structure

1. **Why this talk?**: three hooks (unit-distance disproof arXiv:2605.20695,
   OpenAI string theory paper, assignment/exam decorrelation: *synthetic
   data, labelled as such on every slide*), survey, four-moment timeline
2. **What is an LLM?**: f: String→String, nondeterminism, temperature, tokens
3. **The illusion of chat**: cURL, chat as scaffolding, context window/rot,
   compaction
4. **From function to agent**: agent loop, feedback closes the loop,
   filesystem = permanent memory (the radical unlock), subagents,
   adversarial verification
5. **Live demo**: prompts pre-written in `demo/demo_prompt.md` (primary:
   damped driven pendulum phase portrait)
6. **The trend**: Epoch AI figures: ECI frontier, benchmark ladder,
   open-weight lag
7. **The harder problem**: research phase transition, renaissance expert,
   single point of failure, trust arc (Dutch proverb → unhinged MSc student →
   investigative mindset), limitations, automation spectrum, call to action
