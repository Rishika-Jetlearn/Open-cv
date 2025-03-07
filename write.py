import cv2
from tkinter import*
window=Tk()
window.geometry("200x100")
window.title("Number guessing game")
window. configure(bg="#afedd3")

def write():
    word=user.get()
    user.delete(0,END)
    cv2.putText(image,word,(250,500),cv2.FONT_HERSHEY_COMPLEX,2,(20,40,144),3)

    #BODY
    cv2.rectangle(image, (150, 200), (350, 400), (150, 75, 0), -1)

    #ROOF
    cv2.rectangle(image, (125, 150), (375, 400), (0, 0, 255), -1)  

    # Draw the door (rectangle)
    cv2.rectangle(image, (230, 300), (270, 400), (50, 50, 150), -1) 


    #drawing a line

    cv2.line(image,(125,150),(250,117),(200,15,124),50)
    

    cv2.line(image,(250,117),(375,150),(200,15,124),50)
    

    # Show the image
    cv2.imshow("House", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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


window.mainloop()