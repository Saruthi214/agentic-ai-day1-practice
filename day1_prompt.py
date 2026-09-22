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
            "content": "You are a helpful teacher. Explain concepts in simple language suitable for a beginner."
        },
        {
            "role": "user",
            "content": "What is Machine Learning?"
        }
    ]
)

print(response.choices[0].message.content)