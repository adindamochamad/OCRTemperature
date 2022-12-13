import easyocr
import cv2
import glob
import os
import numpy as np
from PIL import Image

#Input Folder Terbaru
bacafolder=glob.glob('D:\File APKM ITTS\Dataset\*')
file=max(bacafolder, key=os.path.getctime)
img=cv2.imread(file)
imgcropped=img[65:1200,0:1920]

reader=easyocr.Reader(['en'], gpu=True) #English
result=(reader.readtext(imgcropped))
fix=result[0][1]

file = open("datasuhu.txt","w") #Opening datasuhu.txt
try:
    file.write(fix[-4:])
    file.close()
    print("Done")
except:
    file.write("ERROR")
    file.close() #Close datasuhu.txt
    print("Error")