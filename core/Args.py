import argparse

class Args(object):
    """Get command line arguments"""
    def __init__(self, fp = None, bd = None, add_file = None, rem_file = None, list_config = None):
        if fp is None:
            self.filename = fp
        if bd is None:
            self.backupdest = bd
        if add_file is None:
            self.add_file = add_file
        if rem_file is None:
            self.rem_file = rem_file
        if list_config is None:
            self.list_config = list_config

        parser = argparse.ArgumentParser(description='Time Machine Application - File Backup Periodically')
        parser.add_argument('-f', '--file', type=str, default = 'resources/FileConfig.yml',
                            help='path to config file')
        parser.add_argument('-bd', '--backupdestination', type=str, default = 'backup_dest',
                            help='path backup')
        parser.add_argument('-add', '--addfile', type=str, default = None,
                            help='add file to config')
        parser.add_argument('-remove', '--removefile', type=str, default = None,
                            help='remove file from config')
        parser.add_argument('-list', '--listconfig', type=str, default = None,
                            help='list config file')

        self.args = parser.parse_args()
        self.set_config_file_arg(self.args)
        self.set_backupdest_arg(self.args)
        self.set_add_file_arg(self.args)
        self.set_remove_file_arg(self.args)
        self.set_list_config_arg(self.args)

    def set_config_file_arg(self, args):
        self.filename = args.file

    def get_config_file_arg(self):
        return self.filename

    def set_backupdest_arg(self, args):
        self.backupdest = args.backupdestination

    def get_backupdest_arg(self):
        return self.backupdest

    def set_add_file_arg(self, args):
        self.add_file = args.addfile

    def get_add_file_arg(self):
        return self.add_file

    def set_remove_file_arg(self, args):
        self.rem_file = args.removefile

    def get_remove_file_arg(self):
        return self.rem_file

    def set_list_config_arg(self, args):
        self.list_config = args.listconfig

    def get_list_config_arg(self):
        return self.list_config
