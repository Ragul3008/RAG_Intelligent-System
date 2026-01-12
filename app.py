import os
import numpy as np

from config.settings import *
from data.loader import load_notes
from preprocessing.cleaner import clean_text
from preprocessing.chunker import chunk_text
from embeddings.embedder import embed_text
from embeddings.store import save_embeddings, load_embeddings
from retrieval.semantic_retriever import retrieve_chunks
from evaluation.confidence_gate import is_confident
from llm.prompt_builder import build_prompt
from llm.answer_generator import generate_answer

# Load & preprocess notes
raw_notes = load_notes(NOTES_PATH)
cleaned_notes = clean_text(raw_notes)

chunks = chunk_text(
    cleaned_notes,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

# Generate or load embeddings (LOCAL)
if not os.path.exists(EMBEDDINGS_PATH):
    embeddings = [
        embed_text(chunk)        # ✅ FIXED
        for chunk in chunks
    ]
    save_embeddings(np.array(embeddings), EMBEDDINGS_PATH)
else:
    embeddings = load_embeddings(EMBEDDINGS_PATH)

def answer_question(question):
    indices, scores = retrieve_chunks(
        question,
        chunks,
        embeddings,
        TOP_K                     # ✅ FIXED
    )

    if not is_confident(scores, SIMILARITY_THRESHOLD):
        return "Information not available in the notes."

    context = "\n\n".join(
        f"[Chunk {i}] {chunks[i]}"
        for i in indices
    )

    prompt = build_prompt(context, question)
    return generate_answer(prompt, LLM_MODEL)

if __name__ == "__main__":
    print("Academic Notes Intelligence System (Gemini)")
    while True:
        q = input("\nAsk a question (type exit to quit): ")
        if q.lower() == "exit":
            break
        print("\nAnswer:\n", answer_question(q))