import easyocr
import cv2
import glob
import os
import numpy as np
from PIL import Image

#Input Folder Terbaru
bacafolder=glob.glob('D:\File APKM ITTS\Dataset\*')
fileterbaru=max(bacafolder, key=os.path.getctime)
print(fileterbaru)
image=Image.open(fileterbaru)

for x in range (image.size[0]):
    for y in range (image.size[1]):
        r, g, b=image.getpixel((x,y))
        image.putpixel((x,y),(0,g,b)) #0 Red

reader=easyocr.Reader(['en'], gpu=True) #English
result=(reader.readtext(image))
file = open("datasuhu.txt","w") #Opening datasuhu.txt

try:
    fixresult=(result[2][1]) #Spesific the result temperature
    file.write(fixresult[-4:]) #Show index 3 angka dari belakang
    file.close() #Close datasuhu.txt
    print("Done")
except:
    file.write("ERROR")
    file.close() #Close datasuhu.txt
    print("Error")