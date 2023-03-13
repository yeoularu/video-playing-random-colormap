import random
import cv2 as cv

# for webcam(s), 0(, 1, 2, ...). for video file, file path.
video_source = 0

video = cv.VideoCapture(video_source)

if video.isOpened():
    colorMap = random.randint(0, 21)
    while True:
        valid, img = video.read()
        if not valid:
            break

        info = f'Press Space Key'
        cv.putText(img, info, (10, 25),
                   cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
        dst = cv.applyColorMap(img, colormap=colorMap)
        cv.imshow('Video Player', dst)

        key = cv.waitKey(1)
        if key == ord(' '):
            colorMap = random.randint(0, 21)
        if key == 27:  # ESC
            break

    cv.destroyAllWindows()
