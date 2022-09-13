import board
import neopixel
import time

Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Kaz.brightness = 1  #setting the brightness of the light, from 0-1 brightness

while True:
    Kaz.fill((204, 0, 153))#setting the color with RGB values
    time.sleep(3)#pausing code
    Kaz.fill((204, 255, 204))
    time.sleep(3)