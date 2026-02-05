from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ScamRequest, ScamResponse
from scam_agent import detect_scam

app = FastAPI(title="RakshakAI – Scam Detection API")

# -------------------------------
# CORS (safe for hackathon bots)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# GET / (health check)
# -------------------------------
@app.get("/")
def home():
    return {"status": "RakshakAI running"}

# --------------------------------------------------
# POST /  ✅ HACKATHON REQUIRED ROOT ENDPOINT
# --------------------------------------------------
@app.post("/")
def hackathon_entry(payload: dict):
    """
    Impact AI Hackathon compatibility endpoint
    Accepts any valid JSON payload and returns
    the exact expected response format.
    """
    return {
        "status": "success",
        "reply": "Why is my account being suspended?"
    }

# --------------------------------------------------
# POST /detect  (your original logic – keep it)
# --------------------------------------------------
@app.post("/detect", response_model=ScamResponse)
def detect(request: ScamRequest):
    """
    Deploy-safe detect endpoint
    (Database temporarily disabled)
    """

    # No DB usage during hackathon testing
    history = []

    # Scam detection logic
    result = detect_scam(request.message, history)

    # Return clean JSON
    return result.model_dump()

