import easyocr
import cv2
import numpy as np
from PIL import Image

file = open("datasuhu.txt","w") #Opening datasuhu.txt
filename="Dataset/dataset (13).jpg" #dataset
image=Image.open(filename)

for x in range (image.size[0]):
    for y in range (image.size[1]):
        r, g, b=image.getpixel((x,y))
        image.putpixel((x,y),(0,g,b)) #0 Red

try:
    reader=easyocr.Reader(['en']) #Bahasa eng
    result=(reader.readtext(image))
    fixresult=(result[2][1]) #Spesific the result temperature
    file.write(fixresult[-4:]) #Index 3 angka dari belakang
    file.close() #Close datasuhu.txt
except:
    file.write("ERROR") 
    file.close() #Close datasuhu.txt