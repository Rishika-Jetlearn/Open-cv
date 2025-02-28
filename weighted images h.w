import cv2
from tkinter import*
import numpy as np

def weight_image():

    landscape.get() 

def weight_image2():

    snow.get()

image=cv2.imread("landscape.jpg",cv2.IMREAD_COLOR)
image2=cv2.imread("snow.jpg",cv2.IMREAD_COLOR)


window=Tk()

#buttons
snow=Entry()
snow.pack()

landscape=Entry()
landscape.pack()


#weighted image
weighted=cv2.addWeighted(image,weight_image(),image2,weight_image2(),0)
cv2.imshow("Weighted",weighted)
cv2.waitKey(0)

cv2.destroyAllWindows()
