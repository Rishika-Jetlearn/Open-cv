import cv2
image=cv2.imread("Pokemon.png",cv2.IMREAD_COLOR)

#border
bordered=cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=(155,140,32))
cv2.imshow("Bordered",bordered)
cv2.waitKey(0)

bordered=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_REFLECT)
cv2.imshow("Bordered",bordered)
cv2.waitKey(0)


#greyscale
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey",grey)
cv2.waitKey(0)

#rotating
r,c=image.shape[0:2]
rotated=cv2.getRotationMatrix2D((c/2,r/2),90,1)
ro=cv2.warpAffine(image,rotated,(r,c))
cv2.imshow("Rotation",ro)
cv2.waitKey(0)

cv2.destroyAllWindows()

#edge detection
ed=cv2.Canny(image,125,250)
cv2.imshow("ed",ed)
cv2.waitKey(0) 

cv2.destroyAllWindows()

#blurring
gb=cv2.GaussianBlur(image,(71,71),0)
cv2.imshow("gb",gb)
cv2.waitKey(0)

#median blur
mb=cv2.medianBlur(image,9)
cv2.imshow("mb",mb)
cv2.waitKey(0)

cv2.destroyAllWindows()