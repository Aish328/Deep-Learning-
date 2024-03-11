import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haarcascade.xml')
people = ['Nick', 'robert', 'joe']
# features = np.load('features.npy')
# labels = np.load('labels.npy')
#instantiate the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trainedl.yml')
img  = cv.imread('/home/aishanya/Desktop/projects/opencv/models/face_recognition/people/Nick/2.jpeg')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)
cv.imshow('person' , gray)
#detecting face
face_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 4)

#to drwa box around face
for (x , y, w, h) in face_rect:
    face_roi = gray[y:y+h , x:x+h]
    
    labels , confidence  = face_recognizer.predict(face_roi)
    print("label : " , labels)
    print("confidence", confidence)
    
    cv.putText(img , str(people[labels]),(20,20), cv.FONT_HERSHEY_COMPLEX , 1.0 , (0,255,0), thickness = 2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness = 2)
    
cv.imshow('detected'  , img)
cv.waitKey(0)