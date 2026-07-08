from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.core.logger import logger
from app.schemas.chunk import Chunk
from app.schemas.embedding import Embedding


class EmbeddingService:
    """
    Generates vector embeddings for document chunks.
    """

    def __init__(self):

        logger.info(
            f"Loading embedding model: {settings.EMBEDDING_MODEL}"
        )

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

        logger.info("Embedding model loaded successfully.")

    def generate_embeddings(
        self,
        chunks: list[Chunk],
    ) -> list[Embedding]:

        if not chunks:

            logger.warning("No chunks received.")

            return []

        logger.info(
            f"Generating embeddings for {len(chunks)} chunks."
        )

        texts = [chunk.text for chunk in chunks]

        vectors = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        embeddings = []

        for chunk, vector in zip(chunks, vectors):

            embeddings.append(
                Embedding(
    chunk_id=chunk.chunk_id,
    document_id=chunk.document_id,
    filename=chunk.filename,
    page_number=chunk.page_number,
    text=chunk.text,
    vector=vector.tolist(),
)
            )

        logger.info(
            f"Generated {len(embeddings)} embeddings."
        )

        return embeddings