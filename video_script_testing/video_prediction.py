import numpy as np
from roboflow import Roboflow
from dotenv import dotenv_values
import cv2
import sys


config = dotenv_values('.env')

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
    # cv2.imshow('frame', frame)

    pred = model.predict(frame, confidence=40, overlap=30).json()
    if pred['predictions']:
        # print(pred['predictions'][0]['class'])
        # print('pred', pred)

        for idx, p in enumerate(pred['predictions']):

            x = int(pred['predictions'][idx]["x"])
            y = int(pred['predictions'][idx]["y"])
            width = int(pred['predictions'][idx]["width"])
            height = int(pred['predictions'][idx]["height"])

            # print("x", x)print(pred['predictions'][0]['class']
            # print("y", y)
            # print("width", width)
            # print("height", height)
            
            # img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

            # cv2.rectangle(img_array, (x, y), (x + width, y + height), (0, 255, 0), 2)
        
            print("prediction", pred['predictions'][idx]['class'], (x, y))
        # cv2.imshow('image', img_array)
    else:
        print('No card found...')

    # this works but the api calls are too slow, need to either 
    # figure out a way to run the model locally or use a different method

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

### Next steps:
# -- speed up API calls - maybe by training own model?
# -- more accurate bounding boxes
# -- detect multiple cards in a frame - DONE