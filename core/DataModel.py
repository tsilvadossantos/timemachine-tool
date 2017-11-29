import re
import json
from core.File import File

class DataModel(object):

    def __init__(self, dl):
        self.data_loaded = dl
        self.file_id = {}
        self.f_name = {}
        self.f_mdate = {}
        self.f_desc = {}
        self.wild_card = {}
        self.id_key_serial = -1
        self.id_value_serial = 0

    def set_id_key_serial(self):
        self.id_key_serial += 1

    def get_id_key_serial(self):
        return self.id_key_serial

    def set_id_value_serial(self):
        self.id_value_serial += 1

    def get_id_value_serial(self):
        return self.id_value_serial

    def set_data_model(self):
        for datamodel_i in xrange(0, len(self.data_loaded['file_descriptor']), 1):
            self.set_file_id(datamodel_i)

        for id_k, id_v in self.get_file_id().iteritems():
            self.set_f_name(id_k, id_v)
            self.set_f_mdate(id_k, id_v)
            self.set_f_desc(id_k, id_v)

    def set_file_id(self, datamodel_i = None, filter_string = 'file_id'):
        self.file_id[datamodel_i] = self.data_loaded['file_descriptor'][datamodel_i][filter_string]
        self.set_id_key_serial()
        self.set_id_value_serial()

    def get_file_id(self):
        return self.file_id

    def set_f_name(self, data_index, file_id, filter_string = 'file'):
        self.f_name[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]

    def get_f_name(self):
        return self.f_name

    def set_f_mdate(self, data_index, file_id, filter_string = 'modified_date'):
            self.f_mdate[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]

    def get_f_mdate(self):
        return self.f_mdate

    def set_f_desc(self, data_index, file_id, filter_string = 'description'):
        self.f_desc[file_id] = self.data_loaded['file_descriptor'][data_index][filter_string]

    def get_f_desc(self):
        return self.f_desc
