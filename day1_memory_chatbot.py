import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor. Remember the conversation and explain concepts clearly."
    }
]

print("AI Memory Chatbot")
print("Type 'exit' to stop.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Add user's message to conversation history
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    answer = response.choices[0].message.content

    # Add AI response to conversation history
    messages.append({
        "role": "assistant",
        "content": answer
    })

    print("AI:", answer)
    print()