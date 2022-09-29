import cv2
import numpy as np


Fire_Reported = 0

video = cv2.VideoCapture('video2.mp4') # If you want to use webcam use Index like 0,1.

while True:
    success, img = video.read()      # success here is a boolean(image shown or not)
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    frame = cv2.resize(frame, (960, 540))

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)

    no_red = cv2.countNonZero(mask)

    # this paramter can be set
    if int(no_red) > 2500:
        Fire_Reported = Fire_Reported + 1

    # print(no_red)
    cv2.imshow("output", output)

    if Fire_Reported >= 1:
        print('Fire detected')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
video.release()
