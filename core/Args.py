import argparse

class Args(object):
    """Get command line arguments"""
    def __init__(self, fp = None, bd = 'None'):
        if fp is None:
            self.filename = fp
        if bd is None:
            self.backupdest = bd
        parser = argparse.ArgumentParser(description='Time Machine Application - File Backup Periodically')
        parser.add_argument('-f', '--file', type=str, default = 'resources/FileConfig.yml',
                            help='path to config file')
        parser.add_argument('-bd', '--backupdestination', type=str, default = 'backup_dest',
                            help='path backup')
        self.args = parser.parse_args()
        self.set_filename_arg(self.args)
        self.set_backupdest_arg(self.args)

    def set_filename_arg(self, args):
        self.filename = args.file

    def get_filename_arg(self):
        return self.filename

    def set_backupdest_arg(self, args):
        self.backupdest = args.backupdestination

    def get_backupdest_arg(self):
        return self.backupdest
