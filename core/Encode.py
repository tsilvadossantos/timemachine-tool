from time import gmtime, strftime
from File import File
import json
import os

class Encode(object):

    def __init__(self, config_file):
        self.config_file = config_file
        self.encode = {}

    def set_encode(self, outer_label, inner_data):
        self.encode[outer_label].append(inner_data)

    def get_encode(self):
        return self.encode

    def json_dump_model(self, f_id, f_desc, f_name, f_mdate):
        inner_data = {}
        self.encode = {'file_descriptor': []}
        for id_key, id_value in f_id.items():
            inner_data = {}
            inner_data = {'file_id' : id_value, 'description' : f_desc[id_value], 'file' : f_name[id_value], 'modified_date' : f_mdate[id_value]}
            self.set_encode('file_descriptor', inner_data)

        #Write to config file
        f = File(self.config_file)
        f.write_to_json_file(self.get_encode())

    def json_dump_history(self, flush_history):
        inner_data = {}
        self.encode = {'file_last_modification': []}
        for id_key, id_value in flush_history.items():
            inner_data = {'file_id' : id_key, 'last_two_changes' : id_value}
            self.set_encode('file_last_modification', inner_data)

        # prepare log dir and write to log file
        log_dir = 'logs'
        log_name = 'main.log'
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        else:
            dtime = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
            os.rename(log_dir + '/' + log_name, log_dir + '/' + log_name + '.' + dtime)
            f = File('logs/file_changes.log')
            f.write_to_json_file(self.get_encode())
