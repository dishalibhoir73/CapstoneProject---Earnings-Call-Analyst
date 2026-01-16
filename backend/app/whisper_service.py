import whisper
from pathlib import Path

# load model once
model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    """
    Takes audio file path and returns transcribed text
    """
    result = model.transcribe(audio_path)
    return result["text"]
