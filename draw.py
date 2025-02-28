import cv2

image=cv2.imread("landscape.jpg",cv2.IMREAD_COLOR)
cv2.imshow("image",image)
cv2.waitKey(0)

#drawing a line
cv2.line(image,(0,0),(50,63),(200,15,124),4)
cv2.imshow("image",image)
cv2.waitKey(0)

#drawing a rectangle
cv2.rectangle(image,(5,1),(150,70),(7,140,255),8)
cv2.imshow("image",image)
cv2.waitKey(0)

#filled rectangle
cv2.rectangle(image,(100,100),(230,170),(7,140,255),-1)
cv2.imshow("image",image)
cv2.waitKey(0)
#drawing a circle
cv2.circle(image,(300,50),50,(181,176,254),10)
cv2.imshow("image",image)
cv2.waitKey(0)

#drawing a filled circle
cv2.circle(image,(50,500),50,(181,176,254),-10)
cv2.imshow("image",image)
cv2.waitKey(0)

#add text
cv2.putText(image,"Hello",(589,90),cv2.FONT_HERSHEY_SIMPLEX,2,(45,897,255))
cv2.imshow("image",image)
cv2.waitKey(0)

