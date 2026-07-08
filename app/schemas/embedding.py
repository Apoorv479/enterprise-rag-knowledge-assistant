from pydantic import BaseModel


class Embedding(BaseModel):
    """
    Represents a single vector embedding.
    """

    chunk_id: int
    document_id: str
    filename: str
    page_number: int | None = None
    text: str
    vector: list[float]


class EmbeddingList(BaseModel):
    """
    Collection of embeddings.
    """

    total_embeddings: int
    embeddings: list[Embedding]