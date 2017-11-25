from core.DataModel import DataModel

class DictModel(object):
    def __init__(self, dl):
        self.data_loaded = dl
        self.dm = DataModel(self.data_loaded)
        self.dm.set_data_model()

    def get_dict_of_files(self):
        dict_of_files = []
        for lf_values in self.dm.get_file_name_dict().values():
            dict_of_files.append(lf_values)
        return dict_of_files

    def get_dict_of_modified_date(self):
        dict_of_mod_dates = []
        for lf_values in self.dm.get_modified_date_dict().values():
            dict_of_mod_dates.append(lf_values)
        return dict_of_mod_dates

    def get_dict_of_description(self):
        dict_of_desc = []
        for lf_values in self.dm.get_description_dict().values():
            dict_of_desc.append(lf_values)
        return dict_of_desc
