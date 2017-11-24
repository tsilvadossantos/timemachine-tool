import os.path
import yaml

class File(object):
    """Read file and return a list of data"""
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, "r") as r:
                data_loaded = yaml.load(r)
                #list_of_words.append(str(line.strip()).lower())
        except IOError:
            return False
        return data_loaded

    def write_to_file(self):
        file_temp = self.filename + '.tmp'
        #node1_version, node2_version = getargs()
        with open(self.filename, 'r') as r:
             with open(file_temp, 'w') as a:
                 for line in r:
                     if line == 'pattern':
                         a.write('line')
                     #else:
                    #     a.write('line')
        os.rename(file_temp, self.filename)

    def verify_file_exists(self):
        if os.path.isfile(self.filename):
            return True
        return False
