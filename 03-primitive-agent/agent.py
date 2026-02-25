"""
A minimal agent loop in ~100 lines.

System prompt tells the model it has two tools (read_file, write_file).
The model requests tool calls using a simple XML format. The loop parses
and executes them, appending results to history, until the model
produces a final text response with no tool call.

Every step is printed to stdout so the audience can follow along.
"""

import os
import re
import sys

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.")
        print("Export it before running this script:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    import anthropic
    from tools import read_file, write_file

    client = anthropic.Anthropic()

    system_prompt = """You are a helpful assistant with access to two tools.

To use a tool, respond with EXACTLY this XML format (one tool call per response):

<tool_call>
<name>TOOL_NAME</name>
<arg name="PARAM">VALUE</arg>
</tool_call>

Available tools:

1. read_file(path) - Read a file from the workspace directory.
   Example:
   <tool_call>
   <name>read_file</name>
   <arg name="path">data.csv</arg>
   </tool_call>

2. write_file(path, content) - Write content to a file in the workspace directory.
   Example:
   <tool_call>
   <name>write_file</name>
   <arg name="path">output.txt</arg>
   <arg name="content">Hello, world!</arg>
   </tool_call>

When you are done and have no more tool calls to make, respond with plain text (no XML tags).
All file paths are relative to the workspace directory."""

    # Read the task
    task_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "workspace", "example_task.md")
    with open(task_file) as f:
        task = f.read()

    messages = [{"role": "user", "content": task}]

    print(f"[TASK]\n{task}\n")
    print("=" * 60)

    for step in range(1, 20):  # safety limit
        print(f"\n[STEP {step}: SENDING TO LLM]")
        print(f"  (message history length: {len(messages)})")

        response = client.messages.create(
            model="claude-sonnet-4-6-20250627",
            max_tokens=1024,
            system=system_prompt,
            messages=messages,
        )

        text = response.content[0].text
        print(f"\n[LLM RESPONSE]\n{text}")

        # Check for tool call
        match = re.search(
            r"<tool_call>\s*<name>(\w+)</name>(.*?)</tool_call>",
            text,
            re.DOTALL,
        )

        if not match:
            print("\n[DONE] No tool call detected. Agent finished.")
            break

        tool_name = match.group(1)
        args_text = match.group(2)

        # Parse arguments
        args = {}
        for arg_match in re.finditer(
            r'<arg name="(\w+)">(.*?)</arg>', args_text, re.DOTALL
        ):
            args[arg_match.group(1)] = arg_match.group(2)

        print(f"\n[TOOL CALL: {tool_name}({args})]")

        # Execute
        if tool_name == "read_file":
            result = read_file(args.get("path", ""))
        elif tool_name == "write_file":
            result = write_file(args.get("path", ""), args.get("content", ""))
        else:
            result = f"Error: unknown tool '{tool_name}'"

        print(f"[TOOL RESULT]\n{result}")

        # Append to history
        messages.append({"role": "assistant", "content": text})
        messages.append({"role": "user", "content": f"Tool result:\n{result}"})
    else:
        print("\n[STOPPED] Reached maximum steps.")


if __name__ == "__main__":
    main()
