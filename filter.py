from tkinter import*
import cv2
image=cv2.imread("C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\Pokemon.png",cv2.IMREAD_COLOR)
cv2.imshow("image",image)

def grey():
    cv2.destroyAllWindows()
    grey=cv2.imread("C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\Pokemon.png",cv2.IMREAD_GRAYSCALE)
    cv2.imshow("greyscale",grey)
    print(grey)
    cv2.waitKey(1000)

def black():
    cv2.destroyAllWindows()
    b,g,r=cv2.split(image)
    print(b)
    cv2.imshow("black",b)
    cv2.waitKey(1000)


window=Tk()

#buttons
greyim=Button(text="grey",padx=10,command=grey)
greyim.grid(row=1,column=1)

blackim=Button(text="black",padx=20,command=black)
blackim.grid(row=1,column=2)




window.mainloop()