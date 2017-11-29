from DataModelController import DataModelController
import json

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
        #initialize data by calling the controller
        dc = DataModelController(self.config_file)
        dc.initialize_data_model()
        f_id, f_name, f_mdate, f_desc = dc.initialize_data_model()
        self.display_config_file(f_id, f_name, f_mdate, f_desc)

    def remove_config(self, filename):
        pass

    def display_config_file(self, f_id, f_name, f_mdate, f_desc):
        inner_data = {}
        self.encode = {'file_descriptor': []}
        for id_key, id_value in f_id.items():
            inner_data = {}
            inner_data = {'file_id' : id_value, 'description' : f_desc[id_value], 'file' : f_name[id_value], 'modified_date' : f_mdate[id_value]}
            print json.dumps(inner_data, indent=2, ensure_ascii=False)
