from rag import OpenAI, Dict, Any
import json

class BaseAgent:
    def __init__(self, name: str, instructions: str
                 , chat_model: str = "llama3.2"
                 , api_key: str = "ollama"
                 , max_tokens: int = 2000
                 , temperature: float = 0.5):
        self.name = name
        self.instructions = instructions
        self.chat_model = chat_model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.ollama_client = OpenAI(
            base_url="http//localhost:11434/v1",
            api_key=api_key,
        )

    async def run(self, messages: str) -> Dict[str, Any]:
        raise NotImplementedError("run method must be implemented in subclass")
    
    