from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ScamRequest, ScamResponse
from scam_agent import detect_scam

app = FastAPI(title="Rakshak AI – Scam Detection API")

# -------- Enable CORS --------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for hackathon/local testing, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect", response_model=ScamResponse)
def detect_scam_api(data: ScamRequest):
    return detect_scam(data.message, data.history or [])

@app.get("/")
def home():
    return {"status": "running", "service": "Rakshak AI"}

