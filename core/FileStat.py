import datetime
import os

class TimeStamp(object):
    def __init__(self, fn):
        self.filename = filename

    def get_mod_time_stamp(self):
        timeStamp = os.path.getmtime(self.filename)
        dateTime = datetime.datetime.fromtimestamp(timestamp)
        return dateTime
