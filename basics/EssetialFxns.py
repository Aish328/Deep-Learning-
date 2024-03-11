import cv2 as cv
import numpy

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')
#cv.imshow('img' , img)
#converting img to grayscale
gray  = cv.cvtColor(img , cv.COLOR_BGR2GRAY )
cv.imshow('gray' , gray)
#blurring img
blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT) 
                            #kernel size
cv.imshow('blurred img' , blur)

#edge cascading of the image
canny = cv.Canny(blur , 125 , 175)
cv.imshow('canny' , canny)

#dilating an image
dilated = cv.dilate(canny , (7,7) , iterations = 7)
cv.imshow('dilated' , dilated)

#eroding the dilated image back to thestructured image
eroded = cv.erode(dilated , (3,3) , iterations = 3)
cv.imshow('eroded' , eroded)

#resizng an image
resized = cv.resize(img,(500,200),interpolation = cv.INTER_CUBIC)
cv.imshow('resized' , resized)
 
#cropping
cropped = img[50:200 , 200:500]
cv.imshow('cropped', cropped)

cv.waitKey(0)
cv.DestroyAllWindows()