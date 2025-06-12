import cv2

xml=
classifier=cv2.CascadeClassifier(xml)
vid_file=""
video=cv2.VideoCapture(vid_file)
while video.isOpened():
    b,f=video.read()
    if b==False:
        continue
    grey_vid=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    list_cats=classifier.detectMultiScale(grey,1.3,10)
    for x,y,w,h in list_vehicles:
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("vehicle detection",f)
    cv2.waitKey(1000)
