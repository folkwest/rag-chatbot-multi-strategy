from backend.chunking.fixed import FixedChunker
from backend.chunking.sentence import SentenceChunker
from backend.utils.embeddings import embed_texts
from backend.rag.retriever import retrieve
from backend.rag.generator import generate_answer

def get_chunker(strategy: str):
    if strategy == "sentence":
        return SentenceChunker()
    return FixedChunker()

def run_rag(question, text, vector_store, strategy):
    chunker = get_chunker(strategy)
    chunks = chunker.chunk(text)

    embeddings = embed_texts(chunks)
    vector_store.add(embeddings, chunks)

    query_embedding = embed_texts([question])[0]
    retrieved = retrieve(vector_store, query_embedding, top_k=5)

    context_chunks = [c for c, _ in retrieved]
    answer = generate_answer(question, context_chunks)

    confidence = min(1.0, sum(1/(1+d) for _, d in retrieved) / len(retrieved))

    return answer, confidence, retrieved
