from File import File
from DataModel import DataModel
from DataModelObserver import DataModelObserver
from FileStat import FileStat

class Config(object):
    def __init__(self, config_file):
        self.config_file = config_file

    def add_config(self, filename, description = None):
        #Read the file by parsing the filename
        f = File(self.config_file)
        data_loaded = f.read_yaml_file()

        #get data model loaded to obtain new file id
        dm = DataModel(data_loaded)
        dm.set_data_model()

        #generate new file_id
        dm.set_file_id_dict()
        dm.update_modified_data_dict(10) #add new class ManageDataModel

        print dm.get_modified_date_dict()






        #Get new file timestamp (last modified date)
        fs = FileStat(filename)
        modified_date = fs.get_time_t()

        #append values to DataModel

        #request changes from DataModelObserver by issuing all entities
        #dmo = DataModelObserver(self.config_file)
        #dmo.generate_json_config_dump(dm.get_file_id_dict(), description, filename, modified_date, 'w')

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
            print 'Added: {}'.format(filename)
