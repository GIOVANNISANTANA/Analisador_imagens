import pytesseract
import numpy as np
import cv2
import re
#importando bibliotecas


img = cv2.imread('image.png')
#cv2_imshow(img)

def theshold(img):
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return img

h, w, c = img.shape

boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    b = b.split(" ")
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

texto = pytesseract.image_to_string(img)
print(texto)
