import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("================================")
print("      Python AI Q&A Assistant")
print("================================")
print("Type 'exit' to stop.\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": """
You are a Python programming tutor.

Return ONLY valid JSON with these fields:
topic
answer
example
difficulty

Keep the explanation suitable for a beginner.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        text = response.choices[0].message.content

        data = json.loads(text)

        print("\nTopic:", data["topic"])
        print("Answer:", data["answer"])
        print("Example:", data["example"])
        print("Difficulty:", data["difficulty"])
        print()

    except json.JSONDecodeError:
        print("\nThe AI returned an invalid JSON response.")
        print("Please try again.\n")

    except Exception as e:
        print("\nSomething went wrong:", e)