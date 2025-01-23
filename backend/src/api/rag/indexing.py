from fastapi import APIRouter
from pydantic import BaseModel
from feature.rag.indexing.parser import DocumentReader
from feature.rag.indexing.chunk import ChunkOptimization
from dbcontext.chroma import ChromaDbContext
import os.path

router = APIRouter()

class PDFPath(BaseModel):
    path: str
    collection_name: str = ""

    @property
    def formatted_path(self) -> str:
        clean_path = os.path.normpath(self.path)
        clean_path = clean_path.replace("\\", "/")
        return clean_path
    
class Query(BaseModel):
    query: str
    collection_name: str = ""

# @router.post("/upload-pdf")
# async def read_pdf(pdf_path: PDFPath) -> dict:
#     reader = DocumentReader(file_path=pdf_path.formatted_path)
#     documents = reader.read_pdf()
#     return {
#             "length": len(documents),
#             "documents": [
#                 {
#                     "page_content": doc.page_content,
#                     "metadata": doc.metadata
#                 } for doc in documents
#             ]
#         }

# @router.post("/upload-pdf/chunk")
# async def read_pdf(pdf_path: PDFPath) -> dict:
#     reader = DocumentReader(file_path=pdf_path.formatted_path)
#     documents = reader.read_pdf()
#     optimizer = ChunkOptimization()
#     chunk_documents = optimizer.simple_split(documents)
#     return {
#             "length": len(chunk_documents),
#             "documents": [
#                 {
#                     "page_content": doc.page_content,
#                     "metadata": doc.metadata
#                 } for doc in chunk_documents
#             ]
#         }

@router.post("/upload-pdf/")
async def read_pdf(pdf_path: PDFPath) -> dict:
    reader = DocumentReader(file_path=pdf_path.formatted_path)
    documents = reader.read_pdf()
    optimizer = ChunkOptimization()
    chunk_documents = optimizer.simple_split(documents)

    context = ChromaDbContext()
    response = context.insert_document(pdf_path.collection_name, chunk_documents)

    return {
        "response": response   
    }

@router.post("/search")
async def search(query: Query) -> dict:
    context = ChromaDbContext()
    results = context.similarity_search(query.query, query.collection_name)
    
    # Extract only documents and metadata from QueryResult
    return {
        "results": [
            {
                "document": doc,
                "metadata": meta[0] if meta else None,
                "distance": dist[0] if dist else None
            } for doc, meta, dist in zip(
                results.get("documents", []), 
                results.get("metadata", []), 
                results.get("distances", [])
            )
        ] if results.get("documents") else []
    }