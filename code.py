import board
import neopixel

Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)
Kaz.brightness = 1 

print("Make it red!")

while True:
    Kaz.fill((204, 0, 153))
    print("Make it red!")