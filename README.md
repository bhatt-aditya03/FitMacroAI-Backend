# FitMacroAI Backend 🤖

FastAPI backend for FitMacroAI iOS app — AI-powered food nutrition analysis.

## Live API
https://web-production-f32bc.up.railway.app

## Endpoint
POST /analyze-food

Request:
```json
{
  "food_description": "rajma chawal",
  "quantity": "1 katori"
}
```

Response:
```json
{
  "food_name": "Rajma Chawal",
  "calories": 420,
  "protein": 19.0,
  "carbs": 60.0,
  "fat": 14.0,
  "serving_size": "1 katori (250-300 grams)"
}
```

## Tech Stack
- **Framework:** FastAPI + Python
- **AI:** LLaMA 3.3 70B via Groq
- **Deployment:** Railway.app

## Setup
```bash
git clone https://github.com/bhatt-aditya03/FitMacroAI-Backend
cd FitMacroAI-Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key" > .env
uvicorn main:app --reload
```

## iOS App
[FitMacroAI](https://github.com/bhatt-aditya03/FitMacroAI)


