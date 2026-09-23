from config import client, MODEL, banner

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

DIRECT_PROMPT = (
    "You are a helpful assistant. Answer the question directly. "
    "Give only the final answer. Do not explain."
)

if __name__ == "__main__":
    banner("DIRECT PROMPTING")

    print("QUESTION:")
    print(QUESTION)

    print("\n--- DIRECT ANSWER ---")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": DIRECT_PROMPT},
            {"role": "user", "content": QUESTION},
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content.strip()

    print(answer)