from fastapi import APIRouter, UploadFile, Form
from backend.chunking import get_chunker
from backend.utils.parsing import parse_pdf, parse_txt
from backend.utils.embeddings import embed_texts
from backend.vectorstore.faiss_store import vector_store
from backend.storage.document_store import doc_store
import uuid

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile, chunking_strategy: str = Form("fixed")):
    doc_id = str(uuid.uuid4())
    path = f"/tmp/{doc_id}_{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):
        text = parse_pdf(path)
    else:
        text = parse_txt(path)

    # get chosen chunker
    chunker = get_chunker(chunking_strategy)
    chunks = chunker.chunk(text)

    embeddings = embed_texts(chunks)

    metadatas = [
        {
            "doc_id": doc_id,
            "filename": file.filename,
            "chunk_id": i,
            "chunking_strategy": chunking_strategy
        }
        for i in range(len(chunks))
    ]

    vector_store.add(embeddings, chunks, metadatas)
    doc_store.add(doc_id, file.filename)

    return {
        "document_id": doc_id,
        "num_chunks": len(chunks),
        "filename": file.filename,
        "chunking_strategy": chunking_strategy
    }
