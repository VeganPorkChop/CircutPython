import servo
import math
import time

myServo = 3
servoMove = 1000
servoSecondMove = 50000

while True:
    myServo.angle = 1090
    time.sleep(1)
    myServo.angle = 50000
    time.sleep(1)
    print("qowid")