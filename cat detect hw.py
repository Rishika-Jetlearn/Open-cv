import cv2


xml=r"C:\Users\Freze\Jetlearn Python projects-Rishika\Open cv\Open-cv\cat xml.xml"
classifier=cv2.CascadeClassifier(xml)
vid="catvideo.mp4"
video=cv2.VideoCapture(vid)
while video.isOpened():
    b,f=video.read()
    f=cv2.resize(f,(1000,800))
    if b==False:
        continue
    grey=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    list_cats=classifier.detectMultiScale(grey,1.3,10)
    for x,y,w,h in list_cats:
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("cat",f)
    cv2.waitKey(1000)
