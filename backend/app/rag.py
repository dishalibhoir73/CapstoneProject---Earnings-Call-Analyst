import requests
from .query_qdrant import retrieve_context

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def ask_question(question: str) -> str:
    contexts = retrieve_context(question)

    if not contexts:
        return "No relevant context found."

    prompt = f"""
You are a financial analyst.
Answer strictly using the context below.

Context:
{chr(10).join(contexts)}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"].strip()
