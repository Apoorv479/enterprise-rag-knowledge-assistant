from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.core.config import settings
from app.core.logger import logger
from app.schemas.embedding import Embedding
from app.schemas.search import SearchResult


class VectorService:
    """
    Handles all Qdrant operations.
    """

    def __init__(self):

        logger.info("Connecting to Qdrant.")

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )

        logger.info("Connected to Qdrant.")

    def create_collection(self) -> None:

        collections = self.client.get_collections()

        existing = [collection.name for collection in collections.collections]

        if settings.QDRANT_COLLECTION in existing:

            logger.info("Collection already exists.")
            return

        logger.info("Creating Qdrant collection.")

        self.client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=settings.EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )

        logger.info("Collection created successfully.")

    def insert_embeddings(
        self,
        embeddings: list[Embedding],
    ) -> None:
        """
        Insert embeddings into Qdrant.
        """

        if not embeddings:

            logger.warning("No embeddings received.")
            return

        logger.info(f"Inserting {len(embeddings)} embeddings into Qdrant.")

        points = []

        for embedding in embeddings:

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=embedding.vector,
                    payload={
                        "document_id": embedding.document_id,
                        "chunk_id": embedding.chunk_id,
                        "filename": embedding.filename,
                        "page_number": embedding.page_number,
                        "text": embedding.text,
                    },
                )
            )

        self.client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=points,
            wait=True,
        )

        logger.info("Embeddings inserted successfully.")

    def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
    ) -> list[SearchResult]:
        """
        Perform semantic similarity search.
        """

        logger.info(f"Searching top {top_k} similar chunks.")

        results = self.client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            limit=top_k,
        )

        search_results = []

        for point in results.points:

            payload = point.payload

            search_results.append(
                SearchResult(
                    document_id=payload["document_id"],
                    chunk_id=payload["chunk_id"],
                    filename=payload["filename"],
                    page_number=payload.get("page_number"),
                    text=payload["text"],
                    score=point.score,
                )
            )

        logger.info(f"Retrieved {len(search_results)} chunks.")

        return search_results
