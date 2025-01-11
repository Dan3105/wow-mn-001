from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from feature.rag import Document
from langchain_core.output_parsers import StrOutputParser

class GenerationAgent:
    def __init__(self, name):
        self.name = name
        self.ollama_client = ChatOllama(
            model="llama3.2",
            base_url="http://localhost:11434/"
        )

        template = """
        Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        self.prompt_template = ChatPromptTemplate.from_template(template)

    def run(self, context: list[Document], question):
        chain = (
            self.prompt_template |
            self.ollama_client |
            StrOutputParser()
        )
        return chain.invoke({"context":context, "question":question})