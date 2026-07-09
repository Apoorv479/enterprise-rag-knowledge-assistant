from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    """
    User query for semantic search.
    """

    query: str = Field(
        ...,
        min_length=3,
        description="User search query",
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of similar chunks to retrieve",
    )

    document_id: str | None = Field(
        default=None,
        description="Search only inside a specific document",
    )

    filename: str | None = Field(
        default=None,
        description="Search only inside a specific file",
    )


class SearchResult(BaseModel):
    """
    Single retrieved chunk.
    """

    document_id: str
    chunk_id: int
    filename: str
    page_number: int | None = None
    text: str
    score: float


class SearchResponse(BaseModel):
    """
    Semantic search response.
    """

    query: str
    total_results: int
    results: list[SearchResult]
