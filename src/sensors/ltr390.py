#!/usr/bin/env python

import adafruit_ltr390

class LTR390:
    """Reads LTR390 UV sensor"""

    def __init__(self, i2c):
        self.i2c = i2c
        self.ltr = adafruit_ltr390.LTR390(i2c)

    def read(self):
        return {
            'uvs':   self.ltr.uvs,
            'light': self.ltr.light,
            'uvi':   self.ltr.uvi,
            'lux':   self.ltr.lux
        }
