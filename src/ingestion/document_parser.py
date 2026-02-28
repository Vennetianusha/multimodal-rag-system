import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image


class DocumentParser:

    def parse_pdf(self, file_path):
        results = []
        doc = fitz.open(file_path)

        document_id = os.path.basename(file_path)

        for page_number in range(len(doc)):
            page = doc[page_number]

            # Extract text
            text = page.get_text()
            if text.strip():
                results.append({
                    "document_id": document_id,
                    "page_number": page_number + 1,
                    "content_type": "text",
                    "content": text
                })

            # Extract images
            image_list = page.get_images(full=True)

            for img_index, img in enumerate(image_list):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                if pix.n < 5:
                    img_path = f"sample_documents/page_{page_number+1}_img_{img_index}.png"
                    pix.save(img_path)

                    # OCR on image
                    ocr_text = pytesseract.image_to_string(Image.open(img_path))

                    results.append({
                        "document_id": document_id,
                        "page_number": page_number + 1,
                        "content_type": "image",
                        "image_path": img_path,
                        "ocr_text": ocr_text
                    })

                pix = None

        return results


    def parse_image(self, file_path):
        results = []

        document_id = os.path.basename(file_path)

        # OCR
        ocr_text = pytesseract.image_to_string(Image.open(file_path))

        results.append({
            "document_id": document_id,
            "page_number": 1,
            "content_type": "image",
            "image_path": file_path,
            "ocr_text": ocr_text
        })

        return results


    def parse_text(self, file_path):
        results = []

        document_id = os.path.basename(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        results.append({
            "document_id": document_id,
            "page_number": 1,
            "content_type": "text",
            "content": text
        })

        return results