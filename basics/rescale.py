import cv2 as cv

capture = cv.VideoCapture('/home/aishanya/Downloads/video_of_funny_cat (1080p).mp4')
#will work for imagrs, videos and live video
def rescale(frame , scale = 0.25):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dim = (width ,  height)
    resized_frame = cv.resize(frame , dim , interpolation = cv.INTER_AREA)
    return resized_frame
    


while True:
    isTrue , frame = capture.read()
    
    resized_img = rescale(frame)
    
    #cv.imshow('Video',frame)
    cv.imshow('resized', resized_img)

    if cv.waitKey (20) & 0xFF == ord('d'):
        break
capture.release()
cv.DestroyAllWindows()
#img = cv.imread('/home/aishanya/Pictures/Screenshot from 2024-02-07 22-53-32.png')
#cv.imshow('Screenshot',img)
# print("Aish")
# cv.waitKey(0)/home/aishanya/Downloads/