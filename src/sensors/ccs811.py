#!/usr/bin/env python

import adafruit_ccs811

class CCS811:
    """CCS811 Air Quality Sensor Breakout - VOC and eCO2 - https://www.adafruit.com/product/3566"""

    def __init__(self, i2c):
        self.i2c = i2c
        self.ccs811 = adafruit_ccs811.CCS811(i2c)

    def read(self):
        if self.ccs811.data_ready:
            return {
                'eco2': self.ccs811.eco2,
                'tvoc': self.ccs811.tvoc
            }
        else:
            return None
