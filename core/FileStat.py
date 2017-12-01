import datetime
import os
import sys

class FileStat(object):
    def __init__(self):
        self.dateTime = ''
        self.cached_changes = {}

    def set_cached_changes(self, data):
        self.cached_changes.update(data)

    def get_cached_changes(self):
        return self.cached_changes

    def get_time_t(self, fname):
        """  time_t  /* time of last modification */ """
        time_t = os.path.getmtime(fname)
        self.dateTime = datetime.datetime.fromtimestamp(time_t)
        return self.__str__()

    def __str__(self):
        return str(self.dateTime)

    def check_file_changes(self, fname):
        local_cache = {}
        for k, v in fname.iteritems():
            if self.get_time_t(v):
                local_cache[k] = self.get_time_t(v)
                self.set_cached_changes(local_cache)
        return self.get_cached_changes()
