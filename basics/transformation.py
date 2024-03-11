import numpy as np
import cv2 as cv

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')
def translate(img , x , y ):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)

translated = translate(img , 50, 100)
cv.imshow('translated' , translated)
# +x --> right , +y --> down , -x --> left , -y --> up

def rotate(img, angle , rotPoint = None):
    (height , width) = img.shape[:2]
    if rotPoint is  None:
        rotPoint = (height//2 , width //2)
    #DEFINING ROTATION MATRIX
    rotMat = cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dimensions = (height , width)
    
    return cv.warpAffine(img , rotMat , dimensions)

rotated = rotate(img , 50 )
cv.imshow('rotated' , rotated)
cv.waitKey(0)