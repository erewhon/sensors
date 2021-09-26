#!/usr/bin/env python

import json
import logging

class Logger:
    """Writes object to stdout"""

    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info("""Starting sensors""")

    def write(self, obj):
        logging.info(obj)
