from File import File
from DataModel import DataModel
import json
from collections import defaultdict
import pprint

class DataModelObserver(DataModel):
    def __init__(self, config_file):
        self.config_file = config_file
        self.new_load = []
        self.f = File(self.config_file)

    def set_new_load_dict(self, nl):
        self.new_load.append(nl)

    def get_new_load_dict(self):
        return self.new_load

    def generate_json_dump(self, file_id, desc, fname, modified_date):
        for id_key, id_value in file_id.items():
            get_values = [id_value, desc[id_value], fname[id_value], modified_date[id_value]]
            list_data.append(get_values)

        list_collection = (zip(list_data))
