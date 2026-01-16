import requests
from .query_qdrant import retrieve_context

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

def ask_question(question: str):
    contexts = retrieve_context(question)

    prompt = f"""
You are a financial analyst.
Answer ONLY using the context below.

Context:
{chr(10).join(contexts)}

Question:
{question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    return response.json()["response"]
