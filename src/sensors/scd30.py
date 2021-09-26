#!/usr/bin/env python

import adafruit_scd30

class SCD30:
    """Read SCD30 CO2 sensor"""

    def __init__(self, i2c):
        self.i2c = i2c
        self.scd = adafruit_scd30.SCD30(i2c)

    def read(self):
        if self.scd.data_available:
            return {
                'co2':         self.scd.CO2,
                'temperature': self.scd.temperature * 1.8 + 32.0,
                'humidity':    self.scd.relative_humidity
            }
        else:
            return None
