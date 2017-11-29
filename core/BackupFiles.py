from File import File
from FileStat import FileStat
from DataModel import DataModel
from DataModelObserver import DataModelObserver
from BackupHistory import BackupHistory
from Args import Args
import shutil
import os

class BackupFiles(DataModel):

    def __init__(self, config_file):
        self.config_file = config_file

    def execute_backup(self, backupdest):
        #make_initial_setup (open file and load data)
        #Read the file by parsing the filename
        self.f = File(self.config_file)
        self.data_loaded = self.f.read_yaml_file()

        #each line of the config file is returned as an independent entity represented by a dictionary
        self.dm = DataModel(self.data_loaded)
        self.dm.set_data_model()

        #list to append modified dates
        modification_date_history = []

        #iterate over the dictionary of files to check each modified_date timestamp
        for fk, fv in self.dm.get_file_name_dict().iteritems():
            fs = FileStat(fv)

            #if file is not present in backupdir - backup is created for the first time
            f = fv.split('/')[-1] #remove absolute path from file attribute
            if self.is_file_in_backupdir(f, backupdest):
                self.copy_files(fv, backupdest)

            #ELSE: check if file last modified_date changed
            elif fs.get_time_t() != self.dm.get_modified_date_dict()[fk]:
                #copy files to backup destination
                self.copy_files(fv, backupdest)

                #update modified_data value for modified_date[fk]
                copy_of_old_timestamp = self.dm.get_modified_date_dict()[fk]
                dm.update_modified_data_dict(10)
                self.dm.set_modified_date_dict(None, fk, fs.get_time_t())

                #Log in file changes
                #setup modification record with filename_id and old and new timestamp
                copy_of_new_timestamp = self.dm.get_modified_date_dict()[fk]
                list_of_changes = fv, copy_of_old_timestamp, copy_of_new_timestamp
                modification_date_history.append(list_of_changes)

        #issue change history to BackupHistory
        self.create_backup_history(modification_date_history)

        #request changes from DataModelObserver by issuing all entities
        dmo = DataModelObserver(self.config_file)
        dmo.generate_json_config_dump(self.dm.get_file_id_dict(), self.dm.get_description_dict(), self.dm.get_file_name_dict(), self.dm.get_modified_date_dict(), 'w')

    @staticmethod
    def copy_files(orig, dst):
        shutil.copy(orig, dst)

    def is_file_in_backupdir(self, filename, backupdest):
        list_of_backups = os.listdir(backupdest)
        if filename not in list_of_backups:
            return True
        return None

    def create_backup_history(self, mh):
        #issue change history to BackupHistory
        bkph = BackupHistory()
        bkph.set_backup_history(mh)
