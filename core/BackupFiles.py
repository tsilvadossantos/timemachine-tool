from FileStat import FileStat
from DataModel import DataModel
from File import File
from DataModel import DataModel
from DataModelObserver import DataModelObserver
import shutil

class BackupFiles(DataModel):

    def __init__(self, config_file):
        #Read the file by parsing the filename
        self.config_file = config_file
        self.f = File(self.config_file)
        self.data_loaded = self.f.read_yaml_file()

        #get a dict of files from config file
        self.dm = DataModel(self.data_loaded)
        self.dm.set_data_model()

    def execute_backup(self, backup_dest):
        modification_date_history = {}
        flag = 0
        #iterate over the dictionary of files to check each modified_date timestamp
        for fk, fv in self.dm.get_file_name_dict().iteritems():

            #to-do
            #get list of files in dir and check if file is present


            fs = FileStat(fv)
            #check if file last modified_date changed
            if fs.get_time_t() != self.dm.get_modified_date_dict()[fk]:
                flag = 1
                #copy files to backup destination
                self.copy_files(fv, backup_dest)

                #update modified_data value for modified_date[fk]
                copy_of_old_timestamp = self.dm.get_modified_date_dict()[fk]
                self.dm.set_modified_date_dict(None, fk, fs.get_time_t())

                #setup modification record with filename_id and old and new timestamp
                copy_of_new_timestamp = self.dm.get_modified_date_dict()[fk]
                modification_date_history[fk] = copy_of_old_timestamp, copy_of_new_timestamp

        #request changes from DataModelObserver
        dmo = DataModelObserver(self.config_file)
        dmo.generate_json_dump(self.dm.get_file_id_dict(), self.dm.get_description_dict(), self.dm.get_file_name_dict(), self.dm.get_modified_date_dict())


        #self.f.write_to_yam_file(data_dump)

    @staticmethod
    def copy_files(orig, dst):
        shutil.copy(orig, dst)
