# main.py -- put your code here!
from machine import Pin
from neopixel import NeoPixel
from time

pin = Pin(48, Pin.OUT)
neo = NeoPixel(pin, 1)
while True:
    neo[0] = (255, 0, 0)
    time.sleep(0.2)
    neo.write()

    neo[0] = (0, 255, 0)
    time.sleep(0.2)
    neo.write()

    neo[0] = (0, 0, 255)
    time.sleep(0.2)
    neo.write()