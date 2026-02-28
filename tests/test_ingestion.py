import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.document_parser import DocumentParser
from src.embeddings.model_loader import EmbeddingModel
from src.vector_store.chroma_manager import ChromaManager
from src.retrieval.retriever import Retriever
from src.generation.generator import VLMGenerator


def test_complete_multimodal_rag():

    parser = DocumentParser()
    embedder = EmbeddingModel()
    vector_db = ChromaManager()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pdf_path = os.path.join(base_dir, "sample_documents", "sample.pdf")

    # 1️⃣ Ingestion
    results = parser.parse_pdf(pdf_path)

    # 2️⃣ Embedding + Indexing
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
            doc_id=f"id_{idx}",
            document=document_content
        )

    # 3️⃣ Retrieval
    retriever = Retriever()
    query = "What is required in the API section?"
    search_results = retriever.search(query, top_k=3)

    # 4️⃣ Generation
    generator = VLMGenerator()
    final_response = generator.generate_answer(query, search_results)

    print("\nFINAL ANSWER:\n")
    print(final_response)