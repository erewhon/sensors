#!/usr/bin/env python

# "DATASHEET": http://cl.ly/ekot
# https://gist.github.com/kadamski/92653913a53baf9dd1a8

import serial, struct, sys, time, json, subprocess

DEBUG = 0
CMD_MODE = 2
CMD_QUERY_DATA = 4
CMD_DEVICE_ID = 5
CMD_SLEEP = 6
CMD_FIRMWARE = 7
CMD_WORKING_PERIOD = 8
MODE_ACTIVE = 0
MODE_QUERY = 1
PERIOD_CONTINUOUS = 0

class PM25USB:
    """PM25 USB sensor"""

    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = "/dev/ttyUSB0"
        self.ser.baudrate = 9600

        self.ser.open()
        self.ser.flushInput()

    def read(self):
        if self.ccs811.data_ready:
            return {
                'eco2': self.ccs811.eco2,
                'tvoc': self.ccs811.tvoc
            }
        else:
            return None
