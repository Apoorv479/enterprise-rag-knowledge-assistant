from app.core.logger import logger
from app.schemas.search import SearchResponse
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class RetrievalService:
    """
    Handles semantic document retrieval.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

        logger.info("Retrieval Service initialized.")

    def semantic_search(
        self,
        query: str,
        top_k: int,
        document_id: str | None = None,
        filename: str | None = None,
    ) -> SearchResponse:

        logger.info(f"Searching for: {query}")

        # Step 1
        query_embedding = self.embedding_service.generate_query_embedding(query)

        logger.info("Query embedding generated.")

        # Step 2
        results = self.vector_service.search(
            query_vector=query_embedding,
            top_k=top_k,
            document_id=document_id,
            filename=filename,
        )

        logger.info(f"Retrieved {len(results)} chunks.")

        return SearchResponse(
            query=query,
            total_results=len(results),
            results=results,
        )
