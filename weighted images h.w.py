import cv2
from tkinter import*
import numpy as np

def weight_image():

    entl=float(landscape.get())
    ents=float(snow.get())

    weighted=cv2.addWeighted(image,entl,image2,ents,0)
    cv2.imshow("Weighted",weighted)
    cv2.waitKey(0)

image=cv2.imread("landscape.jpg",cv2.IMREAD_COLOR)
image2=cv2.imread("snow.jpg",cv2.IMREAD_COLOR)


window=Tk()

#entrys
snow=Entry()
snow.pack()

landscape=Entry()
landscape.pack()

#button
go=Button(window,command=weight_image,text="go")
go.pack()

window.mainloop()