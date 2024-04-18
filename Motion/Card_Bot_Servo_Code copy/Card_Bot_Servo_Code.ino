import time
from adafruit_servokit import ServoKit
myKit = ServoKit(channels = 16)
myKit.servo[0].angle=180
while True:
    for i in range(0, 180):
        myKit.servo[0].angle = i
        time.sleep(.01)
        print(i)
    for i in range(180, 0, -1):
        myKit.servo[0].angle = i
        time.sleep(.01)
        print(i)
    break
