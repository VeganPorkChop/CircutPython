import board
import neopixel
import time

Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)
Kaz.brightness = 1  

while True:
    Kaz.fill((204, 0, 153))
    time.sleep(3)
    Kaz.fill((204, 255, 204))
    time.sleep(3)