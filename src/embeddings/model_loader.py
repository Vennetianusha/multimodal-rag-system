from sentence_transformers import SentenceTransformer
from PIL import Image


class EmbeddingModel:

    def __init__(self):
        # CLIP model supports both text and image embeddings
        self.model = SentenceTransformer("clip-ViT-B-32")

    def embed_text(self, text: str):
        return self.model.encode(text).tolist()

    def embed_image(self, image_path: str):
        image = Image.open(image_path)
        return self.model.encode(image).tolist()