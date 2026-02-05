from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="CallShield AI – Scam Detection API")


# -------- Request Model (MATCHES HACKATHON PAYLOAD) --------
class DetectRequest(BaseModel):
    sessionId: str
    message: Dict        # sender, text, timestamp
    conversationHistory: List = []
    metadata: Dict


# -------- API ENDPOINT --------
@app.post("/detect")
def detect_scam(data: DetectRequest):
    # Extract scam text
    scam_text = data.message.get("text", "")

    # 👉 Your scam logic / AI model can be here
    # (for now, static reply is acceptable for hackathon testing)
    reply_text = "Why is my account being suspended?"

    return {
        "status": "success",
        "reply": reply_text
    }


# -------- Root endpoint (optional but safe) --------
@app.get("/")
def home():
    return {"status": "running", "service": "CallShield AI"}

