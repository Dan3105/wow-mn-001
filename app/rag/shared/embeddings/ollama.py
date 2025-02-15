from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    base_url="http://localhost:11434",
    model="granite-embedding")