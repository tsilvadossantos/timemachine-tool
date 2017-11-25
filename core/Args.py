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
                            help='path to config file', required=True, nargs='+')
        parser.add_argument('-bd', '--backupdestination', type=str, default = 'backup_dest',
                            help='path backup', required=True, nargs='+')
        self.args = parser.parse_args()
        self.set_args(self.args)

    def set_args(self, args):
        self.filename = args.file
        self.backupdest = args.backupdestination

    def get_args(self):
        return self.filename, self.backupdest
