import os
from wand.image import Image
 
pdf_file = 'c:/Users/Markos/MyPythonScripts/scanpdf5.pdf'
 
files = []
with(Image(filename=pdf_file, resolution = 500)) as conn: 
    for index, image in enumerate(conn.sequence):
        image_name = os.path.splitext(pdf_file)[0] + str(index + 1) + '.png'
        Image(image).save(filename = image_name)
        files.append(image_name)
        
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

all_text = []
for file in files:
    text = pytesseract.image_to_string(Image.open(file))
    all_text.append(text)
    print(text)


