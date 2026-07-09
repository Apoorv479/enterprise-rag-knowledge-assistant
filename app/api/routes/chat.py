from fastapi import APIRouter

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["RAG Chat"],
)

rag_service = RAGService()


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):

    return rag_service.ask(
        question=request.question,
        top_k=request.top_k,
        document_id=request.document_id,
        filename=request.filename,
    )
