from DataModelObserver import DataModelObserver

class BackupHistory(object):
    def __init__(self):
        self.backup_history = {}

    def set_backup_history(self, modification_history):
        self.backup_history = modification_history
        self.make_modification_history_persistent()


    def get_backup_history(self):
        return self.backup_history

    def make_modification_history_persistent(self):
        dmo = DataModelObserver(self.backup_history)
        dmo.generate_json_log_dump(self.get_backup_history(), 'w')
