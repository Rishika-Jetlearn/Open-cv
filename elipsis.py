import cv2
import numpy as np

im=cv2.imread("circles.jpg",cv2.IMREAD_COLOR)
cv2.imshow("im",im)
cv2.waitKey(0)


blob=cv2.SimpleBlobDetector_Params()
blob.filterByArea=True
blob.minArea=100

blob.filterByCircularity=True
blob.minCircularity=0.2

blob.filterByConvexity=True
blob.minConvexity=0.5

blob.filterByInertia=True
blob.minInertiaRatio=0.1

detector=cv2.SimpleBlobDetector_create(blob)


kp=detector.detect(im)
print(kp)
count=str(len(kp))


draw=cv2.drawKeypoints(im,kp,np.zeros((1,1)),(0, 250, 233),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.putText(draw,count,(70,500),3,9,(25,40,239))
cv2.imshow("im",draw)
cv2.waitKey(0)