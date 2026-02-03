from .base import Chunker

class FixedChunker(Chunker):
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str):
        chunks = []
        step = self.chunk_size - self.overlap
        for i in range(0, len(text), step):
            chunks.append(text[i:i + self.chunk_size])
        return chunks
