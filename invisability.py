import cv2
import numpy as np

"""blue=np.uint8([[[255,0,0]]])
hsvblue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
print(hsvblue)"""

vid=cv2.VideoCapture("video.mp4")

for i in range(60):
    s,bg=vid.read()
    if s is False:
        continue

"""cv2.imshow("vid",bg)
cv2.waitKey(0)"""

lb=np.array([155,40,40])
ub=np.array([180,255,255])

while vid.isOpened():
    s,f=vid.read()
    if s is False:
        break

    frame=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    mask1=cv2.inRange(frame,lb,ub)
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3)))
    mask2=cv2.bitwise_not(mask1)

    r1=cv2.bitwise_and(bg,bg,mask=mask1)
    r2=cv2.bitwise_and(frame,frame,mask=mask2)
    output=cv2.add(r1,r2)
    cv2.imshow("output",output)
    cv2.waitKey(10)

