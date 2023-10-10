import numpy as np
import cv2
import sys


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(frame.shape)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
