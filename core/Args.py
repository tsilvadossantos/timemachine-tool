import argparse

class Args(object):
    """Get command line arguments"""
    def __init__(self, fp = None):
        if fp is None:
            self.filename = fp
        parser = argparse.ArgumentParser(description='Time Machine Application - File Backup Periodically')
        parser.add_argument('--file', type=str, help='path to target file', required=True, nargs='+')
        self.args = parser.parse_args()
        self.set_args(self.args)

    def set_args(self, args):
        self.filename = args.file

    def get_args(self):
        return self.filename
