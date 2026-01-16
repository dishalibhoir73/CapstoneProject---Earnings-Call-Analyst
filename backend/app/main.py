from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import shutil

from .whisper_service import transcribe_audio
from .rag import ask_question

app = FastAPI()

AUDIO_DIR = Path("data/audio")
TRANSCRIPT_DIR = Path("data/transcripts")

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_path = AUDIO_DIR / file.filename

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript_text = transcribe_audio(str(audio_path))

    transcript_path = TRANSCRIPT_DIR / f"{audio_path.stem}.txt"
    transcript_path.write_text(transcript_text, encoding="utf-8")

    return {
        "message": "Transcription completed",
        "transcript_file": transcript_path.name
    }


@app.post("/ask")
async def ask(payload: dict):
    question = payload.get("question")

    if not question:
        return {"error": "Question is required"}

    answer = ask_question(question)

    return {
        "question": question,
        "answer": answer
    }
