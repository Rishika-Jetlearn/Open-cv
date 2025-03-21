import cv2
import numpy as np
image=cv2.imread("packman.png",cv2.IMREAD_COLOR)
cv2.imshow("im",image)
cv2.waitKey(0)


grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.medianBlur(grey,7)#blurring
detected=cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,1,10,param1=60,param2=30,minRadius=5,maxRadius=45)
print(detected)

if detected is not None:
    detected=np.uint(np.around(detected))
    print(detected)
    for x,y,r in detected[0]:
        print(x,y,r) 
        cv2.circle(image,(x,y),r,(255,0,0),2)
        cv2.imshow("im",image)
        cv2.waitKey(0)