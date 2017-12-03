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
    """Backup files to a specific directory by reading a given configuration file"""

    def __init__(self, config_file):
        self.config_file = config_file
        self.main_log_path = 'logs/main.log'
        self.error_log = 'logs/error.log'
        #Request entity management to list entities
        self.dc = EntityManagement(self.config_file)
        self.f_id, self.f_name, self.f_mdate, self.f_desc = self.dc.list_entity()


    def execute_backup(self, backupdest):
        """Backup the files.

        Usage: execute_backup(backup_destination)"""
        
        fs = FileStat()
        lastest_mdates = fs.check_file_changes(self.f_name)

        #verify if there files changed
        f_updated = self.check_modified_files(lastest_mdates)

        #backup files if they are not backued up yet
        absent_files = self.fetch_absent_files_from_backupdir(backupdest)
        if absent_files:
            self.copy_new_files(backupdest)
        #if there are updated files: update entity, append to log and backup file
        elif f_updated:
            self.request_entity_update(self.f_mdate, f_updated)
            self.copy_changed_files(backupdest, f_updated)
            self.update_config_file()

    def update_config_file(self):
        #Encode entities to required format
        encode = Encode(self.config_file)
        jdump = encode.json_dump_model(self.f_id, self.f_desc, self.f_name, self.f_mdate)
        #Request data to be written to file
        if jdump:
            self.write_changes(jdump)
        else:
            self.commit_to_log_file('Error: Failed to write to ' + self.config_file, error_log)

    def copy_new_files(self, backupdest):
        for k, name in self.f_name.iteritems():
            shutil.copy(name, backupdest)
        self.commit_to_log_file('INFO: Backup executed successfully', self.main_log_path, self.f_name)

    def copy_changed_files(self, backupdest, entity):
        cached_files = {}
        for k, v in entity.iteritems():
            shutil.copy(self.f_name[k], backupdest)
            temp_cache = {}
            temp_cache[k] = v
            cached_files.update(temp_cache)
        self.commit_to_log_file('INFO: Backup executed successfully', self.main_log_path, cached_files)

    def fetch_absent_files_from_backupdir(self, backupdest):
        cached_files = {}
        for k, v in self.f_name.iteritems():
            #remove absolute path from file attribute
            filename = v.split('/')[-1]
            list_of_backups = os.listdir(backupdest)
            local_cache = {}
            if filename not in list_of_backups:
                local_cache[k] = v
                cached_files.update(local_cache)
        return cached_files

    @staticmethod
    def commit_to_log_file(msg, log_path, entity = None):
        #log changes
        log = Log(log_path)
        if entity is None:
            log.commit_log(msg)
        else:
            log.commit_log(msg, entity)

    def write_changes(self, data):
        f = File(self.config_file)
        f.write_to_file(data, 'w')

    def check_modified_files(self, lastest_mdates):
        cached_changes = {}
        for k, v in lastest_mdates.iteritems():
            if v != self.f_mdate[k]:
                local_cache = {}
                local_cache[k] = v
                cached_changes.update(local_cache)
        return cached_changes

    def request_entity_update(self, entity, last_modified_data):
        cached_changes = {}
        if last_modified_data:
            for obj_id, last_modified_date in last_modified_data.iteritems():
                #update entity: entity name, id, value to be updated, and the filename as reference
                temp_cache = {}
                temp_cache = self.dc.update_entity(entity, obj_id, last_modified_date)
                cached_changes.update(temp_cache)

            #flush history to log file if exists
            if cached_changes:
                self.commit_to_log_file('INFO: File modified since last Backup', self.main_log_path, cached_changes)
            return True
        else:
            return False
