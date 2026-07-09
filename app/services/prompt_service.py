from app.core.logger import logger
from app.schemas.search import SearchResult


class PromptService:
    """
    Builds prompts for the LLM.
    """

    def build_prompt(
        self,
        question: str,
        chunks: list[SearchResult],
    ) -> str:
        """
        Build RAG prompt using retrieved context.
        """

        logger.info("Building RAG prompt.")

        context = "\n\n".join(
            [f"[Chunk {chunk.chunk_id}]\n{chunk.text}" for chunk in chunks]
        )

        prompt = f"""
You are an intelligent AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
reply with:

"I don't have enough information in the provided documents."

------------------------
Context
------------------------

{context}

------------------------
Question
------------------------

{question}

------------------------
Answer
------------------------
"""

        logger.info("Prompt built successfully.")

        return prompt
