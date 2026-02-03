from fastapi import APIRouter
from backend.schemas import ChatRequest, ChatResponse
from backend.rag.pipeline import run_rag
from backend.vectorstore.faiss_store import vector_store

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # req.chunking_strategy can now be a list or single
    strategies = req.chunking_strategy
    if isinstance(strategies, str):
        strategies = [strategies]

    all_results = []

    for strat in strategies:
        answer, confidence, retrieved = run_rag(
            req.question,
            vector_store,
            req.document_id,
            chunking_strategy=strat
        )

        sources = [
            {
                "text": r["text"],
                "score": r["score"],
                "doc_id": r["metadata"]["doc_id"],
                "filename": r["metadata"]["filename"],
                "chunking_strategy": r["metadata"]["chunking_strategy"]
            }
            for r in retrieved
        ]

        all_results.append({
            "strategy": strat,
            "answer": answer,
            "confidence": confidence,
            "sources": sources
        })

    return {"results": all_results}

