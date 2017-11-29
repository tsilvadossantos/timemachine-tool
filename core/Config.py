from EntityManagement import EntityManagement
from Encode import Encode
import json

class Config(object):
    def __init__(self, config_file):
        self.config_file = config_file

    def add_config(self, filename, description = None):
        #request entity management to add new entity
        dc = EntityManagement(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.add_entity(filename, description)

        #Encode new entities to json and make it persistence
        dmo = Encode(self.config_file)
        dmo.json_dump_model(f_id, f_desc, f_name, f_mdate)

    def list_config(self, config_file):
        #Request entity management to list entities
        dc = EntityManagement(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.list_entity()
        self.display_config_file(f_id, f_name, f_mdate, f_desc)

    def remove_config(self, filename):
        #Request entity management to remove a member of the entity
        dc = EntityManagement(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.remove_entity(filename)

        #Encode new entities to json and make it persistence
        dmo = Encode(self.config_file)
        dmo.json_dump_model(f_id, f_desc, f_name, f_mdate)

    def display_config_file(self, f_id, f_name, f_mdate, f_desc):
        inner_data = {}
        self.encode = {'file_descriptor': []}
        for id_key, id_value in f_id.items():
            inner_data = {}
            inner_data = {'file_id' : id_value, 'description' : f_desc[id_value], 'file' : f_name[id_value], 'modified_date' : f_mdate[id_value]}
            print json.dumps(inner_data, indent=2, ensure_ascii=False)
