import pytesseract
import cv2
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract.exe'
# hello.png ocr
img = cv2.imread(R'asset\images\_product_image_3547.jpeg')
text = pytesseract.image_to_string((img), lang='eng+kor')
print(text)