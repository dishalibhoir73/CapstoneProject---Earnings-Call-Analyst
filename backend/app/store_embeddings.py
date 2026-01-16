from pathlib import Path
from utils import chunk_text
from .embeddings import embed_text
from qdrant_db import client, init_collection, COLLECTION_NAME
import uuid

TRANSCRIPT_DIR = Path("data/transcripts")

def store_all_transcripts():
    for file in TRANSCRIPT_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        chunks = chunk_text(text)

        sample_vector = embed_text(chunks[0])
        init_collection(len(sample_vector))

        points = []
        for chunk in chunks:
            vector = embed_text(chunk)
            points.append({
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {
                    "text": chunk,
                    "source": file.name
                }
            })

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )

        print(f"Stored {len(points)} chunks from {file.name}")


if __name__ == "__main__":
    store_all_transcripts()
