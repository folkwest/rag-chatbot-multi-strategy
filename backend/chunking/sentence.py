import nltk
from .base import Chunker

nltk.download("punkt")
from nltk.tokenize import sent_tokenize

class SentenceChunker(Chunker):
    def __init__(self, max_chars=500):
        self.max_chars = max_chars

    def chunk(self, text: str):
        sentences = sent_tokenize(text)
        chunks, current = [], ""

        for sent in sentences:
            if len(current) + len(sent) > self.max_chars:
                chunks.append(current)
                current = sent
            else:
                current += " " + sent

        if current:
            chunks.append(current)

        return chunks
