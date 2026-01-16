from pathlib import Path
from app.utils import chunk_text

TRANSCRIPT_PATH = Path("data/transcripts")

for file in TRANSCRIPT_PATH.glob("*.txt"):
    text = file.read_text(encoding="utf-8")
    chunks = chunk_text(text)

    print(f"{file.name}")
    print(f"Total chunks: {len(chunks)}")
    print("Sample chunk:\n")
    print(chunks[0][:300])
    break
