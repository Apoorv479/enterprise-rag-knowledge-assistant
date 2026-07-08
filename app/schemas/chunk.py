from pydantic import BaseModel


class Chunk(BaseModel):
    """
    Represents a single document chunk.
    """

    chunk_id: int
    text: str
    character_count: int


class ChunkList(BaseModel):
    """
    Collection of chunks.
    """

    total_chunks: int
    chunks: list[Chunk]