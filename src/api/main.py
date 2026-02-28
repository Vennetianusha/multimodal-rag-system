import os
from fastapi import FastAPI
from pydantic import BaseModel

from src.ingestion.document_parser import DocumentParser
from src.embeddings.model_loader import EmbeddingModel
from src.vector_store.chroma_manager import ChromaManager
from src.retrieval.retriever import Retriever
from src.generation.generator import VLMGenerator

app = FastAPI(title="Multimodal RAG System 🚀")

class QueryRequest(BaseModel):
    query: str


# Global components
parser = DocumentParser()
embedder = EmbeddingModel()
vector_db = ChromaManager()
retriever = Retriever()
generator = VLMGenerator()


@app.on_event("startup")
def load_documents():
    """
    Automatically ingest ALL files inside sample_documents
    """
    print("📂 Loading documents into vector database...")

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../sample_documents"))

    for file in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file)

        if file.endswith(".pdf"):
            results = parser.parse_pdf(file_path)

        elif file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            results = [{
                "document_id": file,
                "page_number": 1,
                "content_type": "text",
                "content": text
            }]

        elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            results = [{
                "document_id": file,
                "page_number": 1,
                "content_type": "image",
                "image_path": file_path
            }]
        else:
            continue

        for idx, item in enumerate(results):

            if item["content_type"] == "text":
                embedding = embedder.embed_text(item["content"])
                document_content = item["content"]

            elif item["content_type"] == "image":
                embedding = embedder.embed_image(item["image_path"])
                document_content = item["image_path"]

            else:
                continue

            metadata = {
                "document_id": item["document_id"],
                "page_number": item["page_number"],
                "content_type": item["content_type"]
            }

            vector_db.add_embedding(
                embedding=embedding,
                metadata=metadata,
                doc_id=f"{file}_{idx}",
                document=document_content
            )

    print("✅ All documents indexed successfully!")


@app.get("/")
def root():
    return {"message": "Multimodal RAG System is running 🚀"}


@app.post("/query")
def query_rag(request: QueryRequest):
    search_results = retriever.search(request.query, top_k=3)

    if not search_results or not search_results.get("documents"):
        return {
            "answer": "No relevant information found in the database.",
            "sources": []
        }

    final_response = generator.generate_answer(request.query, search_results)

    return final_response