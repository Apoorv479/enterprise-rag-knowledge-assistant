from pathlib import Path
from uuid import uuid4

import fitz
from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.core.logger import logger


class PDFService:
    """
    Handles all PDF related operations.
    """

    def __init__(self):
        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def validate_pdf(self, file: UploadFile) -> None:
        """
        Validate uploaded PDF.
        """

        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename is missing."
            )

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Invalid content type."
            )

    def generate_filename(self) -> str:
        """
        Generate unique filename.
        """

        return f"{uuid4()}.pdf"

    async def save_file(
        self,
        file: UploadFile,
        filename: str,
    ) -> tuple[Path, bytes]:

        file_path = self.upload_dir / filename

        content = await file.read()

        if len(content) > settings.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="Maximum file size exceeded."
            )

        with open(file_path, "wb") as pdf:
            pdf.write(content)

        logger.info(f"PDF saved successfully: {filename}")

        return file_path, content

    def extract_text_and_metadata(
        self,
        file_path: Path,
    ) -> dict:
        """
        Extract text and metadata in a single pass.
        """

        try:

            document = fitz.open(file_path)

            extracted_text = []

            for page in document:
                extracted_text.append(page.get_text())

            text = "".join(extracted_text)

            metadata = {
                "text": text,
                "page_count": document.page_count,
                "character_count": len(text),
            }

            document.close()

            logger.info("Text extraction completed.")

            return metadata

        except Exception as e:

            logger.error(f"PDF extraction failed: {str(e)}")

            raise HTTPException(
                status_code=500,
                detail="Unable to process PDF."
            )

    

async def process_pdf(
    self,
    file: UploadFile,
) -> dict:

    logger.info("Starting PDF upload process.")

    # Step 1: Validate uploaded PDF
    self.validate_pdf(file)

    # Step 2: Generate document ID
    document_id = str(uuid4())

    # Step 3: Generate unique filename for storage
    unique_filename = self.generate_filename()

    # Step 4: Save uploaded file
    file_path, content = await self.save_file(
        file=file,
        filename=unique_filename,
    )

    # Step 5: Extract text and metadata
    metadata = self.extract_text_and_metadata(file_path)

    logger.info("PDF processing completed successfully.")

    return {
        "document_id": document_id,
        "filename": file.filename,
        "saved_as": unique_filename,
        "content_type": file.content_type,
        "size": len(content),
        "page_count": metadata["page_count"],
        "character_count": metadata["character_count"],
        "message": "Document uploaded successfully.",
    }