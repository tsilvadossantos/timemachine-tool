import datetime
import os

class FileStat(object):
    def __init__(self, fn):
        self.filename = fn
        self.dateTime = ''

    def get_time_t(self):
        """  time_t  /* time of last modification */ """
        time_t = os.path.getmtime(self.filename)
        self.dateTime = datetime.datetime.fromtimestamp(time_t)
        return self.__str__()

    def __str__(self):
        return str(self.dateTime)
