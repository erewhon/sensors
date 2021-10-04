#!/usr/bin/env python3.9

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
PERIOD_5MIN = 5

class PM25USB:
    """PM25 USB sensor"""

    # byte, data = 0, ""

    def __init__(self, dev='/dev/tty.usbserial-330'):
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info("""PM25USB Opening serial port""")

        self.ser = serial.Serial()
        self.ser.port = dev # "/dev/ttyUSB0"
        self.ser.baudrate = 9600

        self.ser.open()
        self.ser.flushInput()

        logging.info("""PM25USB initializing""")

        self.cmd_set_sleep(0)
        self.cmd_firmware_ver()
        self.cmd_set_working_period(PERIOD_5MIN)
        self.cmd_set_mode(MODE_QUERY);

        logging.info("""PM25USB done initializing""")

    def dump(self, d, prefix=''):
        print(prefix + ' '.join(x.encode('hex') for x in d))

    def construct_command(self, cmd, data=[]):
        assert len(data) <= 12
        data += [0,]*(12-len(data))
        checksum = (sum(data)+cmd-2)%256
        ret = "\xaa\xb4" + chr(cmd)
        ret += ''.join(chr(x) for x in data)
        ret += "\xff\xff" + chr(checksum) + "\xab"

        if DEBUG:
            self.dump(ret, '> ')
        return ret.encode()

    def process_data(self, d):
        r = struct.unpack('<HHxxBB', d[2:])
        pm25 = r[0]/10.0
        pm10 = r[1]/10.0
        checksum = sum(v for v in d[2:8])%256
        return [pm25, pm10]
        #print("PM 2.5: {} μg/m^3  PM 10: {} μg/m^3 CRC={}".format(pm25, pm10, "OK" if (checksum==r[2] and r[3]==0xab) else "NOK"))

    def process_version(self, d):
        r = struct.unpack('<BBBHBB', d[3:])
        checksum = sum(v for v in d[2:8])%256
        print("Y: {}, M: {}, D: {}, ID: {}, CRC={}".format(r[0], r[1], r[2], hex(r[3]), "OK" if (checksum==r[4] and r[5]==0xab) else "NOK"))

    def read_response(self):
        byte = 0
        while byte != b'\xaa':
            byte = self.ser.read(size=1)

        d = self.ser.read(size=9)

        if DEBUG:
            self.dump(d, '< ')

        return byte + d

    def cmd_set_mode(self, mode=MODE_QUERY):
        self.ser.write(self.construct_command(CMD_MODE, [0x1, mode]))
        self.read_response()

    def cmd_query_data(self):
        self.ser.write(self.construct_command(CMD_QUERY_DATA))
        d = self.read_response()
        values = []
        if d[1] == ord(b'\xc0'):
            values = self.process_data(d)
        return values

    def cmd_set_sleep(self, sleep):
        mode = 0 if sleep else 1
        self.ser.write(self.construct_command(CMD_SLEEP, [0x1, mode]))
        self.read_response()

    def cmd_set_working_period(self, period):
        self.ser.write(self.construct_command(CMD_WORKING_PERIOD, [0x1, period]))
        self.read_response()

    def cmd_firmware_ver(self):
        self.ser.write(self.construct_command(CMD_FIRMWARE))
        d = self.read_response()
        self.process_version(d)

    def cmd_set_id(self, id):
        id_h = (id>>8) % 256
        id_l = id % 256
        self.ser.write(self.construct_command(CMD_DEVICE_ID, [0]*10+[id_l, id_h]))
        self.read_response()

    def read(self):
        # todo : don't read if it's been less than 5 minutes?
        self.cmd_set_sleep(0)

        for t in range(15):
            values = self.cmd_query_data()
            if values is not None and len(values) == 2:
                print(values)
                time.sleep(2)

        self.cmd_set_sleep(5)

        return {
            'pm25': values[0],
            'pm100': values[1]
        }

if __name__ == '__main__':
    device = PM25USB('/dev/tty.usbserial-330')
