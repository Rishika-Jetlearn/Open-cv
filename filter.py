from tkinter import*
window=Tk()

#buttons
edit=Button(text="Edit",padx=10)
edit.grid(row=1,column=1)

delete=Button(text="Delete",padx=20)
delete.grid(row=1,column=2)

save=Button(window,text="Save")
save.grid(row=4,column=1,pady=30,padx=40)



window.mainloop()
