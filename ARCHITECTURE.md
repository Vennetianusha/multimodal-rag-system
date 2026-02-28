# 🏗 Multimodal RAG System Architecture

## Overview

This system implements a complete Multimodal Retrieval-Augmented Generation (RAG) pipeline.

It supports:
- PDF ingestion
- Text ingestion
- Image ingestion
- Multimodal embeddings
- Cross-modal retrieval
- REST API interface

---

## System Flow

User Query
    ↓
Retriever
    ↓
Vector Database (ChromaDB)
    ↓
Context Construction
    ↓
Generator
    ↓
API Response

---

## Architecture Components

### 1️⃣ Ingestion Layer
- Parses PDFs (PyMuPDF)
- Extracts text + images
- Processes standalone text files
- Processes standalone images

### 2️⃣ Embedding Layer
- Uses CLIP model from Sentence Transformers
- Generates embeddings for:
  - Text
  - Images

### 3️⃣ Vector Store
- ChromaDB
- Stores embeddings + metadata:
  - document_id
  - page_number
  - content_type

### 4️⃣ Retrieval Layer
- Performs semantic similarity search
- Supports cross-modal retrieval
- Returns top-k relevant chunks

### 5️⃣ Generation Layer
- Formats retrieved context
- Generates grounded response
- Returns answer + sources

---

## Design Decisions

- Modular architecture for clarity
- Automatic indexing on startup
- Local execution (no paid API required)
- FastAPI for performance