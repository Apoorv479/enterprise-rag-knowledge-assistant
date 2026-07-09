from fastapi import APIRouter

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
)

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"],
)


@router.post(
    "",
    response_model=SearchResponse,
)
async def semantic_search(
    request: SearchRequest,
):

    return SearchResponse(
        query=request.query,
        total_results=0,
        results=[],
    )