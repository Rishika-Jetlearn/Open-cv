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
a=cv2.CascadeClassifier(xml)
vid=cv2.VideoCapture(0)
pic_count=0
while pic_count<30:
    

