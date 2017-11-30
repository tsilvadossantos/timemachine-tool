from File import File
from FileStat import FileStat
from DataModel import DataModel
from Encode import Encode
from EntityManagement import EntityManagement
from Log import Log
from Args import Args
import shutil
import os

class BackupFiles(DataModel):

    def __init__(self, config_file):
        self.config_file = config_file

    def execute_backup(self, backupdest):
        main_log_path = 'logs/main.log'
        change_log_path = 'logs/last_modified_files_from_config.log'
        error_log = 'logs/error.log'
        cached_changes = {}
        #Request entity management to list entities
        dc = EntityManagement(self.config_file)
        f_id, f_name, f_mdate, f_desc = dc.list_entity()

        #iterate over the dictionary of files to check each modified_date timestamp
        for obj_id, fn in f_name.iteritems():
            fs = FileStat(fn)
            last_modified_date = fs.get_time_t()

            #if file is not present in backupdir - backup is created for the first time
            f = fn.split('/')[-1] #remove absolute path from file attribute
            if self.is_file_in_backupdir(f, backupdest):
                self.copy_files(fn, backupdest)
                self.commit_to_log_file('INFO: Backup executed successfully', main_log_path, f_name)

                #Encode entities to required format
                encode = Encode(self.config_file)
                jdump = encode.json_dump_model(f_id, f_desc, f_name, f_mdate)

                #Request data to be written to file
                if jdump:
                    self.write_changes(jdump)
                else:
                    self.commit_to_log_file('Error: Failed to write to ' + self.config_file, error_log)

            #ELSE: check if file last modified_date changed
            elif last_modified_date != f_mdate[obj_id]:
                #copy files to backup destination
                self.copy_files(fn, backupdest)
                self.commit_to_log_file('INFO: Backup executed successfully', main_log_path, f_name)

                #update entity: entity name, id, value to be updated, and the filename as reference
                temp_cache = {}
                temp_cache = dc.update_entity(f_mdate, obj_id, last_modified_date)
                cached_changes.update(temp_cache)

                #Encode entities to required format
                encode = Encode(self.config_file)
                jdump = encode.json_dump_model(f_id, f_desc, f_name, f_mdate)

                if jdump:
                    #Request data to be written to file
                    self.write_changes(jdump)
                else:
                    self.commit_to_log_file('Error: Failed to write to ' + self.config_file, error_log)

        #flush history to log file if exists
        if cached_changes:
            self.commit_to_log_file('INFO: File modified (last two modifications)', change_log_path, cached_changes)

    @staticmethod
    def copy_files(orig, dst):
        shutil.copy(orig, dst)

    def is_file_in_backupdir(self, filename, backupdest):
        list_of_backups = os.listdir(backupdest)
        if filename in list_of_backups:
            return False
        return True

    def commit_to_log_file(self, msg, log_path, entity = None):
        #log changes
        log = Log(log_path)
        if entity is None:
            log.commit_log(msg)
        else:
            log.commit_log(msg, entity)

    def write_changes(self, data):
        f = File(self.config_file)
        f.write_to_file(data, 'w')
