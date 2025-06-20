import cv2
import os
import numpy as np
main_folder="faces"
xml="haarcascade_frontalface_default.xml"
print(list(os.walk(main_folder)))

images=[]
labels=[]
names={}

width=100
height=120
identifier=0
for root,subfolders,files in os.walk(main_folder):
    for subfolder in subfolders:
        names[identifier]=subfolder
        path=os.path.join(main_folder,subfolder)
        for file in os.listdir(path):
            imagepath=os.path.join(path,file)
            image=cv2.imread(imagepath,cv2.IMREAD_GRAYSCALE)
            images.append(image)
            labels.append(identifier)
        identifier=identifier+1
print(names)
print(labels)
images=np.array(images)
labels=np.array(labels)

model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)

vid=cv2.VideoCapture(0)
classifier=cv2.CascadeClassifier(xml)
while True:
    b,f=vid.read()
    if not b:
        continue
    grey=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    list_faces=classifier.detectMultiScale(grey,1.2,4 )
    for x,y,w,h in list_faces:
        face=grey[y:y+h,x:x+w]
        resized=cv2.resize(face,(width,height))
        detect=model.predict(resized)
        print(names[detect[0]])
        cv2.putText(f,names[detect[0]],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
        print(detect)
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("im",f)
    waitkey=cv2.waitKey(1000)
    if waitkey==27:
        break
