from pydantic import BaseModel
from typing import List, Optional

class UploadResponse(BaseModel):
    document_id: str
    num_chunks: int

class ChatRequest(BaseModel):
    question: str
    chunking_strategy: str

class SourceChunk(BaseModel):
    text: str
    score: float

class ChatResponse(BaseModel):
    answer: str
    confidence: float
    sources: List[SourceChunk]