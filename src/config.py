#!/usr/bin/env python

import board
import sensors
import sinks

i2c = board.I2C()  # uses board.SCL and board.SDA

config = {
    'sources': [
        # sensors.BMP280(i2c),
        # sensors.CCS811(i2c),
        # sensors.PM25(i2c),
        sensors.SCD30(i2c),
        # sensors.LTR390(i2c)
    ],
    'sinks': [
        sinks.Logger(),
        # sinks.Stdout()
        sinks.AdafruitIO(),
    ],
    'delay': 30.0
}
