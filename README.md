# 🚀 Multimodal RAG System

A production-ready **Multimodal Retrieval-Augmented Generation (RAG)** system that supports PDF documents, text files, and images, enabling cross-modal semantic search and grounded response generation through a REST API.

---

## 📌 Project Overview

This project implements a complete end-to-end **Multimodal RAG pipeline** capable of:

- Extracting text and images from PDFs
- Processing standalone text and image files
- Generating multimodal embeddings using CLIP
- Indexing embeddings in a vector database (ChromaDB)
- Performing semantic similarity search
- Returning grounded answers with source references

All documents placed inside the `sample_documents/` directory are automatically indexed when the server starts.

---

## 🎯 Key Features

- ✅ PDF parsing with text and embedded image extraction  
- ✅ Text file ingestion  
- ✅ Image embedding support  
- ✅ CLIP-based multimodal embeddings  
- ✅ ChromaDB vector indexing  
- ✅ Cross-modal retrieval (text ↔ image)  
- ✅ Source-grounded answers  
- ✅ REST API with Swagger documentation  
- ✅ Automated test suite  

---

## 🏗 System Architecture

The system follows a modular, decoupled pipeline:

1. **Ingestion Layer**
2. **Embedding Layer**
3. **Vector Indexing Layer**
4. **Retrieval Layer**
5. **Generation Layer**
6. **FastAPI API Layer**

For detailed architecture documentation, see:

📄 `ARCHITECTURE.md`

---

## 🛠 Technology Stack

- Python  
- FastAPI  
- PyMuPDF  
- Pillow  
- Sentence Transformers (CLIP model)  
- ChromaDB  
- Uvicorn  
- Pytest  

---
## 📂 Project Structure

```text
multimodal-rag-system/
│
├── src/
│   ├── api/
│   │   └── main.py                # FastAPI application entry point
│   │
│   ├── ingestion/
│   │   ├── document_parser.py     # PDF & text parsing logic
│   │   └── image_processor.py     # Image processing & OCR handling
│   │
│   ├── embeddings/
│   │   └── model_loader.py        # CLIP embedding model loader
│   │
│   ├── retrieval/
│   │   └── retriever.py           # Cross-modal retrieval logic
│   │
│   ├── generation/
│   │   └── generator.py           # Response generation module
│   │
│   └── vector_store/
│       └── chroma_manager.py      # ChromaDB management
│
├── sample_documents/              # Input PDFs, images, text files
│
├── tests/
│   ├── test_ingestion.py
│   └── test_api.py
│
├── requirements.txt               # Python dependencies
├── ARCHITECTURE.md                # System architecture explanation
├── submission.yml                 # Automated evaluation config
└── README.md                      # Project documentation
```

## ⚙️ Setup Instructions
### 1️⃣ Clone Repository
- git clone <your-repo-url>
- cd multimodal-rag
### 2️⃣ Create Virtual Environment
- Windows
- python -m venv venv
venv\Scripts\activate
- Mac/Linux
python3 -m venv venv
source venv/bin/activate
### 3️⃣ Install Dependencies
pip install -r requirements.txt
### 4️⃣ Run the Application
- uvicorn src.api.main:app --reload

- Open API documentation:

http://127.0.0.1:8000/docs
- 📥 Adding Documents

- Place your files inside:

- sample_documents/

Supported formats:

.pdf

.txt

.png

.jpg

.jpeg

- They will be automatically indexed on startup.

### 🔍 API Usage
- Endpoint

POST /query

Example Request
{
  "query": "What is ETL?"
}
Example Response
{
  "answer": "ETL stands for Extract, Transform, Load.",
  "sources": [
    {
      "document_id": "file2.txt",
      "page_number": 1,
      "content_type": "text"
    }
  ]
}
### 🧠 Features

- Automatic document ingestion

- Multimodal embeddings (CLIP-based)

- Cross-modal semantic search

- Metadata-rich indexing

- Source-grounded responses

- Fully documented REST API

- Automated test suite

🧪 Running Tests
pytest
### 🎯 Evaluation Criteria Covered

✔ PDF + Image ingestion
✔ Multimodal embeddings
✔ Cross-modal retrieval
✔ REST API endpoint
✔ JSON response format
✔ Source references
✔ Modular architecture

### 📈 Performance

- Automatic indexing on startup

- Supports 10+ diverse documents

- Average response time < 15 seconds

### 📄 Documentation

- See ARCHITECTURE.md for system design

- See submission.yml for evaluation commands

### 👩‍💻 Author
- Anusha Pavani Venneti
- Multimodal RAG System Implementation
- Data Engineering + Machine Learning Project







