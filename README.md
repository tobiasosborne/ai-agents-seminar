# AI Coding Agents: A Reductive Account for Physicists

Materials for a 1-hour seminar at UCL Physics. The goal is to demystify
AI coding agents by showing that every part of the stack reduces to
simple, composable primitives that physicists already have intuition for.

## Setup

```bash
git clone https://github.com/<you>/ucl-ai-agents-seminar.git
cd ucl-ai-agents-seminar
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## Regenerate slides

```bash
python build_slides.py
```

This produces four PDFs, one per section.

## Structure

| Directory | What it covers |
|-----------|---------------|
| `01-stateless-nondeterministic-function/` | An LLM is a stateless nondeterministic function f : String -> String |
| `02-illusion-of-chat/` | Chat is a client-side loop. Memory is an illusion. |
| `03-primitive-agent/` | The agent loop: LLM + tools + history |
| `04-audience-vote/` | Live audience vote on what to build next |

Each section directory has its own README with instructions for running
its demos and what the audience should observe.

## Requirements

- Python 3.10+
- An Anthropic API key (for the demo scripts)
- reportlab (for slide generation)
