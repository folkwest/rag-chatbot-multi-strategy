from backend.utils.embeddings import embed_texts
from backend.rag.generator import generate_answer

def run_rag(question, vector_store, document_id=None):
    query_embedding = embed_texts([question])[0]

    retrieved = vector_store.search(
        query_embedding,
        top_k=5,
        doc_id=document_id
    )

    context_chunks = [r["text"] for r in retrieved]
    answer = generate_answer(question, context_chunks)

    confidence = min(
        1.0,
        sum(1 / (1 + r["score"]) for r in retrieved) / len(retrieved)
        if retrieved else 0.0
    )

    return answer, confidence, retrieved
