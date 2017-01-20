from PIL import Image
import pytesseract
import sys

sys.path.append("C:\\Program Files\\Tesseract-OCR")
#image = Image.open("c:\\projects\\pyocr\\pyocr\\test2.jpg")
#image = Image.open("c:\\projects\\pyocr\\pyocr\\test3.png")
#image = Image.open("c:\\projects\\pyocr\\pyocr\\test2.jpg")
#print(pytesseract.image_to_string(image))


image = Image.open("c:\\projects\\pyocr\\pyocr\\test2.jpg")
#(a, b, c, d)
#upper left, lower right
cropsection =  (455, 340, 545, 370)
croppedimage = image.crop(cropsection)
croppedimage.save("c:\\projects\\pyocr\\pyocr\\test22.jpg")
croppedimage.show()

image2 = Image.open("c:\\projects\\pyocr\\pyocr\\test22.jpg")
print(pytesseract.image_to_string(image2))
