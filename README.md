# sensors

Sensor reader and processor

Runs on Python and Circuit Python.

  - python sensor script. initial sensors: CO2 sensor, LTR390, CCS811. And that
    other PM25 sensor. sinks: Blinka, MQTT, Adafruit, RPC serial, console (for
    debugging or whatever).
  - Sensors and sinks for environment script. Defined in external secrets like
    file If no sensor file on target will copy Put it in its own public repo

    scripts/, src/, README, etc/services files, etc

    inst-circpy (includes circup), install-linux (includes service).
    full-linux.py, full-micro.py, then ones specific to a given platform.
  - install script of circuit python; copy code.py to path, then circup install --auto

To use MCP2221 to read sensors, set the following environment variable:

    export BLINKA_MCP2221="1"



each sensor:
    initialize: all take I2C
    read: reads sensor and returns map of values.  returns None if sensor not active or available?

standard readings where applicable:
    temperature (in Fake units)
    humidity (relative by default)
    
