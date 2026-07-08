from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    saved_as: str
    content_type: str
    size: int
    page_count: int
    character_count: int
    total_chunks: int
    total_embeddings: int
    status: str