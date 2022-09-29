# Table Of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
## Hello_CircuitPython:
### Description
The assignment is teaching the student the basics of how to use a servo with interval degrees
### Code
```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import neopixel
import board
import pwmio
from adafruit_motor import servo
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)
BUTTON = 1
Kaz.brightness = 1
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
  for angle in range(0, 180, 180):  # 0 - 180 degrees, 100 degrees at a time.
        my_servo.angle = angle
  for angle in range(180, 0, -180): # 180 - 0 degrees, 100 degrees at a time.
        my_servo.angle = angle
```
### Evidence:
#### Funcioning Video
![Servo_Spinning](https://user-images.githubusercontent.com/91289762/192614293-b1612daf-d5ca-4ed8-9b4c-d0f26612e901.gif)
#### Wiring Diagram
![Wiring Of Servo](https://user-images.githubusercontent.com/91289762/192615571-1d0a45ed-eb88-417b-8a5a-f431c68ef31d.png)
### Reflection
When I tried to add the degree intervals at the end of the "angle in range" statement I forgot to add a delay time and that blew the servo, I also made the degree over 180 and that confused the code. When I forgot to add delay the servo spasmed left and right very fast thats then screwed the glue, or stripped a gear and stopped the servo, it also sparked. When I made the intervol too large the code said that there was an error, so nothing broke. I learned that when your servo groggles and sparks then you've done something wrong.
