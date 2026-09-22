import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# -----------------------------
# Configuration
# -----------------------------

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL")

if not api_key:
    print("ERROR: GROQ_API_KEY is missing.")
    exit()

if not model:
    print("ERROR: MODEL is missing.")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# -----------------------------
# Conversation memory
# -----------------------------

messages = [
    {
        "role": "system",
        "content": """
You are an AI programming tutor.

Your job is to help students learn programming.

Rules:
1. Explain concepts in simple language.
2. Give examples when useful.
3. Give code examples when appropriate.
4. Encourage the student to understand the concept.
5. If the student asks for a solution, explain the reasoning too.
"""
    }
]

# -----------------------------
# Welcome message
# -----------------------------

print("=" * 50)
print("           AI PROGRAMMING TUTOR")
print("=" * 50)

print("""
Commands:
  exit   - Stop the program
  clear  - Clear conversation memory
  help   - Show commands
""")

# -----------------------------
# Main chatbot loop
# -----------------------------

while True:

    question = input("You: ").strip()

    # Empty input
    if not question:
        print("Please enter something.\n")
        continue

    # Exit command
    if question.lower() == "exit":
        print("\nThank you for using AI Tutor!")
        break

    # Help command
    if question.lower() == "help":
        print("""
Commands:
  exit   - Stop the program
  clear  - Clear conversation memory
  help   - Show commands
""")
        continue

    # Clear memory
    if question.lower() == "clear":

        messages = [
            {
                "role": "system",
                "content": """
You are an AI programming tutor.
Explain programming concepts clearly and simply for beginners.
"""
            }
        ]

        print("Conversation memory cleared.\n")
        continue

    # Add user message
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Call the LLM
    try:

        response = client.chat.completions.create(
            model=model,
            messages=messages
        )

        answer = response.choices[0].message.content

        # Save AI response
        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        print("\nAI Tutor:", answer)
        print()

    except Exception as e:

        print("\nSomething went wrong.")
        print("Error:", e)
        print()