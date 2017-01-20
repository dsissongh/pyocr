from PIL import Image
import pytesseract
import sys

sys.path.append("C:\\Program Files\\Tesseract-OCR")
image = Image.open("c:\\projects\\pyocr\\pyocr\\test2.jpg")

print(pytesseract.image_to_string(image))