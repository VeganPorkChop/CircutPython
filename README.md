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
### To commit from VS Code:
1. Go to the little branch icon in the left bar of VS Code.
2. Click the + icon next  to the files you want to commit.
3. Write a message that descibes your changes in the "Message" box and hit commit.
4. If you get an error about user.name and user.email, see the next section.
5. Click the "Sync changes" button.
### If you get an error about user.name and user.email
1. In VS Code, hit `` Ctrl+Shift+` ``
2. Filling in your actual information, run the following commands one line at a time. The paste shortcut is `Ctrl+V` or you can right click then hit paste. Spelling must match exactly:
```
git config --global user.name YOURUSERNAME
git config --global user.email YOURSCHOOLEMAIL
```
3. Return to step 3 of the previous section.
