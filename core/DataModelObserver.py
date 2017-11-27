from File import File
from DataModel import DataModel
import json
from collections import defaultdict

class DataModelObserver(DataModel):
    def __init__(self, config_file):
        self.config_file = config_file
        self.encode_dict = {'file_descriptor': []}
        self.f = File(self.config_file)

    def set_encode_dict(self, inner_dict):
        self.encode_dict['file_descriptor'].append(inner_dict)

    def get_encode_dict(self):
        return self.encode_dict

    def generate_json_dump(self, file_id, desc, fname, modified_date):
        inner_dict = {}
        for id_key, id_value in file_id.items():
            inner_dict = {'file_id' : id_value, 'description' : desc[id_value], 'file' : fname[id_value], 'modified_date' : modified_date[id_value]}
            self.set_encode_dict(inner_dict)
        #Write to file
        self.f.write_to_json_file(self.get_encode_dict())
