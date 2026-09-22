import re
from academic_config import SUBJECT_CREDITS, QUESTIONS


def workflow(question):
    codes = re.findall(r"[A-Z]{2}\d{3}", question.upper())

    credits = [
        SUBJECT_CREDITS[code]
        for code in codes
        if code in SUBJECT_CREDITS
    ]

    if not credits:
        return "Sorry, I can only answer questions about subject credits."

    text = question.lower()

    # Total credits
    if "total" in text:
        total = sum(credits)
        return f"Total credits: {total}"

    # Compare two subjects
    if "more" in text or "by how much" in text:
        if len(credits) == 2:
            difference = abs(credits[0] - credits[1])

            if credits[0] > credits[1]:
                higher = codes[0]
            elif credits[1] > credits[0]:
                higher = codes[1]
            else:
                return "Both subjects have the same number of credits."

            return (
                f"{higher} has more credits by "
                f"{difference} credit(s)."
            )

    # Single subject
    if len(credits) == 1:
        return f"Credits for {codes[0]}: {credits[0]}"

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":
    print("\n=== RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)