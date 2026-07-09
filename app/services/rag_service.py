from app.core.logger import logger
from app.schemas.chat import ChatResponse
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.services.retrieval_service import RetrievalService


class RAGService:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):

        self.retrieval_service = RetrievalService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

        logger.info("RAG Service initialized.")

    def ask(
        self,
        question: str,
        top_k: int = 5,
        document_id: str | None = None,
        filename: str | None = None,
    ) -> ChatResponse:

        logger.info("Starting RAG pipeline.")

        # Step 1: Retrieve relevant chunks
        retrieval = self.retrieval_service.semantic_search(
            query=question,
            top_k=top_k,
            document_id=document_id,
            filename=filename,
        )

        # Step 2: Build prompt
        prompt = self.prompt_service.build_prompt(
            question=question,
            chunks=retrieval.results,
        )

        # Step 3: Generate answer
        answer = self.llm_service.generate(prompt)

        logger.info("RAG pipeline completed successfully.")

        return ChatResponse(
            question=question,
            answer=answer,
            retrieved_chunks=len(retrieval.results),
            sources=retrieval.results,
        )
