import cv2 as cv

# Function to rescale the video/image with the given scaling factor
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
    
# Similar code from read_video.py

# capture= cv.VideoCapture('./videos/second.mp4')

# while True:
#     isTrue,frame=capture.read()

#     # Showing 2 windows to see the difference
#     cv.imshow("Original",frame)
#     cv.imshow("Rescaled",rescale(frame))

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


img= cv.imread('images/first.jpeg')

# creates a output window with title as given.
while True:
    cv.imshow("Spongebob",img)
    cv.waitKey(0)
    cv.imshow("Spongebob",rescale(img))
    cv.waitKey(0)




