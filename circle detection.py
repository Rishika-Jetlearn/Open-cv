import cv2
import numpy as np
image=cv2.imread("eyes.jpg",cv2.IMREAD_COLOR)
cv2.imshow("im",image)
cv2.waitKey(0)

#technique 1
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.medianBlur(grey,7)#blurring
detected=cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,1,10,param1=60,param2=30,minRadius=20,maxRadius=35)
print(detected)

if detected is not None:
    detected=np.uint(np.around(detected))
    print(detected)
    for x,y,r in detected[0]:
        print(x,y,r) 
        cv2.circle(image,(x,y),r,(23,44,255),2)
        cv2.imshow("im",image)
        cv2.waitKey(0)

#technique 2
im=cv2.imread("circles.jpg",cv2.IMREAD_COLOR)
cv2.imshow("im",im)
cv2.waitKey(0)


blob=cv2.SimpleBlobDetector_Params()
blob.filterByArea=True
blob.minArea=100

blob.filterByCircularity=True
blob.minCircularity=0.9

blob.filterByConvexity=True
blob.minConvexity=0.9

blob.filterByInertia=True
blob.minInertiaRatio=0.6

detector=cv2.SimpleBlobDetector_create(blob)


kp=detector.detect(im)
print(kp)
count=str(len(kp))


draw=cv2.drawKeypoints(im,kp,np.zeros((1,1)),(0, 250, 233),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.putText(draw,count,(70,500),3,9,(25,40,239))
cv2.imshow("im",draw)
cv2.waitKey(0)