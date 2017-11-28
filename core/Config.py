from File import File
from DataModel import DataModel

class Config(object):
    def __init__(self):
        pass

    def add_config(self, filename):
        pass

    def list_config(self, config_file):
        #Read the file by parsing the filename
        f = File(config_file)
        data_loaded = f.read_yaml_file()

        #read config file by instantiating the DataModel
        dm = DataModel(data_loaded)
        dm.set_data_model()
        self.display_config(dm.get_file_name_dict())

    def remove_config(self, filename):
        pass

    def display_config(self, filedict):
        for filename in filedict.values():
            print filename
