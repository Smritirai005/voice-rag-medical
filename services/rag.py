import faiss
import os
from sentence_transformers import SentenceTransformer

def load_docs():
    docs = []
    paths = []
    for file in os.listdir("data"):
        with open(f"data/{file}", "r") as f:
            docs.append(f.read())
            paths.append(file)
    return docs, paths

def create_index():
    docs, _ = load_docs()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(docs)
    index = faiss.IndexFlatL2(vectors[0].shape[0])
    index.add(vectors)
    faiss.write_index(index, "embeddings/faiss_index.index")

def retrieve(query, k=3):
    docs, _ = load_docs()
    index = faiss.read_index("embeddings/faiss_index.index")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    q_vec = model.encode([query])
    D, I = index.search(q_vec, k)
    return [docs[i] for i in I[0]]
