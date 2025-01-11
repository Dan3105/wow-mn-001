from langchain_text_splitters import RecursiveCharacterTextSplitter
from feature.rag import Document

class ChunkOptimization:
    def __init__(self, chunk_size: int = 512,
                 chunk_overlap: int = 128,
                 add_start_index: bool = True,
                 **kwargs):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            add_start_index=add_start_index,
            **kwargs
        )

    def simple_split(self, data: list[Document]) -> list[Document]:
        return self.splitter.split_documents(data)