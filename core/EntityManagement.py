from File import File
from FileStat import FileStat
from DataModel import DataModel
import sys

class EntityManagement(DataModel):
    def __init__(self, config_file = None):
        if config_file != None:
            self.config_file = config_file
            self.id_key_serial = 0
            self.id_value_serial = 0

    def get_id_key_serial(self):
        return self.id_key_serial

    def get_id_value_serial(self):
        return self.id_value_serial

    def initialize_data_model(self):
        #make_initial_setup (open file and generate entities)
        f = File(self.config_file)
        data_loaded = f.read_yaml_file()

        #instantiate ModelData class which each attribute considered an independent ity
        dm = DataModel(data_loaded)
        dm.set_data_model()
        self.id_key_serial = dm.get_id_key_serial()
        self.id_value_serial = dm.get_id_value_serial()
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

    def add_entity(self, filename, description):
        #initialize data
        f_id, f_name, f_mdate, f_desc = self.initialize_data_model()

        #if file is present in config_file
        if self.search_member_entity(filename, f_name):
            return None
        else:
            #add new file_id entity
            file_id_key = self.get_id_key_serial() + 1
            file_id_value = self.get_id_value_serial() + 1
            f_id[file_id_key] = file_id_value

            #add new file entity
            f_name[file_id_value] = filename

            #add new modified_date entit
            fs = FileStat(filename)
            last_modified_date = fs.get_time_t()
            f_mdate[file_id_value] = last_modified_date

            #add new file description entity
            f_desc[file_id_value] = description
            return f_id, f_name, f_mdate, f_desc

        return None

    def remove_entity(self, filename):
        #initialize data
        f_id, f_name, f_mdate, f_desc = self.initialize_data_model()

        #if file is not present in config_file
        if self.search_member_entity(filename, f_name):
            key_found = self.search_member_entity(filename, f_name)
            #pop ou the member from all entities
            for k, v in f_id.iteritems():
                if v == key_found:
                    f_id_key = k
            if f_id_key:
                f_id.pop(f_id_key)
                f_name.pop(key_found)
                f_mdate.pop(key_found)
                f_desc.pop(key_found)
                return f_id, f_name, f_mdate, f_desc
        else:
            return None

        return None

    def list_entity(self):
        return self.initialize_data_model()


    def search_member_entity(self, member, entity):
        for k, v in entity.iteritems():
            if member == v:
                return k
        return False
