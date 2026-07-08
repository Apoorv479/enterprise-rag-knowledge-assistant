from fastapi import APIRouter, File, UploadFile
from app.schemas.document import DocumentUploadResponse
from app.services.document_ingestion_service import (
    DocumentIngestionService,
)
router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)
document_ingestion_service = DocumentIngestionService()

@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=201,
)
async def upload_document(
    file: UploadFile = File(...),
):
    return await document_ingestion_service.ingest_document(file)