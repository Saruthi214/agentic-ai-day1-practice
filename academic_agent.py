import json

from academic_config import client, MODEL, QUESTIONS
from academic_tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a student academic assistant.

Never guess subject credit values.
Always use get_subject_credits when a subject credit is needed.

Use calculator for arithmetic.

Available subjects:
CS501, CS502, CS503, CS504.

For questions requiring multiple steps, use the tools and continue
until you can provide a final answer.

If no tool is required, answer directly.
"""


def agent(question, max_steps=6):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content.strip()

        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments
                    }
                }
                for call in message.tool_calls
            ]
        })

        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            result = (
                function(**arguments)
                if function
                else f"Unknown tool: {name}"
            )

            print(
                f"Step {step}: "
                f"{name}({arguments}) -> {result}"
            )

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached."


if __name__ == "__main__":

    print("\n=== AI AGENT ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)