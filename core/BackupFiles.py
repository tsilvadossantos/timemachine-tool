from File import File
from FileStat import FileStat
from DataModel import DataModel
from Encode import Encode
from BackupHistory import BackupHistory
from DataModelController import DataModelController
from Args import Args
import shutil
import os

class BackupFiles(DataModel):

    def __init__(self, config_file):
        self.config_file = config_file

    def execute_backup(self, backupdest):
        flush_history = {}
        #get initial data for backup
        dc = DataModelController(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.initialize_data_model()

        #iterate over the dictionary of files to check each modified_date timestamp
        for obj_id, fn in f_name.iteritems():
            fs = FileStat(fn)
            last_modified_date = fs.get_time_t()

            #if file is not present in backupdir - backup is created for the first time
            f = fn.split('/')[-1] #remove absolute path from file attribute
            if self.is_file_in_backupdir(f, backupdest):
                self.copy_files(fn, backupdest)

            #ELSE: check if file last modified_date changed
            elif last_modified_date != f_mdate[obj_id]:
                #copy files to backup destination
                self.copy_files(fn, backupdest)

                #update entity: entity name, id, value to be updated, and the filename as reference
                cached_data = {}
                cached_data = dc.update_entity(f_mdate, obj_id, last_modified_date)
                flush_history.update(cached_data)

        #Encode entities to required format
        encode = Encode(self.config_file)
        encode.json_dump_model(f_id, f_desc, f_name, f_mdate)

        #flush history to file if exists
        if flush_history:
            encode.json_dump_history(flush_history)

    @staticmethod
    def copy_files(orig, dst):
        shutil.copy(orig, dst)

    def is_file_in_backupdir(self, filename, backupdest):
        list_of_backups = os.listdir(backupdest)
        if filename not in list_of_backups:
            return True
        return None
