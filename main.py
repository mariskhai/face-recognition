import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('ImageBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

scale_percent = 50
width = int(imgElon.shape[1] * scale_percent / 100)
height = int(imgElon.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(imgElon, dim, interpolation=cv2.INTER_AREA)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(resizedTest)[0]
encodeTest = face_recognition.face_encodings(resizedTest)[0]
cv2.rectangle(resizedTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(resized, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)