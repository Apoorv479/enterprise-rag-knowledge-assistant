from pydantic import BaseModel, Field

from app.schemas.search import SearchResult


class ChatRequest(BaseModel):
    """
    User question for RAG.
    """

    question: str = Field(
        ...,
        min_length=3,
        description="User question",
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
    )

    document_id: str | None = None

    filename: str | None = None


class ChatResponse(BaseModel):
    """
    Final RAG response.
    """

    question: str

    answer: str

    retrieved_chunks: int

    sources: list[SearchResult]
