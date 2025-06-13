import cv2

xml=r"C:\Users\Freze\Jetlearn Python projects-Rishika\Open cv\Open-cv\cars.xml"
classifier=cv2.CascadeClassifier(xml)
vid_file="video.avi"
video=cv2.VideoCapture(vid_file)
while video.isOpened():
    b,f=video.read()
    if b==False:
        continue
    resized=cv2.resize(f,(1000,800))
    grey_vid=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
    list_vehicles=classifier.detectMultiScale(grey_vid,1.1,5)
    for x,y,w,h in list_vehicles:
        cv2.rectangle(resized,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("vehicle detection",resized)
    cv2.waitKey(10)
