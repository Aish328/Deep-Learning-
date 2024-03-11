import numpy as np
import cv2 as cv

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')
cv.imshow('main img' , img)
#splitting image into channels
# b,g,r = cv.split(img)
# cv.imshow('blue' , b)
# cv.imshow('green' , g)
# cv.imshow('red' , r) 

blank  = np.zeros(img.shape[:2] , dtype = 'uint8')
b,g,r  = cv.split(img)
blue = cv.merge([b,blank, blank])
green = cv.merge([blank,g, blank])
red = cv.merge([blank,blank, r])

cv.imshow('blue' , blue)
cv.imshow('green' , green)
cv.imshow('red' , red)


 

cv.waitKey(0)