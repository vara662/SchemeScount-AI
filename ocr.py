import pytesseract
from PIL import Image, ImageOps

# Windows only: point to your Tesseract install
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image: Image.Image) -> str:
    gray = ImageOps.grayscale(image)
    return pytesseract.image_to_string(gray, lang="eng")  # use "eng+tam" for Tamil