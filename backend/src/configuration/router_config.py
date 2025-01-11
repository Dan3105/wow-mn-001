from fastapi import APIRouter
from api.rag import indexing
from api.rag.agents import generation_agent

router = APIRouter()

@router.get('/')
async def index():
    return {'message': 'Hello World!'}

router.include_router(indexing.router, prefix='/rag/indexing')
router.include_router(generation_agent.router, prefix='/rag/agents')