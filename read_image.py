import cv2 as cv

# imread function takes image path as input
img= cv.imread('images/fourth.jpeg')

# creates a output window with title as given.
cv.imshow("Spongebob",img)

cv.waitKey(0)
"""waitkey specifies time the window will wait for next frame. 0 means it will wait for infinite time. We used 0 as we have only 
  one frame and we don't want our window to fall in error that it can't find a new frame"""