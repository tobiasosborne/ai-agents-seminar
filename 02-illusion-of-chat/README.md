# 02: The Illusion of Chat and Memory

This section reveals how "chat" actually works. There is no persistent
memory on the server. The client re-sends the entire conversation
history with every API call. Chat is a loop. Memory is an illusion
maintained by the client.

## Slides

`slides.pdf` covers: a single API call, the HTTP request structure,
how the message array grows, the context window, the system prompt,
and a summary.

## Demos

### single_call.py

```bash
python single_call.py
```

Makes one API call and prints the full request and response JSON.
**What to observe**: one string in, one string out. That is the
entire interaction.

### chat_loop.py

```bash
python chat_loop.py
```

A terminal chat interface. Each turn prints the number of messages
in the history and the approximate character count of the full context.

**What to observe**: the context grows with every turn. The client
is doing all the bookkeeping. Type `quit` to exit.
