import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "system",
            "content": """
You are a programming teacher.

Rules:
1. Explain concepts in simple language.
2. Give one example.
3. Give one short code example.
4. Keep the answer under 150 words.
"""
        },
        {
            "role": "user",
            "content": "Explain Python functions."
        }
    ]
)

print(response.choices[0].message.content)