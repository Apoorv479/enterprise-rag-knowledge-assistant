from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings
from app.core.logger import logger
from app.schemas.chunk import Chunk


class ChunkingService:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def create_chunks(
    self,
    text: str,
    document_id: str,
    filename: str,
) -> list[Chunk]:
        """
        Split extracted text into chunks.
        """

        logger.info("Starting document chunking.")

        if not text.strip():
            logger.warning("Received empty text.")
            return []

        raw_chunks = self.text_splitter.split_text(text)

        processed_chunks = []

        for index, chunk in enumerate(raw_chunks, start=1):

            cleaned_chunk = chunk.strip()

            if not cleaned_chunk:
                continue

            processed_chunks.append(
                Chunk(
        chunk_id=index,
        document_id=document_id,
        filename=filename,
        page_number=None,
        text=cleaned_chunk,
        character_count=len(cleaned_chunk),
    )
            )

        logger.info(
            f"Chunking completed successfully. Total chunks: {len(processed_chunks)}"
        )

        return processed_chunks