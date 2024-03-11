import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/aishanya/Desktop/projects/opencv/download1.jpeg')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blank = np.zeros (img.shape[:2] , dtype = 'uint8')

cv.imshow('gray' , gray)
mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2),50 , 255 , -1)

masked_img = cv.bitwise_and(gray, gray, mask  = mask)

gray_hist = cv.calcHist([gray] , [0] , masked_img , [256] , [0,256])
plt.title('histogram_plot')
plt.xlabel('bins')
plt.ylabel('# of pixels')

plt.plot(gray_hist)
plt.show()
cv.waitKey(0)