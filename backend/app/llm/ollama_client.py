import requests
from app.config.settings import OLLAMA_URL

# simple client for local ollama server
def query_llm(prompt):

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]