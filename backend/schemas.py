from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    document_id: Optional[str] = None  # None = search all docs

class SourceChunk(BaseModel):
    text: str
    score: float
    doc_id: str
    filename: str

class ChatResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[SourceChunk]
