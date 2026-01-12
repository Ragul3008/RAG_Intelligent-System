import numpy as np
import os

def save_embeddings(embeddings, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path, embeddings)

def load_embeddings(path):
    return np.load(path)
