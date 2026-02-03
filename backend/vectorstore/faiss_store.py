import faiss
import numpy as np

class FaissStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )
        results = []
        for idx, dist in zip(I[0], D[0]):
            results.append((self.texts[idx], float(dist)))
        return results
