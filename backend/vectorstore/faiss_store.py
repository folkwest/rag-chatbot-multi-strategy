import faiss
import numpy as np

class FaissStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.metadatas = []

    def add(self, embeddings, texts, metadatas):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)
        self.metadatas.extend(metadatas)

    def search(self, query_embedding, top_k=5, doc_id=None):
        D, I = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k * 3  # over-fetch for filtering
        )

        results = []
        for idx, dist in zip(I[0], D[0]):
            meta = self.metadatas[idx]
            if doc_id and meta["doc_id"] != doc_id:
                continue
            results.append({
                "text": self.texts[idx],
                "score": float(dist),
                "metadata": meta
            })
            if len(results) >= top_k:
                break

        return results

vector_store = FaissStore(dim=1536)