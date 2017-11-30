import os.path
import json
import re
import sys

class File(object):
    """Read file and return a list of data"""
    def __init__(self, filename = None):
        if filename != None:
            self.filename = filename
        self.data_loaded = {}
        self.main_log_path = 'logs/main.log'
        self.error_log = 'logs/error.log'

    def read_yaml_file(self):
        try:
            with open(self.filename, "r") as r:
                self.data_loaded = json.load(r)
                return self.data_loaded
        except:
            print 'Error reading the file or file not found: {}'.format(self.filename) #some stdout to user
            self.commit_to_log_file('Error: Failed to add file / File is already added to ' + filename, self.error_log)
            self.abort_operation()
        return None

    def write_to_file(self, stream, mode):
        try:
            f = open(self.filename, mode)
            f.write(stream)
            f.close()
        except:
            print 'Error to write to file: {}'.format(self.filename) #some stdout to user
            self.commit_to_log_file('Error: Failed to add file / File is already added to ' + filename, self.error_log)
            self.abort_operation()

    def commit_to_log_file(self, msg, log_path):
        log = Log(log_path)
        log.commit_log(msg)

    def abort_operation(self):
        sys.exit(1)
