from EntityManagement import EntityManagement
from File import File
from Encode import Encode
from Log import Log
import sys
import json

class Config(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.main_log_path = 'logs/main.log'
        self.error_log = 'logs/error.log'

    def add_config(self, filename, description = None):
        #request entity management to add new entity
        dc = EntityManagement(self.config_file)
        if dc.add_entity(filename, description):
            f_id, f_name, f_mdate, f_desc = dc.add_entity(filename, description)

            #Encode new entities to json and make it persistence
            dmo = Encode(self.config_file)
            jdump = dmo.json_dump_model(f_id, f_desc, f_name, f_mdate)
            if jdump:
                #commit changes to file
                self.commit_to_config_file(jdump)
                #save changes to log
                self.commit_to_log_file('INFO: Added new file to configuration file ' + filename, self.main_log_path)
        else:
            self.commit_to_log_file('Error: Failed to add file / File is already added to ' + filename, self.error_log)
            self.abort_operation()

    def list_config(self, config_file):
        #Request entity management to list entities
        dc = EntityManagement(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.list_entity()
        self.display_config_file(f_id, f_name, f_mdate, f_desc)

    def remove_config(self, filename):
        #Request entity management to remove a member of the entity
        dc = EntityManagement(self.config_file)
        if dc.remove_entity(filename):
            f_id, f_name, f_mdate, f_desc = dc.remove_entity(filename)

            #Encode new entities to json and make it persistence
            dmo = Encode(self.config_file)
            jdump = dmo.json_dump_model(f_id, f_desc, f_name, f_mdate)

            if jdump:
                #commit changes to file
                self.commit_to_config_file(jdump)
                #save changes to log
                self.commit_to_log_file('INFO: Removed file from ' + filename, self.main_log_path)
        else:
            self.commit_to_log_file('Error: File:' + filename + ' not found in the configuration file', self.error_log)
            self.abort_operation()

    def commit_to_config_file(self, data):
        f = File(self.config_file)
        f.write_to_file(data, 'w')

    def commit_to_log_file(self, msg, log_path):
        #log changes
        log = Log(log_path)
        log.commit_log(msg)

    def abort_operation(self):
        sys.exit(1)

    def display_config_file(self, f_id, f_name, f_mdate, f_desc):
        inner_data = {}
        for id_key, id_value in f_id.items():
            inner_data = {}
            inner_data = {'file_id' : id_value, 'description' : f_desc[id_value], 'file' : f_name[id_value], 'modified_date' : f_mdate[id_value]}
            if inner_data:
                print json.dumps(inner_data, indent=2, ensure_ascii=False)
        if not inner_data:
            print 'Config file is empty: {}'.format(self.config_file)
