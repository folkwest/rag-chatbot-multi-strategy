from fastapi import FastAPI
from backend.api import upload, chat

app = FastAPI(title="RAG Chatbot")

app.include_router(upload.router)
app.include_router(chat.router)
