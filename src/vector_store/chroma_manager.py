import chromadb


class ChromaManager:

    def __init__(self):
        self.client = chromadb.Client()

        try:
            self.collection = self.client.get_collection("multimodal_collection")
        except:
            self.collection = self.client.create_collection(
                name="multimodal_collection"
            )

    def reset(self):
        try:
            self.client.delete_collection("multimodal_collection")
        except:
            pass

        self.collection = self.client.create_collection(
            name="multimodal_collection"
        )

    def add_embedding(self, embedding, metadata, doc_id, document):

        self.collection.add(
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[doc_id],
            documents=[document]
        )

    def query(self, embedding, top_k=3):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )