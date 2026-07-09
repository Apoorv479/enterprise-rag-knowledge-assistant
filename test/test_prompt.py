from app.schemas.search import SearchResult
from app.services.prompt_service import PromptService

chunks = [
    SearchResult(
        document_id="123",
        chunk_id=1,
        filename="python.pdf",
        page_number=1,
        text="FastAPI is a modern Python framework.",
        score=0.95,
    ),
    SearchResult(
        document_id="123",
        chunk_id=2,
        filename="python.pdf",
        page_number=2,
        text="FastAPI supports async programming.",
        score=0.91,
    ),
]

service = PromptService()

prompt = service.build_prompt(
    question="What is FastAPI?",
    chunks=chunks,
)

print(prompt)
