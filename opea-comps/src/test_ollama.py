import requests
import json

def test_ollama():
    # Test the Ollama endpoint
    url = "http://localhost:8008/api/generate"
    
    payload = {
        "model": "llama3.2:1b",
        "prompt": "What is machine learning?"
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_ollama() 