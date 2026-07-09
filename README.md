# Enterprise RAG Backend

A production-oriented Retrieval-Augmented Generation (RAG) backend built with FastAPI, Qdrant Vector Database, and Sentence Transformers. The project enables intelligent document ingestion, semantic search, and context-aware question answering over enterprise knowledge bases.

---

# Features

## Document Ingestion

- Upload PDF documents
- PDF validation
- Secure file storage
- UUID-based document identification
- Metadata extraction

## Text Processing

- PDF text extraction using PyMuPDF
- Recursive text chunking
- Configurable chunk size
- Configurable chunk overlap
- Chunk metadata generation

## Embedding Generation

- Sentence Transformer embeddings
- Batch embedding generation
- Configurable embedding model
- Normalized embeddings for semantic search

## Vector Database

- Qdrant Vector Database integration
- Automatic collection creation
- Batch vector indexing
- Metadata payload storage
- Cosine similarity search configuration

## Semantic Retrieval

- Query embedding generation
- Top-K semantic search
- Metadata-based filtering
- Similarity score ranking
- Context retrieval

## RAG Pipeline

- Prompt construction
- LLM integration
- Context-aware response generation
- Source citation
- Multi-document retrieval

---

# System Architecture

```text
                    Client
                       │
                       ▼
                 FastAPI Backend
                       │
                       ▼
          Document Ingestion Service
                       │
 ┌─────────────────────┼─────────────────────┐
 │                     │                     │
 ▼                     ▼                     ▼
PDF Service      Chunking Service    Embedding Service
                                              │
                                              ▼
                                       Vector Service
                                              │
                                              ▼
                                    Qdrant Vector Database
                                              │
                                              ▼
                                      Semantic Retrieval
                                              │
                                              ▼
                                      Prompt Construction
                                              │
                                              ▼
                                      Large Language Model
                                              │
                                              ▼
                                   Context-Aware Response
```

---

# Project Structure

```text
RAG-Backend/
│
├── app/
│   ├── api/
│   │   ├── router.py
│   │   └── routes/
│   │       ├── health.py
│   │       └── upload.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── schemas/
│   │   ├── chunk.py
│   │   ├── document.py
│   │   └── embedding.py
│   │
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── chunking_service.py
│   │   ├── embedding_service.py
│   │   ├── vector_service.py
│   │   └── document_ingestion_service.py
│   │
│   └── main.py
│
├── uploads/
├── requirements.txt
├── README.md
└── .env
```

---

# Technology Stack

| Category          | Technology                               |
| ----------------- | ---------------------------------------- |
| Language          | Python 3.12                              |
| Backend Framework | FastAPI                                  |
| Validation        | Pydantic v2                              |
| Vector Database   | Qdrant                                   |
| Embedding Model   | all-MiniLM-L6-v2                         |
| PDF Processing    | PyMuPDF                                  |
| Text Chunking     | LangChain RecursiveCharacterTextSplitter |
| API Testing       | Swagger UI, Postman                      |
| ASGI Server       | Uvicorn                                  |

---

# Document Ingestion Pipeline

```text
PDF Upload
     │
     ▼
PDF Validation
     │
     ▼
Store PDF
     │
     ▼
Extract Text
     │
     ▼
Recursive Chunking
     │
     ▼
Embedding Generation
     │
     ▼
Batch Vector Indexing
     │
     ▼
Qdrant Vector Database
```

---

# Retrieval Pipeline

```text
User Query
     │
     ▼
Generate Query Embedding
     │
     ▼
Semantic Similarity Search
     │
     ▼
Top-K Relevant Chunks
     │
     ▼
Prompt Construction
     │
     ▼
Large Language Model
     │
     ▼
Context-Aware Answer
```

---

# REST APIs

## Health Check

```http
GET /health
```

Returns application status.

---

## Upload Document

```http
POST /documents/upload
```

Uploads and indexes a PDF document into the vector database.

---

## Semantic Search

```http
POST /search
```

Performs semantic similarity search.

---

## Chat / Question Answering

```http
POST /chat
```

Returns context-aware answers using the indexed documents.

---

# Environment Variables

```env
APP_NAME=Enterprise RAG Backend
APP_VERSION=1.0.0

HOST=127.0.0.1
PORT=8000

MAX_FILE_SIZE=10485760

CHUNK_SIZE=1000
CHUNK_OVERLAP=200

EMBEDDING_MODEL=all-MiniLM-L6-v2
EMBEDDING_DIMENSION=384

QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION=documents
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/rag-backend.git
```

Navigate to the project

```bash
cd rag-backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the development server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Current Development Status

| Module                            | Status    |
| --------------------------------- | --------- |
| FastAPI Backend                   | Completed |
| Configuration Management          | Completed |
| Logging                           | Completed |
| PDF Upload                        | Completed |
| PDF Text Extraction               | Completed |
| Recursive Chunking                | Completed |
| Embedding Generation              | Completed |
| Qdrant Integration                | Completed |
| Batch Vector Indexing             | Completed |
| Semantic Search                   | Completed |
| Top-K Retrieval                   | Completed |
| Metadata Filtering                | Completed |
| RAG Inference Pipeline            | Completed |
| Conversational Question Answering | Completed |

---

# Future Enhancements

- Hybrid Search (Dense + Sparse Retrieval)
- Metadata Filtering
- Background Document Indexing
- Multi-file Upload
- JWT Authentication
- Conversation History
- Streaming Responses
- Redis Caching
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- Prometheus Monitoring
- Grafana Dashboard
- Unit and Integration Tests

---

# Learning Objectives

This project demonstrates:

- Production-ready FastAPI architecture
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Approximate Nearest Neighbor (ANN) Search
- Enterprise Backend Development
- Modular Service Architecture
- Clean Code Principles
- Scalable API Design

---

# License

This project is intended for educational, learning, and portfolio purposes.
