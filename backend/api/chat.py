from fastapi import APIRouter
from backend.schemas import ChatRequest, ChatResponse
from backend.rag.pipeline import run_rag
from backend.api.upload import vector_store

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer, confidence, retrieved = run_rag(
        req.question,
        vector_store,
        req.document_id
    )

    sources = [
        {
            "text": r["text"],
            "score": r["score"],
            "doc_id": r["metadata"]["doc_id"],
            "filename": r["metadata"]["filename"]
        }
        for r in retrieved
    ]

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }

