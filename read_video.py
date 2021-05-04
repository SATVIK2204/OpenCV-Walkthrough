import cv2 as cv


def rescale(frame,scale=0.75):

    """Scaling the height and width with same factor to maintain the aspect ratio
       Also typecasting the width and height to intgers as cv.resize() takes int parameters, not float"""

    width= int((frame.shape[1])*scale)
    height=int((frame.shape[0])*scale)

    dimensions=(width,height)
    resized_frame=cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

    """Interpolation is the way in which the image is upscaled or down scaled. We are using cv.INTER_AREA as
       it is fast and optimal for frame decimation.
       I would recommed this blog for better intution :-
       https://medium.com/@wenrudong/what-is-opencvs-inter-area-actually-doing-282a626a09b3
       """
    return resized_frame




"""  VideoCapture takes either path of the video file as its argument or interger like 0,1,2.. with corresponds
     to the webcam or any other camera connected to your system"""
capture=cv.VideoCapture('./videos/second.mp4')


""" We read a video frame by frame so we are using a loop and while its True and there is a frame in our video it shows it"""

while True:
    isTrue,frame=capture.read()

    cv.imshow("Spongebob",frame)
    cv.imshow("Spongebob Rescaled",rescale(frame))

    """Here window wait for 20ms for the next frame and if the key D is pressed or not. Changing the waitkey will 
       slow down or speed up the video"""
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

