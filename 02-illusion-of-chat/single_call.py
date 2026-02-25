"""
Show the raw structure of a single API call.

Makes one call, prints the full request payload (as formatted JSON)
and the full response payload. This is all there is.
"""

import json
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

    request_payload = {
        "model": "claude-sonnet-4-6-20250627",
        "max_tokens": 256,
        "messages": [
            {"role": "user", "content": "What is a quark?"}
        ],
    }

    print("=== REQUEST ===")
    print(json.dumps(request_payload, indent=2))
    print()

    response = client.messages.create(**request_payload)

    print("=== RESPONSE ===")
    print(json.dumps(response.model_dump(), indent=2, default=str))


if __name__ == "__main__":
    main()
