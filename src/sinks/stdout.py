#!/usr/bin/env python

import json

class Stdout:
    """Writes object to stdout"""

    def __init__(self):
        pass

    def write(self, obj):
        print(json.dumps(obj))
