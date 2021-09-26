#!/usr/bin/env python

from adafruit_pm25.i2c import PM25_I2C

class PM25:
    """pm2.5"""

    def __init__(self, i2c):
        reset_pin = None

        self.i2c = i2c
        self.pm25 = PM25_I2C(i2c, reset_pin)

    def read(self):
        pmdata = self.pm25.read()

        return {
            # Standard concentration units
            'pm10 standard':  pmdata['pm10 standard'],
            'pm25 standard':  pmdata['pm25 standard'],
            'pm100 standard': pmdata['pm100 standard'],
            # Environmental concentration units
            'pm10 env':  pmdata['pm10 env'],
            'pm25 env':  pmdata['pm25 env'],
            'pm100 env': pmdata['pm100 env'],
            # Raw particle counts
            'particles 03um':  pmdata["particles 03um"],
            'particles 05um':  pmdata["particles 05um"],
            'particles 10um':  pmdata["particles 10um"],
            'particles 25um':  pmdata["particles 25um"],
            'particles 50um':  pmdata["particles 50um"],
            'particles 100um': pmdata["particles 100um"]
        }
