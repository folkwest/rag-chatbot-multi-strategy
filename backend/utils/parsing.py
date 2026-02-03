from pypdf import PdfReader

def parse_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    return "\n".join(page.extract_text() for page in reader.pages)

def parse_txt(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
