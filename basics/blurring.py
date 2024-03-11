import numpy as np
import cv2 as cv

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')
cv.imshow('main' , img)
average = cv.blur(img , (3,3)) #averaging
cv.imshow('average' , average)
#median blur
median = cv.medianBlur(img , 3)
cv.imshow('medan' , median)
#bilateral blur
bilateral = cv.bilateralFilter(img, 5 , 15 ,  15)
cv.imshow('bilateral' , bilateral )

cv.waitKey(0)