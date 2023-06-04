import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe' # File path

image = Image.open('images.png')  # The picture from which the text is taken

text = pytesseract.image_to_string(image, lang='eng')   # in "lang", select the language in which the text in the photo is

print(f'TEXT FROM THE IMAGE: {text}')
