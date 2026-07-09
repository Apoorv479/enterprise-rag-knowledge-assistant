from pydantic import BaseModel


class Chunk(BaseModel):
    """
    Represents a single document chunk.
    """

    chunk_id: int
    document_id: str
    filename: str
    page_number: int | None = None
    text: str
    character_count: int


class ChunkList(BaseModel):
    """
    Collection of chunks generated from a document.
    """

    total_chunks: int
    chunks: list[Chunk]