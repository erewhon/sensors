#!/usr/bin/env bash
set -euo pipefail

PIP3=/usr/local/opt/python-3.9.7/bin/pip3.9

sudo $PIP3 install \
    adafruit-blinka \
    adafruit-circuitpython-amg88xx \
    adafruit-circuitpython-bmp280 \
    adafruit-circuitpython-ccs811 \
    adafruit-circuitpython-ltr390 \
    adafruit-circuitpython-pm25 \
    adafruit-circuitpython-scd30 \
    adafruit-python-shell \
    adafruit-io
