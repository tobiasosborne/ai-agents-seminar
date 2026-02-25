"""
A minimal terminal chat interface in ~40 lines.

Maintains a messages list. Each turn: append user input, send the full
list to the API, append the assistant response, print. The audience
sees the context growing with each turn.

Type 'quit' to exit.
"""

import os
import sys

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        print("Export it before running this script:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    import anthropic

    client = anthropic.Anthropic()
    messages = []

    print("Chat with Claude. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break

        messages.append({"role": "user", "content": user_input})

        response = client.messages.create(
            model="claude-sonnet-4-6-20250627",
            max_tokens=512,
            messages=messages,
        )

        assistant_text = response.content[0].text
        messages.append({"role": "assistant", "content": assistant_text})

        approx_tokens = len(str(messages))
        print(f"\nAssistant: {assistant_text}")
        print(f"  [messages: {len(messages)}, approx chars in context: {approx_tokens}]\n")


if __name__ == "__main__":
    main()
