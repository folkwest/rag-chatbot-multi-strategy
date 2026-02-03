import uuid
from fastapi import APIRouter, UploadFile
from backend.utils.parsing import parse_pdf, parse_txt
from backend.chunking.fixed import FixedChunker
from backend.utils.embeddings import embed_texts
from backend.vectorstore.faiss_store import FaissStore
from backend.storage.document_store import DocumentStore

router = APIRouter()

vector_store = FaissStore(dim=1536)
doc_store = DocumentStore()

@router.post("/upload")
async def upload(file: UploadFile):
    doc_id = str(uuid.uuid4())
    path = f"/tmp/{doc_id}_{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):
        text = parse_pdf(path)
    else:
        text = parse_txt(path)

    chunker = FixedChunker()
    chunks = chunker.chunk(text)
    embeddings = embed_texts(chunks)

    metadatas = [
        {
            "doc_id": doc_id,
            "filename": file.filename,
            "chunk_id": i
        }
        for i in range(len(chunks))
    ]

    vector_store.add(embeddings, chunks, metadatas)
    doc_store.add(doc_id, file.filename)

    return {
        "document_id": doc_id,
        "num_chunks": len(chunks),
        "filename": file.filename
    }
