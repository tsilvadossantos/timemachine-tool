from File import File
from DataModel import DataModel

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
        new_load_dict_temp = {}
        new_load_dict_temp['file_descriptor'] = {}
        for id_value in file_id.values():
            new_load_dict_temp['file_descriptor']['file_id'] = id_value
            new_load_dict_temp['file_descriptor']['description'] = desc[id_value]
            new_load_dict_temp['file_descriptor']['file'] = fname[id_value]
            new_load_dict_temp['file_descriptor']['modified_date'] = modified_date[id_value]
            self.set_new_load_dict(new_load_dict_temp)
            print self.get_new_load_dict()
        #self.f.write_to_yam_file(self.get_new_load_dict())
