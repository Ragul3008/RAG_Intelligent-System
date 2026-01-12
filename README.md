# 📘 Intelligence System for Academic Notes

An AI-powered **Intelligence System for Academic Notes** that answers student questions **strictly using the provided academic notes**.  
The system uses **semantic search**, **context-bound answering**, and **hallucination control** to ensure accurate and reliable responses.

---

## 🎯 Objective

To design and implement an intelligent question-answering system that:
- Answers **only from given academic notes**
- Retrieves relevant content using **semantic similarity**
- Generates **grounded answers**
- Avoids hallucination
- Refuses to answer when information is not present

---

## ✅ Mandatory Features Implemented

| Feature | Status |
|------|------|
| Text Chunking | ✅ |
| Semantic Search | ✅ |
| Context-Bound Answering | ✅ |
| Hallucination Control | ✅ |
| Source-Based Grounding | ✅ |
| AI-Based Model | ✅ |

---

## 🧠 System Architecture
Academic Notes
↓
Text Cleaning & Chunking
↓
Local Semantic Embeddings
↓
Cosine Similarity Search
↓
Confidence Threshold Check
↓
Context-Bound Prompt
↓
Answer Generation

---

## 📂 Project Structure

medify_ragul/
│
├── app.py # Main CLI application
├── ui.py # Streamlit UI
├── requirements.txt # Dependencies
│
├── config/
│ └── settings.py
│
├── data/
│ └── loader.py
│
├── preprocessing/
│ ├── cleaner.py
│ └── chunker.py
│
├── embeddings/
│ ├── embedder.py
│ └── store.py
│
├── retrieval/
│ └── semantic_retriever.py
│
├── evaluation/
│ └── confidence_gate.py
│
├── llm/
│ ├── prompt_builder.py
│ └── answer_generator.py
│
├── notes/
│ └── notes.txt
│
└── embeddings/
└── embeddings.npy

---

## 🛡️ Hallucination Control

The system prevents hallucinations using:
1. Semantic similarity threshold
2. Top-K retrieval
3. Strict context-only prompt
4. Explicit refusal rule

If the answer is not found:

---

## 🧪 Example Outputs

### Valid Question
What is unsupervised learning?

**Answer:**
> Unsupervised learning involves training models on data without labels.  
> The system tries to find patterns or groupings within the data.

---

### Invalid Question
What is quantum entanglement?

**Answer:**
Information not available in the notes.

---
