"""
Demonstrate that an LLM is a stateless, nondeterministic function.

Sends the same prompt five times at different temperatures and prints
each response. Responses differ (nondeterministic) and no state
carries between calls (stateless).
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
    prompt = "Explain in one sentence what a quark is."
    temperatures = [0.0, 0.3, 0.5, 0.8, 1.0]

    print(f"Prompt: {prompt!r}\n")

    for temp in temperatures:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            temperature=temp,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text
        print(f"[T={temp}] {text}\n")


if __name__ == "__main__":
    main()
