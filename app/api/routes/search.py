from fastapi import APIRouter

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
)
from app.services.retrieval_service import RetrievalService

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"],
)

retrieval_service = RetrievalService()


@router.post(
    "",
    response_model=SearchResponse,
)
async def semantic_search(
    request: SearchRequest,
):

    return retrieval_service.semantic_search(
        query=request.query,
        top_k=request.top_k,
        document_id=request.document_id,
        filename=request.filename,
    )
