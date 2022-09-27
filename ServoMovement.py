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
