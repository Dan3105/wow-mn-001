from langchain.chat_models.ollama import ChatOllama

def build_llm(chat_args):
    return ChatOllama(
        model="llama3.2"
    )