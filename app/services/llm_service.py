from google import genai

from app.core.config import settings
from app.core.logger import logger


class LLMService:
    """
    Handles communication with Gemini using the new Google GenAI SDK.
    """

    def __init__(self):

        logger.info("Initializing Gemini client.")

        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

        logger.info("Gemini client initialized successfully.")

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate response using Gemini.
        """

        logger.info("Sending prompt to Gemini.")

        response = self.client.models.generate_content(
            model=settings.LLM_MODEL,
            contents=prompt,
        )

        logger.info("Received response from Gemini.")

        return response.text
