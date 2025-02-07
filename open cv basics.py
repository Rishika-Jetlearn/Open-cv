import cv2
image=cv2.imread("C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\Pokemon.png",cv2.IMREAD_COLOR)
cv2.imshow("image",image)
print(image)

#colour
k=cv2.waitKey(0)
cv2.destroyAllWindows()#revoing window first,then displaying
print(k)#what key is pressed

#grey
grey=cv2.imread("C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\Pokemon.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("greyscale",grey)
print(grey)
cv2.waitKey(0)

#saving the grey
save=cv2.imwrite("C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\GREY.png",grey)
print(save)

#split
b,g,r=cv2.split(image)
print(b)
cv2.imshow("blue",b)
cv2.waitKey(0)

cv2.imshow("red",r)
cv2.waitKey(0)

cv2.imshow("green",g)
cv2.waitKey(0)
