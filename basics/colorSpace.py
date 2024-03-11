import cv2 as cv
import numpy as np

img  = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')
#bgr to gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)
#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
#bgr to lab
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)
cv.waitKey(0)