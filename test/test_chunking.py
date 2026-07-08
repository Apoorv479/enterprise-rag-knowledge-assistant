from app.services.chunking_service import ChunkingService

service = ChunkingService()

sample_text = """
FastAPI is a modern Python web framework.

It is widely used for backend development.

RAG systems use chunking before embedding generation.

Chunk overlap preserves context.
""" * 300

chunks = service.create_chunks(sample_text)

print(f"Total Chunks: {len(chunks)}")

for index, chunk in enumerate(chunks[:3], start=1):
    print(f"\nChunk {index}")
    print("-" * 40)
    print(chunk[:200])