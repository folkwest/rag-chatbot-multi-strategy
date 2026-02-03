class DocumentStore:
    def __init__(self):
        self.documents = {}

    def add(self, doc_id: str, filename: str):
        self.documents[doc_id] = {
            "filename": filename
        }

    def exists(self, doc_id: str) -> bool:
        return doc_id in self.documents

    def list_docs(self):
        return self.documents

doc_store = DocumentStore()