# 🚨 Rakshak AI – Scam Detection System

Rakshak AI is an **AI-powered web application** designed to detect scam and phishing messages in real-time.  
Built with **FastAPI (backend)** and **TailwindCSS (frontend)**, it provides a modern UI with scanning animations, confidence scoring, and actionable security tips.

---

## 📌 Project Evolution

### 🔹 Version v1
- Minimal FastAPI backend with a single `/detect` endpoint.
- Static response for demo purposes.
- No frontend, tested via Swagger UI.

### 🔹 Version v2 (Current)
- **Backend**:
  - Structured FastAPI app (`main.py`, `schemas.py`, `scam_agent.py`, `models.py`, `db.py`).
  - Rule-based scam detection with regex + confidence scoring.
  - Rich response schema (`is_scam`, `risk_level`, `reason`, `confidence`, `timestamp`, `suggested_action`).
  - Database layer with SQLAlchemy + Alembic migrations.
  - CORS middleware for frontend integration.

- **Frontend**:
  - TailwindCSS + glassmorphism design.
  - Scanning animation, glowing button, bottom navigation icons.
  - Hybrid detection logic: tries backend API, falls back to demo mode if backend offline.

- **Deployment Prep**:
  - Requirements.txt updated with ORM + migrations.
  - Dockerfile + docker-compose planned for containerization.

---

## ⚙️ Tech Stack

- **Backend**: [FastAPI](ca://s?q=FastAPI_backend), [SQLAlchemy](ca://s?q=SQLAlchemy), [Alembic](ca://s?q=Alembic_migrations), [MySQL](ca://s?q=MySQL_database)
- **Frontend**: [TailwindCSS](ca://s?q=TailwindCSS_frontend), Vanilla JS
- **Other Tools**: Docker (planned), Google Generative AI (future integration)

---

## 🚀 How It Works

1. User pastes a suspicious message in the frontend.
2. Frontend sends request to backend `/detect`.
3. Backend runs scam detection → returns structured response.
4. Frontend displays result with color coding, icons, and suggested action.
5. If backend is offline, demo logic runs locally in JS.

---

## 📈 Roadmap (Future v3+)

- [Risk Meter](ca://s?q=Add_risk_meter_UI): Animated progress bar for confidence score.
- [History Tab](ca://s?q=Add_history_tab_UI): Store past scans in DB, show them in frontend.
- [Security Tips](ca://s?q=Add_security_tips_UI): Contextual advice when scam detected.
- [AI Upgrade](ca://s?q=Google_Generative_AI): Smarter detection beyond regex.
- [Deployment](ca://s?q=Render_deployment): Push to Render/Railway/Azure for live demo.
- [Mobile App](ca://s?q=React_Native): Wrap frontend in React Native for iOS/Android.

---

## 🛠️ Setup Instructions

```bash
# Clone repo
git clone https://github.com/<your-username>/rakshak_ai.git
cd rakshak_ai

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload

# Open frontend
open frontend/index.html
  
👩‍💻 Author
Neha Mhatre – Aspiring full‑stack developer building AI‑powered web applications
