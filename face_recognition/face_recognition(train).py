import os
import numpy as np
import cv2 as cv

people = ['Nick', 'robert', 'joe']
#p = []
# for i in os.listdir(r'/home/aishanya/Desktop/projects/opencv/models/face_recognition/people'):
#     p.append(i)
    
# print(p)

# our  training set consists of features and their respective labels
features = []
labels=  []
DIR = r'/home/aishanya/Desktop/projects/opencv/models/face_recognition/people'
haar_cascade = cv.CascadeClassifier('haarcascade.xml') #reading the classifier file


def create_train():
    for i in people: #iterating inside folder
        path = os.path.join(DIR, i)
        label = people.index(i)
        #iterating imges in folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img ) #joining the  image wth the apth
            
            img_array = cv.imread(img_path)#converting img to array then grayscaling
            gray = cv.cvtColor(img_array , cv.COLOR_BGR2GRAY)
            
            face_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 4)
            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print("training done ---")
# print("length of featurs : " , len(features))
# print("length of labels : " , len(labels))   

#instantiate our face_recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
            #train the recognizer on features and labels
features = np.array(features , dtype='object')
labels = np.array(labels)

face_recognizer.train(features , labels)
face_recognizer.save('face_trainedl.yml')
np.save('features.npy' , features)    
np.save('labels.npy' , labels)    

        