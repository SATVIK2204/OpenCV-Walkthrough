import cv2 as cv

"""  VideoCapture takes either path of the video file as its argument or interger like 0,1,2.. with corresponds
     to the webcam or any other camera connected to your system"""
capture=cv.VideoCapture('./videos/second.mp4')

""" We read a video frame by frame so we are using a loop and while its True and there is a frame in our video it shows it"""

while True:
    isTrue,frame=capture.read()

    cv.imshow("Spongebob",frame)

    """Here window wait for 20ms for the next frame and if the key D is pressed or not. Changing the waitkey will 
       slow down or speed up the video"""
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

