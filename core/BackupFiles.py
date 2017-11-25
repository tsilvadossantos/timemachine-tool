import shutil
from core.FileStat import FileStat
from core.DataModel import DataModel

class BackupFiles(object):
    def __init__(self, fn, md, desc):
        self.file_name = fn
        self.modified_date = md
        self.file_description = desc

    def execute_backup(self, backup_dest):
        list_of_changes_dict = {}
        for fk, fe in self.file_name.iteritems():
            fs = FileStat(fe)
            #check if file last modified_date has changed
            if fs.get_time_t() != self.modified_date[fk]:
                print 'different'
                #dm = DataModel(data_loaded)
                #dm.set_modified_date_dict(fk)
                #shutil.copy(f, backup_dest)
                #update dict object to write to file
        #        self.modified_date[fk] = fs.get_time_t()
        #print self.modified_date


    def remove_files(self):
        pass
