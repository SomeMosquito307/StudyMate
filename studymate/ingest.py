import fitz
from PIL import Image
import pytesseract
import io

def extract_text_pages(pdf_path, ocr_threshold=80):
    doc = fitz.open(pdf_path)
    pages = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        text = page.get_text("text").strip()
        if len(text) < ocr_threshold:
            pix = page.get_pixmap(dpi=200)
            img = Image.open(io.BytesIO(pix.tobytes()))
            text = pytesseract.image_to_string(img)
        pages.append({"page": i+1, "text": text})
    return pages

if __name__ == '__main__':
    pages = extract_text_pages('sample_data/sample.pdf')
    print(f'Extracted {len(pages)} pages')
