#!/usr/bin/env python

import colorsys
import signal
import time

import blinkt_gpiod as blinkt

spacing = 360.0 / 16.0
hue = 0
run = True

def do_exit(signum, frame):
  global run
  run = False

signal.signal(signal.SIGTERM, do_exit)
signal.signal(signal.SIGINT, do_exit)

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

while run:
    hue = int(time.time() * 100) % 360
    for x in range(blinkt.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        blinkt.set_pixel(x, r, g, b)

    blinkt.show()
    time.sleep(0.001)

