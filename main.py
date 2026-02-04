# main.py
from fastapi import FastAPI
from schemas import ScamRequest, ScamResponse
from models import save_message, get_user_messages
from scam_agent import detect_scam

app = FastAPI(title="RakshakAI – Scam Detection API")

@app.get("/")
def home():
    return {"status": "RakshakAI running"}

@app.post("/detect", response_model=ScamResponse)
def detect(request: ScamRequest):
    user_id = request.user_id

    # save user message
    save_message(user_id, "user", request.message)

    # fetch chat history
    history = get_user_messages(user_id)

    # AI detection
    result = detect_scam(request.message, history)

    # save assistant response
    save_message(user_id, "assistant", result.model_dump_json())

    # return clean JSON
    return result.model_dump()


