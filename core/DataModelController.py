from File import File
from DataModel import DataModel

class DataModelController(DataModel):
    def __init__(self, config_file):
        self.config_file = config_file

    def initialize_data_model(self):
        #make_initial_setup (open file and generate entities)
        f = File(self.config_file)
        data_loaded = f.read_yaml_file()

        #instantiate ModelData class which each attribute considered an independent ity
        dm = DataModel(data_loaded)
        dm.set_data_model()
        return dm.get_file_id(), dm.get_f_name(), dm.get_f_mdate(), dm.get_f_desc()

    def update_entity(self, entity, obj_id, value):
        #copy old value
        old_value = entity[obj_id]
        #set new value
        entity[obj_id] = value
        #get new value
        new_value = entity[obj_id]
        #o_flusher contains a a pair value old_value, new_value
        obj_flusher = {}
        obj_flusher[obj_id] = [old_value, new_value]
        return obj_flusher


    def remove_entity(self):
        pass

    def add_entity(self):
        pass

    def list_entity(self):
        pass
