import cv2
image=cv2.imread("eyes.jpg",cv2.IMREAD_COLOR)
cv2.imshow("im",image)
cv2.waitKey(0)