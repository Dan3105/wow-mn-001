import chromadb
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from feature.rag import Document

class ChromaDbContext:
    def __init__(self):
        self.client = chromadb.HttpClient(host="localhost", port=8000)
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        

    def insert_document(self, 
                        collection_name: str, 
                        documents: list[Document]):
        collection = self.client.get_collection(name=collection_name)
        if collection is not None:
            self.client.delete_collection(name=collection_name)

        chroma = Chroma.from_documents(
            client=self.client,
            documents=documents,
            collection_name=collection_name,
            embedding=self.embeddings
        )

        return True
        
    
#region Search similarity both function in this region return same result however

    """
    All vectorstores expose a similarity_search method. This will take incoming documents
    ,create an embedding of them, and then find all documents with the most similar embedding.
    """
    def similarity_search(self, 
                          query: str,
                          collection_name: str) -> list[Document]:
        db = self.client.get_collection(name=collection_name)
        if db is None:
            return []
        query_embedding = self.embeddings.embed_query(query)
        results = db.query(query_embedding, n_results=10)

        return results
    
# endregion