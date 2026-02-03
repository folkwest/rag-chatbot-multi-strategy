import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5