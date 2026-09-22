import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Check API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: GROQ_API_KEY is missing.")
    print("Check your .env file.")
    exit()

# Check model
model = os.getenv("MODEL")

if not model:
    print("ERROR: MODEL is missing.")
    print("Check your .env file.")
    exit()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

print("================================")
print("       Safe AI Q&A App")
print("================================")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ").strip()

    # Empty input
    if not question:
        print("Please enter a question.\n")
        continue

    # Exit
    if question.lower() == "exit":
        print("Goodbye!")
        break

    try:

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful Python tutor. Explain concepts clearly for beginners."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        print("\nAI:", answer)
        print()

    except Exception as e:

        print("\nSomething went wrong.")
        print("Error:", e)
        print("Please try again.\n")