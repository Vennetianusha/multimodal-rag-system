from src.embeddings.model_loader import EmbeddingModel
from src.vector_store.chroma_manager import ChromaManager


class Retriever:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.vector_db = ChromaManager()

    def search(self, query: str, top_k: int = 5):
        query_embedding = self.embedder.embed_text(query)
        results = self.vector_db.query(query_embedding, top_k)
        return results