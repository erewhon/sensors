#!/usr/bin/env python

import adafruit_bmp280

class BMP280:
    """Reads BMP280 I2C or SPI Barometric Pressure & Altitude Sensor - https://www.adafruit.com/product/2651"""

    def __init__(self, i2c):
        self.i2c = i2c
        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
        self.bmp280.sea_level_pressure = 1015.0

    def read(self):
        return {
            'temperature': self.bmp280.temperature * 1.8 + 32.0,
            'pressure':    self.bmp280.pressure,
            'altitude':    self.bmp280.altitude * 3.2808
        }
