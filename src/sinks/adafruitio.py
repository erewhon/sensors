#!/usr/bin/env python

from Adafruit_IO import Client, Feed, RequestError
import os

class AdafruitIO:
    """Writes object to Adafruit IO"""

    def __init__(self):
        self.user = os.environ.get('ADAFRUIT_USER')
        self.password = os.environ.get('ADAFRUIT_PASSWORD')
        self.location = os.environ.get('SENSOR_LOCATION')

        self.feeds = {}
        self.aio = Client(self.user, self.password)

        # Get list of feeds and create them if
        feeds = self.aio.feeds()

        for feed in feeds:
            if feed.name.startswith(self.location):
                self.feeds[feed.name] = feed

    def feed(self, attr):
        key = f'{self.location}_{attr}'
        if key in self.feeds:
            return self.feeds[key]
        else:
            feed = self.aio.create_feed(Feed(name=key))
            self.feeds[key] = feed
            return feed

    def write(self, obj):
        for key, value in obj.items():
            # we skip the timestamp value
            if key != 'time':
                feed = self.feed(key)

                self.aio.send(feed.key, value)
