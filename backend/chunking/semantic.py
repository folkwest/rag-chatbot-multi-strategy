from backend.utils.embeddings import embed_texts
import numpy as np

class SemanticChunker:
    def __init__(self, chunk_size=200, overlap=75):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str):
        words = text.split()
        chunks = []
        start = 0
        while start < len(words):
            end = min(start + self.chunk_size, len(words))
            chunk = " ".join(words[start:end]).strip()
            if chunk:  # skip empty chunks
                chunks.append(chunk)
            start += self.chunk_size - self.overlap
        return chunks

