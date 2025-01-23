from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
import os
from dbcontext.chroma import ChromaDbContext
from feature.rag.indexing.parser import DocumentReader
from feature.rag.indexing.chunk import ChunkOptimization

router = APIRouter()

# @router.get('collection/exists/')
# async def check_collections_exists(file: str = Form(...)):
#     norm_file = os.path.normpath(file)
#     context = ChromaDbContext()
#     try:
#         exists = context.client.get_collection(norm_file)
#         if exists is not None:
#             return JSONResponse(status_code=200, content={"message": "Directory exists"})
#         raise HTTPException(status_code=404, detail="Cannot find this collection")
#     except Exception:
#         raise HTTPException(status_code=404, detail="Cannot find this collection")


@router.post('/request-chunking')
async def request_chunking(path: str = Form(...)):
    _, extension = os.path.splitext(path)

    if extension != '.pdf':
        raise HTTPException(status_code=400, 
                            detail=f"Current implementation doesn't support this file type {extension}")
    
    try:
        reader = DocumentReader(file_path=path)
        documents = reader.read_pdf()
        optimizer = ChunkOptimization()
        chunk_documents = optimizer.simple_split(documents)
        context = ChromaDbContext()
        context.insert_document(path, chunk_documents)
        
        return JSONResponse(content={"message": "Chunking request successful"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

