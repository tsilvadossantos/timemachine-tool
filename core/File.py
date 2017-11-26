import os.path
import yaml
import re

class File(object):
    """Read file and return a list of data"""
    def __init__(self, filename):
        self.filename = filename
        self.data_loaded = {}

    def read_yaml_file(self):
        try:
            with open(self.filename, "r") as r:
                self.data_loaded = yaml.load(r)
        except IOError as err:
            return False
        return self.data_loaded

    def write_to_yam_file(self, yaml_dump_list):
        file_temp = self.filename + '.yml'
        print yaml_dump_list
        ptn1 = 'file'
        with open(file_temp, 'w') as w:
            for dl in yaml_dump_list:
                if 'description' in dl:
                    print re.sub(r'\b{}\b'.format('description'), '- description', dl)
                
            #w.write(dl)
        #os.rename(self.filename, self.filename + '.bkp')
        #os.rename(file_temp, self.filename)

    def verify_file_exists(self):
        if os.path.isfile(self.filename):
            return True
        return False
