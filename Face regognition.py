import cv2
import os
main_folder="faces"

print(list(os.walk(main_folder)))

images=[]
labels=[]
names={}

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