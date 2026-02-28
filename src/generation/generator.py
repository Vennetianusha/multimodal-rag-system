class VLMGenerator:
    
    def generate_answer(self, query: str, retrieved_results: dict):

        documents = retrieved_results["documents"][0]
        metadatas = retrieved_results["metadatas"][0]

        answer = "Based on the retrieved information:\n\n"
        sources = []

        for doc, meta in zip(documents, metadatas):

            if not doc:
                continue

            page = meta["page_number"]
            doc_id = meta["document_id"]
            content_type = meta["content_type"]

            if content_type == "text":
                answer += f"According to page {page}, {doc[:300]}...\n\n"
            elif content_type == "image":
                answer += f"As shown in the image on page {page}, relevant visual information is included.\n\n"

            sources.append({
                "document_id": doc_id,
                "page_number": page,
                "content_type": content_type,
                "snippet": doc[:200] if isinstance(doc, str) else str(doc)
            })

        return {
            "answer": answer,
            "sources": sources
        }