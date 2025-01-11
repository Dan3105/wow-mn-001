from fastapi import APIRouter
from pydantic import BaseModel
from feature.rag.agents.generation_agent import GenerationAgent
from feature.rag.indexing.dbcontext.chroma import ChromaDbContext

router = APIRouter()

class PromptRequest(BaseModel):
    collection_name: str = ""
    prompt: str = ""

@router.post("/generate")
async def generate(query: PromptRequest) -> dict:
    agent = GenerationAgent(name="generation_agent")

    context = ChromaDbContext()
    results = context.similarity_search(query.prompt, query.collection_name)

    response = agent.run(results, query.prompt)

    return {"response": response}