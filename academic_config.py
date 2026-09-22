import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
else:
    raise SystemExit("This project is configured for Groq.")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY not found in .env")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

STUDENT_DATA = {
    "name": "Saruthi",
    "department": "CSE",
    "semester": 5,
    "cgpa": 7.81
}

SUBJECT_CREDITS = {
    "CS501": 4,
    "CS502": 3,
    "CS503": 4,
    "CS504": 3
}

QUESTIONS = [
    "How many credits does CS501 have?",
    "What is the total credits of CS501 and CS503?",
    "Which has more credits, CS501 or CS502, and by how much?",
    "Give me a two-line message encouraging me to study.",
    "I can take subjects with a maximum of 7 credits. Which two subjects can I take together?"
]