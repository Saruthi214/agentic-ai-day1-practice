from config import client, MODEL, banner

QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Number each step and show the calculation in each step. "
    "If required information is missing, clearly state that you "
    "cannot determine the answer without that information. "
    "After the steps, write the final answer."
)

if __name__ == "__main__":
    banner("CHAIN-OF-THOUGHT")

    print("QUESTION:")
    print(QUESTION)

    print("\n--- CHAIN-OF-THOUGHT ANSWER ---")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": COT_PROMPT},
            {"role": "user", "content": QUESTION},
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content.strip()

    print(answer)