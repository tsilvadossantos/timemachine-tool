import os.path
import json
import re

class File(object):
    """Read file and return a list of data"""
    def __init__(self, filename = None):
        if filename != None:
            self.filename = filename
        self.data_loaded = {}

    def read_yaml_file(self):
        try:
            with open(self.filename, "r") as r:
                self.data_loaded = json.load(r)
        except IOError as err:
            return False
        return self.data_loaded

    def write_to_json_file(self, dict_dump):
        jdump = (json.dumps(dict_dump, indent=4))
        file_temp = self.filename + '.yml'
        with open(file_temp, 'a') as append_file:
            append_file.write(jdump)
        #os.rename(self.filename, self.filename + '.bkp')
        #os.rename(file_temp, self.filename)

    def verify_file_exists(self):
        if os.path.isfile(self.filename):
            return True
        return False
