import cv2
from tkinter import*
window=Tk()
window.geometry("200x100")
window.title("Number guessing game")
window. configure(bg="#afedd3")

def write():
    user.delete(0,END)
    word=user.get()
    cv2.putText(image,word,(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(20,40,144),3)
    cv2.imshow("im",image)
cv2.waitKey(0)
#labels
lab=Label(window,text="Text:  ")
lab.grid(row=1,column=1)

#Entry
user=Entry(window)
user.grid(row=1,column=2)

#button
go=Button(window,text="go",background="black",foreground="green",width=3,height=1,command=write)
go.grid(row=2,column=2)

#image
image=cv2.imread("landscape.jpg",cv2.IMREAD_COLOR)

cv2.rectangle(image, (150, 200), (350, 400), (150, 75, 0), -1)  

# Draw the roof (rectangle)
cv2.rectangle(image, (125, 150), (375, 200), (0, 0, 255), -1)  

# Draw the door (rectangle)
cv2.rectangle(image, (230, 300), (270, 400), (50, 50, 150), -1) 

# Show the image
cv2.imshow("House", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#drawing a line

cv2.line(image,(125,150),(258,117),(200,15,124),50)
cv2.imshow("image",image)
cv2.waitKey(0)

cv2.line(image,(258,117),(125,150),(200,15,124),50)
cv2.imshow("image",image)
cv2.waitKey(0)






window.mainloop()
