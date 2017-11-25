from core.FileStat import FileStat
from core.DataModel import DataModel
from core.File import File
from core.DataModel import DataModel
import shutil


class BackupFiles(DataModel):

    def __init__(self, config_file):
        #Read the file by parsing the filename
        self.f = File(config_file)
        data_loaded = self.f.read_yaml_file()

        #get a dict of files from config file
        self.dm = DataModel(data_loaded)
        self.dm.set_data_model()

    def execute_backup(self, backup_dest):
        new_modified_date_dict = {}
        for fk, fv in self.dm.get_file_name_dict().iteritems():
            fs = FileStat(fv)
            #check if file last modified_date changed
            if fs.get_time_t() != self.dm.get_modified_date_dict()[fk]:
                #copy files to backup destination
                self.copy_files(fv, backup_dest)

                #update modified_date dictionary with new modification datetime
                new_modified_date_dict = self.dm.get_modified_date_dict()
                new_modified_date_dict[fk] = fs.get_time_t()                

                #write changes to config file
                self.f.write_to_yam_file(self.dm.get_file_name_dict(), self.dm.get_modified_date_dict(), self.dm.get_description_dict())

    @staticmethod
    def copy_files(orig, dst):
        shutil.copy(orig, dst)
