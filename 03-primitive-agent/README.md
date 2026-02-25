# 03: From Function to Agent

This section builds a working agent from scratch. The complete
architecture of every coding agent (Claude Code, Cursor, Copilot)
reduces to:

```
while not done:
    response = llm(system_prompt + history)
    tool_calls = parse(response)
    results = execute(tool_calls)
    history += [response, results]
```

Our agent has two tools: `read_file` and `write_file`. That is
enough to do useful work.

## Slides

`slides.pdf` covers: the agent loop pseudocode, tool definitions,
our two tools, the equivalence with production agents, and a
live demo cue slide.

## Demo

```bash
python agent.py
```

Runs the agent on the task in `workspace/example_task.md`. The agent
will create a CSV file and then analyse it, all by calling the two
tools in a loop.

**What to observe**: every step is printed with clear labels.
Watch the LLM request a tool call, the scaffolding execute it,
and the result get appended to history. The LLM never executes
anything directly.

## Files

- `agent.py`: the agent loop (~100 lines)
- `tools.py`: read_file and write_file, restricted to `workspace/`
- `workspace/example_task.md`: the task the agent will work on
