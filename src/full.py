#!/usr/bin/env python
#
# Kitchen sink sensor reader and publisher.  Reads config.py file
# for list of sensors and outputs
#

import time

try:
    from config import config
except ImportError:
    print("Configuration is kept in config.py. Please add it there!")
    raise

# enter event loop.  loop over sensors to get readings in a list
# and send readings to sinks.
while True:
    results = {
        'time': time.mktime(time.gmtime())
    }

    for source in config['sources']:
        results = results | source.read()

    for sink in config['sinks']:
        sink.write(results)

    time.sleep(config['delay'])
