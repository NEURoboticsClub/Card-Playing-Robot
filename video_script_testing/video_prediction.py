import numpy as np
from roboflow import Roboflow
from dotenv import dotenv_values
import cv2
import sys


config = dotenv_values('../.env')

rf = Roboflow(api_key=config['API_KEY'])
project = rf.workspace().project('playing-cards-ow27d')
model = project.version(4).model

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
    cv2.imwrite('temp.jpg', frame)

    pred = model.predict('temp.jpg', confidence=40, overlap=30).json()
    if pred['predictions']:
        print(pred['predictions'][0]['class'])
    else:
        print('No card found...')

    # this works but the api calls are too slow, need to either 
    # figure out a way to run the model locally or use a different method

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()