from core.Args import Args
from core.BackupFiles import BackupFiles

if __name__ == '__main__':
    #Get the command lines arguments
    args = Args()
    fn, bd = args.get_args()
    config_file, backupdest = fn[0], bd[0]

    #provide the dict of files, modified_date, and description for backup and the data load for modification
    bkp = BackupFiles(config_file)
    bkp.execute_backup(backupdest)

    #print l.get_dict_of_modified_date()
    #print l.get_dict_of_description()
