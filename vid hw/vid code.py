import cv2
import os
from PIL import Image
path="C:\\Users\\Freze\\Jetlearn Python projects-Rishika\\Open cv\\Open-cv\\vid hw"

os.chdir(path)
no_of_im=0
total_height=0
total_width=0

#resize
for file in os.listdir(path):
    if file.endswith(".jpg")or file.endswith(".png")or file.endswith(".jpeg"):
        im=Image.open(os.path.join(path,file))
        w,h=im.size
        total_width=w+total_width
        total_height=h+total_height
        no_of_im=no_of_im + 1

mean_width= total_width//no_of_im
mean_height= total_height//no_of_im
print(mean_width,mean_height)

videoname="edit.avi"
vi=cv2.VideoWriter(videoname,0,0.5,(mean_width,mean_height))


for file in os.listdir(path):
    if file.endswith(".jpg")or file.endswith(".png")or file.endswith(".jpeg"):
        image=cv2.imread(os.path.join(path,file),cv2.IMREAD_COLOR)
        a=cv2.resize(image,(mean_width,mean_height))
        text=cv2.putText(a,"Birthday edit",(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(250,3,20),2)
        vi.write(text)

