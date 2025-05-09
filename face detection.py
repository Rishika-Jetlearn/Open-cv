import cv2
import os
main_folder="faces"
sub_folder="Rishika"
path=os.path.join(main_folder,sub_folder)
if not os.path.isdir(path):
    os.makedirs(path)
    print("path done")

height=120
width=100
xml="haarcascade_frontalface_default.xml"
classifier=cv2.CascadeClassifier(xml)
vid=cv2.VideoCapture(0)
pic_count=0

while pic_count<30:
    b,f=vid.read()
    if b==False:
        continue

    grey=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    list_faces=classifier.detectMultiScale(grey,1.2,4)
    print(list_faces)
    for x,y,w,h, in list_faces:
        cv2.rectangle(f,(x,y),(x+w,y+h),(55,43,17),3)
        face=grey[y:y+h,x:x+w]
        resized=cv2.resize(face,(width,height))
        cv2.imwrite(f"{path}/{pic_count}.png",resized)
        pic_count=pic_count+1
    cv2.imshow("Camera",f)
    wait=cv2.waitKey(1000)
    if wait==27:
        break

