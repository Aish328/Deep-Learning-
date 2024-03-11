import numpy as np
import cv2 as cv

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download1.jpeg')
blank = np.zeros (img.shape[:2] , dtype = 'uint8')

cv.imshow('main' , img)
cv.imshow('blank',blank)
 #creating a mask
mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2),50 , 255 , -1)
cv.imshow('mask' , mask)

masked_img = cv.bitwise_and(img, img, mask  = mask)
cv.imshow('masked img' , masked_img)



cv.waitKey(0)