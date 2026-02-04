from fastapi import FastAPI
from schemas import ScamRequest, ScamResponse
from scam_agent import detect_scam

app = FastAPI(title="RakshakAI – Scam Detection API")


@app.get("/")
def home():
    return {"status": "RakshakAI running"}


@app.post("/detect", response_model=ScamResponse)
def detect(request: ScamRequest):
    """
    Deploy-safe detect endpoint
    (Database temporarily disabled)
    """

    # No DB during deployment
    history = []

    # Scam detection
    result = detect_scam(request.message, history)

    # Return clean JSON
    return result.model_dump()

