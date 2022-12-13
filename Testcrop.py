import cv2
import matplotlib.pyplot as plt
import easyocr

img = cv2.imread("Dataset\datasetsuhu (25).jpg")
cropped = img[65:1200,0:1920]

reader=easyocr.Reader(['en'], gpu=True) #English
result=(reader.readtext(cropped))
result1=result[0][1]
print(result1[-4:])