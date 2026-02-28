# Multimodal RAG System Architecture

## Overview

This system implements a Multimodal Retrieval-Augmented Generation (RAG) pipeline capable of processing:

- PDF documents
- Text files
- Images (PNG/JPEG)

It supports cross-modal retrieval and generates grounded responses through a REST API.

---

## System Architecture

The system follows a decoupled modular pipeline:

1. Ingestion
2. Embedding
3. Indexing
4. Retrieval
5. Generation
6. API Layer

---

## 1. Ingestion Layer

Modules:
- document_parser.py
- image_processor.py

Responsibilities:
- Extract text from PDFs using PyMuPDF
- Extract embedded images
- Process standalone images
- Read text files
- Preserve metadata:
  - document_id
  - page_number
  - content_type

Output:
Structured content objects for embedding.

---

## 2. Embedding Layer

Module:
- model_loader.py

Model:
- CLIP (sentence-transformers/clip-ViT-B-32)

Capabilities:
- Text embedding
- Image embedding
- Shared semantic vector space

---

## 3. Vector Store

Module:
- chroma_manager.py

Technology:
- ChromaDB (local persistent storage)

Stores:
- Embeddings
- Metadata
- Raw content reference

---

## 4. Retrieval Layer

Module:
- retriever.py

Steps:
1. Embed user query
2. Perform similarity search
3. Retrieve top-k results
4. Return documents + metadata

Supports:
- Cross-modal retrieval
- Fusion of text + image results

---

## 5. Generation Layer

Module:
- generator.py

Approach:
- Formats retrieved context
- Generates final grounded response
- Returns structured JSON output

No paid APIs required (local generation logic).

---

## 6. API Layer

Framework:
- FastAPI

Endpoint:
POST /query

Flow:
1. Receive query
2. Retrieve relevant content
3. Generate answer
4. Return JSON response

---

## Data Flow Diagram

User Query  
↓  
Retriever  
↓  
Vector Database  
↓  
Context Fusion  
↓  
Generator  
↓  
API Response  

---

## Key Design Decisions

- Decoupled architecture for scalability
- Shared embedding space for multimodal search
- Metadata-rich indexing
- Automatic document ingestion on startup
- Local-only processing (no paid APIs)

---

## Performance

- Startup auto-indexing
- Response latency under 15 seconds
- Supports 10+ diverse documents

---

## Conclusion

This system demonstrates a complete production-style Multimodal RAG pipeline with:

- Text + Image ingestion
- Multimodal embeddings
- Vector indexing
- Cross-modal retrieval
- REST API exposure