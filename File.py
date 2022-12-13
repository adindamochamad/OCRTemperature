import easyocr
import cv2
import glob
import os
import numpy as np
from PIL import Image

#Input Folder Terbaru
bacafolder=glob.glob('D:\File APKM ITTS\Dataset\*')
folderterbaru=max(bacafolder, key=os.path.getctime)

#Input File Terbaru
folder=(folderterbaru + "\*")
bacafile=glob.glob(folder)
fileterbaru=max(bacafile, key=os.path.getctime)

file = open("datasuhu.txt","w") #Opening datasuhu.txt
filename= fileterbaru #dataset
image=Image.open(filename)