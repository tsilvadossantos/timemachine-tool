import re
import json
from core.File import File

class DataModel(object):

    def __init__(self, dl):
        self.data_loaded = dl
        self.file_id = {}
        self.file_name = {}
        self.modified_date = {}
        self.description = {}

    def set_data_model(self):
        for datamodel_i in xrange(0, len(self.data_loaded['file_descriptor']), 1):
            self.set_file_id_dict(datamodel_i)

        for id_k, id_v in self.get_file_id_dict().iteritems():
            self.set_file_name_dict(id_k, id_v)
            self.set_modified_date_dict(id_k, id_v)
            self.set_description_dict(id_k, id_v)

    def set_file_id_dict(self, datamodel_i, filter_string = 'file_id'):
        self.file_id[datamodel_i] = self.data_loaded['file_descriptor'][datamodel_i][filter_string]

    def get_file_id_dict(self):
        return self.file_id

    def set_file_name_dict(self, data_index, file_id, filter_string = 'file'):
        self.file_name[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]

    def get_file_name_dict(self):
        return self.file_name

    def set_modified_date_dict(self, data_index = None, file_id = None, data_value = None, filter_string = 'modified_date'):
        if data_index != None and file_id != None:
            self.modified_date[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]
        else:
            self.modified_date[file_id] = data_value

    def get_modified_date_dict(self):
        return self.modified_date

    def set_description_dict(self, data_index, file_id, filter_string = 'description'):
        self.description[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]

    def get_description_dict(self):
        return self.description
