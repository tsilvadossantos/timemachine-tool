from DataModelObserver import DataModelObserver

class BackupHistory(object):
    def __init__(self):
        self.backup_history = {}

    def set_backup_history(self, modification_history):
        self.backup_history = modification_history
        dmo = DataModelObserver(self.backup_history)
        dmo.generate_json_log_dump(self.get_backup_history())

    def get_backup_history(self):
        return self.backup_history
