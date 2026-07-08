from uuid import uuid4

from fastapi import UploadFile

from app.core.logger import logger
from app.services.pdf_service import PDFService
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class DocumentIngestionService:
    """
    Handles the complete RAG document ingestion pipeline.
    """

    def __init__(self):

        self.pdf_service = PDFService()
        self.chunking_service = ChunkingService()
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

        logger.info("Document Ingestion Service initialized.")

    async def ingest_document(
        self,
        file: UploadFile,
    ) -> dict:

        logger.info("Starting document ingestion pipeline.")

        # Step 1: Validate PDF
        self.pdf_service.validate_pdf(file)

        # Step 2: Generate Document ID
        document_id = str(uuid4())

        # Step 3: Generate Unique Filename
        unique_filename = self.pdf_service.generate_filename()

        # Step 4: Save PDF
        file_path, content = await self.pdf_service.save_file(
            file=file,
            filename=unique_filename,
        )

        # Step 5: Extract Text
        metadata = self.pdf_service.extract_text_and_metadata(
            file_path
        )

        logger.info("PDF text extracted successfully.")

        # Step 6: Create Chunks
        chunks = self.chunking_service.create_chunks(
            text=metadata["text"],
            document_id=document_id,
            filename=file.filename,
        )

        logger.info(f"Created {len(chunks)} chunks.")

        # Step 7: Generate Embeddings
        embeddings = self.embedding_service.generate_embeddings(
            chunks
        )

        logger.info(f"Generated {len(embeddings)} embeddings.")

        # Step 8: Store Embeddings in Qdrant
        self.vector_service.insert_embeddings(
            embeddings
        )

        logger.info("Embeddings stored successfully in Qdrant.")

        return {
            "document_id": document_id,
            "filename": file.filename,
            "saved_as": unique_filename,
            "content_type": file.content_type,
            "size": len(content),
            "page_count": metadata["page_count"],
            "character_count": metadata["character_count"],
            "total_chunks": len(chunks),
            "total_embeddings": len(embeddings),
            "status": "Indexed Successfully",
        }