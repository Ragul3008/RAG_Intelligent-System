import numpy as np
from embeddings.embedder import embed_text

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_chunks(query, chunks, embeddings, top_k):
    """
    Semantic retrieval using LOCAL embeddings (SentenceTransformer).
    """
    query_embedding = embed_text(query)

    similarities = [
        cosine_similarity(query_embedding, emb)
        for emb in embeddings
    ]

    ranked = sorted(
        enumerate(similarities),
        key=lambda x: x[1],
        reverse=True
    )[:top_k]

    indices = [i for i, _ in ranked]
    scores = [score for _, score in ranked]

    return indices, scores