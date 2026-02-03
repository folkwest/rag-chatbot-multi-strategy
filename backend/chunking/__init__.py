from .fixed import FixedChunker
from .sentence import SentenceChunker

def get_chunker(strategy: str):
    if strategy == "sentence":
        return SentenceChunker()
    # default
    return FixedChunker()
