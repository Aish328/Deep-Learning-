import numpy as np
import cv2 as cv

blank = np.zeros((400,400),dtype = 'uint8')

rectangle = cv.rectangle(blank.copy() , (30,30) ,(370,370) , 255 ,  -1 )
cv.imshow('rectangle' , rectangle)

circle = cv.circle(blank , (200,200) , 200,255 ,-1 )
cv.imshow('circle' , circle)

bitwise_and = cv.bitwise_and(rectangle , circle)
cv.imshow('bitwise and' , bitwise_and)

bitwise_or = cv.bitwise_or(rectangle , circle)
cv.imshow('bitwise_or' , bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle , circle)
cv.imshow('bitwise_xor' , bitwise_xor)

cv.waitKey(0)