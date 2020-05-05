#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Displays an animated gif.
"""

import os.path
from luma.oled.device import ssd1306
from luma.core.interface.serial import i2c
from PIL import Image, ImageSequence
from luma.core.sprite_system import framerate_regulator

device0 = ssd1306(i2c(port=0, address=0x3C))
device1 = ssd1306(i2c(port=1, address=0x3C))

def main():
    regulator = framerate_regulator(fps=10)
    left_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'res', 'Fallin-L.gif'))
    left = Image.open(img_path)
    reight_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'res', 'Fallin-R.gif'))
    right = Image.open(img_path)
    size = [min(*device.size)] * 2
    posn = ((device.width - size[0]) // 2, device.height - size[1])

    while True:
        for frame in ImageSequence.Iterator(left):
            with regulator:
                background = Image.new("RGB", device.size, "white")
                background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                device1.display(background.convert(device1.mode))
        for frame in ImageSequence.Iterator(right):
            with regulator:
                background = Image.new("RGB", device.size, "white")
                background.paste(frame.resize(size, resample=Image.LANCZOS), posn)
                device0.display(background.convert(device0.mode))
