from .pdf_parser import PDFParser
from langchain_core.documents import Document

class DocumentReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_pdf(self) -> list[Document]:
        try:
            loader = PDFParser(file_path=self.file_path)
            return loader.read_pdf()
        except Exception as e:
            raise Exception(f"Error reading PDF file with path: {str(e)}")

