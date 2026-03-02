# FitMacroAI Backend 🤖
> FastAPI backend for FitMacroAI iOS app — AI-powered food nutrition analysis via LLaMA 3.3 70B

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.133-green)](https://fastapi.tiangolo.com)
[![Railway](https://img.shields.io/badge/Deployed-Railway-purple)](https://web-production-f32bc.up.railway.app)

---

## Live API

Base URL: https://web-production-f32bc.up.railway.app

API Docs: https://web-production-f32bc.up.railway.app/docs

---

## What It Does

Accepts natural language food descriptions → sends to LLaMA 3.3 70B via Groq → returns structured nutrition data as JSON.

---

## API Endpoint

**POST** `/analyze-food`

**Request:**
```json
{
  "food_description": "rajma chawal",
  "quantity": "1 katori"
}
```

**Response:**
```json
{
  "food_name": "Rajma Chawal",
  "calories": 420,
  "protein": 19.0,
  "carbs": 60.0,
  "fat": 14.0,
  "serving_size": "1 katori (approximately 250-300 grams)"
}
```

**Error Handling:**
- `400` — Empty or too long food description
- `500` — AI service unavailable or invalid response

---

## Architecture
```
iOS App
    ↓ POST /analyze-food
FastAPI Server (Railway)
    ↓ Groq API
LLaMA 3.3 70B
    ↓ JSON parsing
Structured Response
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI + Python |
| AI Model | LLaMA 3.3 70B via Groq |
| Server | Uvicorn |
| Deployment | Railway.app |
| Validation | Pydantic |

---

## Project Structure
```
FitMacroAI-Backend/
├── main.py           # FastAPI app + endpoint + Groq integration
├── requirements.txt  # Python dependencies
├── Procfile          # Railway deployment config
└── .gitignore        # Excludes .env, venv, pycache
```

---

## Local Setup
```bash
git clone https://github.com/bhatt-aditya03/FitMacroAI-Backend.git
cd FitMacroAI-Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key_here" > .env
uvicorn main:app --reload
```

API available at: http://127.0.0.1:8000
Docs at: http://127.0.0.1:8000/docs

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | API key from console.groq.com |

---

## Deployment

Deployed on Railway.app with auto-deploy on every GitHub push.

---

## iOS App

[FitMacroAI](https://github.com/bhatt-aditya03/FitMacroAI)

---

## Author

**Aditya Bhatt**

---

## Status

✅ Live | Deployed | Portfolio Ready
