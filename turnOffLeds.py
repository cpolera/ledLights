import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 180)

for x in range(1, 180):
        pixels[x] = (0,0,0)
