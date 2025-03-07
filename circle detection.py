import cv2
image=cv2.imread("eyes.jpg",cv2.IMREAD_COLOR)
cv2.imshow("im",image)
cv2.waitKey(0)

#technique 1
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.medianBlur(grey,7)#blurring
detected=cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,1,10,param1=60,param2=30,minRadius=20,maxRadius=45)
print(detected)
