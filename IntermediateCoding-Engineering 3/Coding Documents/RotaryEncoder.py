import rotaryio
import board
import time
from lcd.lcd import LCD 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import analogio
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
enc = rotaryio.IncrementalEncoder(board.D4, board.D3)
last_position = None
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
while True:
    position = enc.position
    if position > 3:
        position = 0
    if position < 0:
        position = 3
    print(position)
    enc.position = position
    time.sleep(.01)