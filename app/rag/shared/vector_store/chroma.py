import os
import chromadb
from langchain_chroma import Chroma
from app.rag.shared.embeddings.ollama import embeddings
from app.config import Config

chroma_client = chromadb.HttpClient(
    host=Config.CHROMA_HOST, port=Config.CHROMA_PORT
)

vector_store = Chroma(
    client=chroma_client, 
    embedding_function=embeddings
)

def build_retriever(chat_args):
    search_kwargs = {"filter": { "file_id": chat_args.file_id }}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )