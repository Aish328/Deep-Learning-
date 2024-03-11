import cv2 as cv
import numpy as np

#creating blank images
blank = np.zeros((500,500,3),dtype = 'uint8')
cv.imshow('blank',blank)

#. paint image:
blank[:] = 0,0,255 # BGR format to color wntire black image as  green
#area selective paintin
blank[200:300 , 300:400] = 0,255,0
cv.imshow('green' , blank)

# draw a rectangle on blank
cv.rectangle(blank,(0,0),(250,125),(0,255,0),thickness = 2)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness = -1)

cv.imshow('rect',blank)

#filling in rectange 
cv.rectangle(blank,(0,0),(250,125),(0,255,0),thickness = cv.FILLED)
#or cv.rectangle(blank,(0,0),(250,125),(0,255,0),thickness = -1)
 
cv.imshow('rect',blank)

cv.waitKey(0)