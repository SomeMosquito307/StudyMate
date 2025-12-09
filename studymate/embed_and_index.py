from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

MODEL = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL)

def build_index(chunks, index_path='faiss.index', meta_path='meta.pkl'):
    embeddings = model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    faiss.write_index(index, index_path)
    with open(meta_path, 'wb') as f:
        pickle.dump(chunks, f)
    return index_path, meta_path

def search(query, k=6, index_path='faiss.index', meta_path='meta.pkl'):
    q_emb = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)
    index = faiss.read_index(index_path)
    D, I = index.search(q_emb, k)
    with open(meta_path, 'rb') as f:
        chunks = pickle.load(f)
    results = []
    for idx, score in zip(I[0], D[0]):
        results.append({'score': float(score), 'text': chunks[idx]})
    return results
