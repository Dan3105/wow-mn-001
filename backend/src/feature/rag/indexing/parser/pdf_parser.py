from langchain_community.document_loaders import PyPDFLoader
from feature.rag import Document

class PDFParser():
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_pdf(self) -> list[Document]:
        loader = PyPDFLoader(file_path=self.file_path)
        return loader.load()
        