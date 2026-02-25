# 01: The LLM as a Stateless Nondeterministic Function

This section establishes the core mental model. From outside the API
boundary, an LLM is a function `f : String -> String` that is:

- **Stateless**: each call is independent, no memory between calls.
- **Nondeterministic**: the same input can produce different outputs,
  governed by a temperature-controlled sampling distribution.

## Slides

`slides.pdf` covers: the observable interface, statelessness,
nondeterminism, temperature (with a Boltzmann analogy), tokens,
inference as a single forward pass, and a summary.

## Demo

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python demo.py
```

Sends the same prompt ("Explain in one sentence what a quark is.")
five times at temperatures 0.0, 0.3, 0.5, 0.8, and 1.0.

**What to observe**: at T=0.0 the output is nearly deterministic.
As temperature increases, responses become more varied. No call
has any knowledge of the previous calls.
