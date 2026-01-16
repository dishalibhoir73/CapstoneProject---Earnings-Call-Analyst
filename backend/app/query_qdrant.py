from qdrant_client import QdrantClient
from .embeddings import embed_text
from .qdrant_db import COLLECTION_NAME

client = QdrantClient(host="localhost", port=6333)

def retrieve_context(query: str, top_k: int = 5):
    query_vector = embed_text(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],
        query=query_vector,
        limit=top_k
    ).points

    return [point.payload["text"] for point in results]
