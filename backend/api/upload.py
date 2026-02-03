import uuid
from fastapi import APIRouter, UploadFile
from backend.utils.parsing import parse_pdf, parse_txt

router = APIRouter()

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

    return {"document_id": doc_id, "text": text}
