from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    model: str
    messages: str

@app.post("/v1/multi-service")
async def process_request(message: Message):
    try:
        # Fixed: Using the correct Ollama API format
        response = requests.post(
            "http://ollama:11434/api/generate",
            json={
                "model": message.model,
                "prompt": message.messages,
                "stream": False,
                "raw": True  # Added this to ensure proper format
            }
        )
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Model {message.model} not found")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error calling Ollama: {str(e)}") 