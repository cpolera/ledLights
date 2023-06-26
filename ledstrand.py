import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 180)
ledCount = 128
pixels[0] = (ledCount, 0, 0)
time.sleep(5)

for x in range(1, ledCount//2):
        pixels[x] = (0,0,255)
#       sleep(1)

for y in range(ledCount//2 + 1, ledCount):
        pixels[y] = (255,69,0)

