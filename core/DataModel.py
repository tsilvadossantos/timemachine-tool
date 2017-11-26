import re
import yaml
import json

class DataModel(object):

    def __init__(self, dl):
        self.data_loaded = dl
        self.file_name = {}
        self.modified_date = {}
        self.description = {}

    def set_data_model(self):
        for datamodel_i, datamodel_e in enumerate(self.data_loaded):
            self.set_file_name_dict(datamodel_i)
            self.set_modified_date_dict(datamodel_i)
            self.set_description_dict(datamodel_i)

    def set_file_name_dict(self, id, filter_string = 'file'):
        self.file_name[id] = self.data_loaded[id][filter_string]

    def get_file_name_dict(self):
        return self.file_name

    def set_modified_date_dict(self, id, filter_string = 'modified_date'):
        self.modified_date[id] = self.data_loaded[id][filter_string]

    def get_modified_date_dict(self):
        return self.modified_date

    def set_description_dict(self, id, filter_string = 'description'):
        self.description[id] = self.data_loaded[id][filter_string]

    def get_description_dict(self):
        return self.description

    def generate_temp_data_model(self, new_date, fname, desc):
        new_load = {}
        new_list = []
        for di, data in enumerate(self.data_loaded):
            new_load['description'] = desc[di]
            new_load['file'] = fname[di]
            new_load['modified_date'] = new_date[di]
            new_list.append(yaml.dump(new_load, default_flow_style=False))
        return new_list
