import os
import json
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
Return ONLY valid JSON.

The JSON must contain:
- topic
- definition
- example
- difficulty
"""
        },
        {
            "role": "user",
            "content": "Explain Python functions."
        }
    ]
)

text = response.choices[0].message.content

print("Raw AI response:")
print(text)

data = json.loads(text)

print("\nTopic:", data["topic"])
print("Definition:", data["definition"])
print("Example:", data["example"])
print("Difficulty:", data["difficulty"])