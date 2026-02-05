# Rakshak AI – Scam Detection Backend

Rakshak AI is a **FastAPI-based backend service** designed to detect and analyze scam or fraudulent messages using AI-driven logic. This repository contains the backend implementation with a clean, modular structure and is built to be deployment-ready.

---

## 🚀 Features

* Scam / fraud message detection API
* Built with **FastAPI** (high-performance Python web framework)
* Modular backend architecture (DB, models, schemas, agents)
* MySQL database support (disabled for production deployment when required)
* Auto-generated API docs using Swagger UI
* Production-ready structure for cloud deployment

---

## 🧠 Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python 3
* **Database:** MySQL (optional / environment-based)
* **ORM / DB Connector:** mysql-connector-python
* **API Documentation:** Swagger (OpenAPI)

---

## 📂 Project Structure

```
rakshak-ai-backend/
│
├── main.py          # FastAPI app entry point
├── db.py            # Database connection logic
├── models.py        # Database CRUD operations
├── schemas.py       # Pydantic request/response schemas
├── scam_agent.py    # Scam detection logic / AI agent
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/neuuu116/rakshak-ai-backend.git
cd rakshak-ai-backend
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file (for local DB usage):

```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=rakshak_ai
```

> ⚠️ For production deployment, local DB usage can be disabled.

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

* API Base URL: `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`
* OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

---

## 📡 API Endpoints

### 🔹 Home

```
GET /
```

Returns API status message.

### 🔹 Detect Scam Message

```
POST /detect
```

**Request Body:**

```json
{
  "user_id": 1,
  "message": "Your bank account will be blocked. Click this link urgently."
}
```

**Response:**

```json
{
  "is_scam": true,
  "confidence": 0.92,
  "reason": "Urgent threat and suspicious link pattern"
}
```

---

## ☁️ Deployment

* Compatible with platforms like **Render, Railway, Fly.io, AWS, GCP**
* Ensure:

  * `requirements.txt` is present
  * DB connections are disabled or environment-based
  * Correct start command:

    ```
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

---

## 🔒 Security Notes

* Do not commit `.env` files
* Use environment variables for secrets
* Add authentication & rate limiting for production use

---

## 📌 Future Improvements

* JWT-based authentication
* Role-based access control
* Logging & monitoring
* AI model upgrades
* Frontend integration

---

## 👩‍💻 Author

**Neha Mhatre**
Backend Developer | API & Data Enthusiast

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

> *Rakshak AI – Building safer digital communication through intelligent backend systems.*
