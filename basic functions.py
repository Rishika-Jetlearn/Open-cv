import cv2
import numpy as np
image=cv2.imread("landscape.jpg",cv2.IMREAD_COLOR)
image2=cv2.imread("snow.jpg",cv2.IMREAD_COLOR)
pokemon=cv2.imread("Pokemon.png",cv2.IMREAD_COLOR)
#add
addition=cv2.add(image,image2)
cv2.imshow("Added",addition)
cv2.waitKey(0)
cv2.destroyAllWindows()
#weighted image
weighted=cv2.addWeighted(image,0.8,image2,0.3,0)
cv2.imshow("Weighted",weighted)
cv2.waitKey(0)

cv2.destroyAllWindows()
#subtract
subtraction=cv2.subtract(image,image2)
cv2.imshow("subtracted",subtraction)
cv2.waitKey(0)
cv2.destroyAllWindows()
#resize
resize=cv2.resize(image2,(500,400))
cv2.imshow("resize",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
#experiment
adding=cv2.add(subtraction,addition)
cv2.imshow("new",adding)
cv2.waitKey(0)
cv2.destroyAllWindows()
#erosion
kernel=np.ones((10,10))
eroded=cv2.erode(image ,kernel)
cv2.imshow("erode",eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()