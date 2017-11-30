from File import File
from time import gmtime, strftime
from datetime import datetime
import calendar
import os
import json
import yaml

class Log(object):
    def __init__(self, log_path):
        self.log_path = log_path
        self.timestamp = 0
        self.cached_log_entries = {}
        self.dtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def set_cached_log_entries(self, data):
        self.cached_log_entries.update(data)

    def get_cached_log_entries(self):
        return self.cached_log_entries

    def set_timestamp(self):
        self.timestamp = self.dtime

    def get_timestamp(self):
        return self.timestamp

    def commit_log(self, msg, entity = None):
        temp_data = {}
        if entity is None:
            self.set_timestamp()
            temp_data[self.get_timestamp()] = msg
            self.set_cached_log_entries(temp_data)
            self.flush_data()
        else:
            for k, v in entity.iteritems():
                log_entry_body = '{} file_id:{} - {}'.format(msg, str(k), v)
                self.set_timestamp()
                temp_data[self.get_timestamp()] = log_entry_body
                self.set_cached_log_entries(temp_data)
                self.flush_data()

    def get_log_path():
        return self.log_path

    def flush_data(self):
        #check if log dir exists before flushing the data
        dirname = self.log_path.split('/')[0]
        if not self.verify_dir_exists(dirname):
            self.create_log_dir(dirname)
        temp_cache = []
        for k, v in self.get_cached_log_entries().iteritems():
            log_entry = '{} {} {} {}'.format(k,'', v, '\n')
            f = File(self.log_path)
            f.write_to_file(log_entry, 'a')

    def create_log_dir(self, dirname):
        os.mkdir(dirname)

    def verify_dir_exists(self, obj):
        if os.path.isdir(obj):
            return True
        return False

    def verify_file_exists(self, obj):
        if os.path.isfile(obj):
            return True
        return False
