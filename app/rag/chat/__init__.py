from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from app.rag.shared.models import ChatArgs
from app.rag.shared.vector_store.chroma import build_retriever
from app.rag.shared.memories.sql_memory import build_memory
from app.rag.shared.llms.chatollama import build_llm

def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    retriever = build_retriever(chat_args=chat_args)
    llm = build_llm(chat_args=chat_args)
    memory = build_memory(chat_args=chat_args)

    return ConversationalRetrievalChain.from_llm(
        retriever=retriever,
        llm=llm,
        memory=memory
    )
