import cv2 as cv
import numpy as np

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download.jpeg')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
# canny = cv.Canny(blur , 125 ,175 )
# contours , hierarchy = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)# here 'contours'  is the list of the contour coordinates and hierachies is the list of hierarchial representation
# #cv.imshow('contours' , contours)
# print(len(contours))
# print(len(hierarchy))

ret ,  thresh = cv.threshold(gray, 125 , 125 , cv.THRESH_BINARY)
cv.imshow('threshold' , thresh)
print(ret) #ret contains number of contour points in the image


cv.waitKey(0)