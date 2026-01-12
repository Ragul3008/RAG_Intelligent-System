from sentence_transformers import SentenceTransformer

# Load model once
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    """
    Generate semantic embedding locally (no API, no quota).
    """
    return _model.encode(text).tolist()
