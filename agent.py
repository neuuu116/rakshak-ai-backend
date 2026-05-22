import os
from dotenv import load_dotenv
from google import genai
import json

# Load environment variables
load_dotenv()

client = genai.Client(api_key="AIzaSyBKHPVHrhjNN1LuQoD491chbnjTerqDpPw")

MEMORY_FILE = "rakshak_memory.txt"

# Load memory if exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = f.read()
else:
    memory = ""


def save_memory():
    """Persist agent memory to file"""
    with open(MEMORY_FILE, "w") as f:
        f.write(memory)


def detect_scam(message: str):
    """
    RakshakAI Scam Detection Agent
    Detects scam intent and returns structured JSON
    """

    prompt = f"""
You are RakshakAI, an AI Scam Detection Agent for India.

Analyze the message below and respond ONLY in valid JSON.

Tasks:
1. Identify if the message is a scam
2. Classify the scam type (if any)
3. Assign a risk level
4. Explain reasoning briefly

Message:
\"\"\"{message}\"\"\"

Return JSON strictly in this format:
{{
  "is_scam": true/false,
  "scam_type": "Banking | OTP | Lottery | KYC | Investment | Other | None",
  "risk_level": "Low | Medium | High",
  "reasons": [
    "reason 1",
    "reason 2"
  ]
}}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    global memory
    memory += f"\n[SCAM_ANALYSIS]\nInput: {message}\nOutput: {response.text}\n"
    save_memory()

    return response.text


def honeypot_response(scam_message: str):
    """
    RakshakAI Honeypot Agent
    Engages scammer to extract intelligence
    """

    prompt = f"""
You are RakshakAI, operating as a human honeypot.

Rules:
- You must behave like a real, unaware human
- Do NOT reveal you are AI
- Stay polite and cooperative
- Try to extract:
  • Bank account numbers
  • UPI IDs
  • Payment links

Scammer message:
\"\"\"{scam_message}\"\"\"

Respond naturally like a human user.
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    global memory
    memory += f"\n[HONEYPOT_INTERACTION]\nScammer: {scam_message}\nRakshakAI: {response.text}\n"
    save_memory()

    return response.text


