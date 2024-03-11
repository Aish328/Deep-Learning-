import numpy as np
import cv2 as  cv
import matplotlib.pyplot as plt

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download1.jpeg')
cv.imshow('main' , img)

colors = ('b', 'g' , 'r')
for i , cols in enumerate(colors):
    hist = cv.calcHist([img] , [i] , None , [255] , [0,256])
    plt.plot(hist)
plt.show()



cv.waitKey(0)