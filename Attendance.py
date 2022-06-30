import cv2
import numpy as np
import face_recognition
import os

path = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in mylist:
	curImg = cv2.imread(f'{path}/{cl}')
	images.append(curImg)
	classNames.append()

imgElon = face_recognition.load_image_file('ImageBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)