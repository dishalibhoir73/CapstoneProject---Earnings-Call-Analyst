from pathlib import Path
from qdrant_client.models import PointStruct
from .utils import chunk_text
from .embeddings import embed_text
from .qdrant_db import client, init_collection, COLLECTION_NAME
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
            points=[
                PointStruct(
                    id=uuid.uuid4().hex,
                    vector=vector,
                    payload={
                        "text": chunk,
                        "source_file": file.name,
                        "company": file.stem.split("_")[0],
                    }
                )
            ]
    )

        print(f"Stored {len(points)} chunks from {file.name}")


if __name__ == "__main__":
    store_all_transcripts()
