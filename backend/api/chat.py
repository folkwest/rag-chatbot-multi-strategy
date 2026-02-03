from fastapi import APIRouter
from backend.schemas import ChatRequest, ChatResponse
from backend.rag.pipeline import run_rag
from backend.vectorstore.faiss_store import FaissStore

router = APIRouter()
vector_store = FaissStore(dim=1536)

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer, confidence, retrieved = run_rag(
        req.question,
        req.context,
        vector_store,
        req.chunking_strategy
    )

    sources = [{"text": t, "score": s} for t, s in retrieved]

    return {
        "answer": answer,
        "confidence": confidence,
        "sources": sources
    }
