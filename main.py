from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FoodRequest(BaseModel):
    food_description: str
    quantity: str = "1 serving"

class FoodResponse(BaseModel):
    food_name: str
    calories: int
    protein: float
    carbs: float
    fat: float
    serving_size: str

@app.get("/")
def root():
    return {"status": "FitMacroAI Backend Running!"}

@app.post("/analyze-food", response_model=FoodResponse)
async def analyze_food(request: FoodRequest):
    
    if not request.food_description.strip():
        raise HTTPException(status_code=400, detail="Food description cannot be empty")
    
    if len(request.food_description) > 200:
        raise HTTPException(status_code=400, detail="Food description too long")
    
    prompt = f"""
    Analyze this food and return ONLY a JSON object with nutritional info.
    
    Food: {request.food_description}
    Quantity: {request.quantity}
    
    Return ONLY this JSON format, nothing else:
    {{
        "food_name": "name of food",
        "calories": 000,
        "protein": 00.0,
        "carbs": 00.0,
        "fat": 00.0,
        "serving_size": "description of serving"
    }}
    
    Use standard Indian food nutrition data where applicable.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        
        text = response.choices[0].message.content.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        data = json.loads(text)
        return FoodResponse(**data)
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI returned invalid response, please try again")
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI service unavailable, please try again later")