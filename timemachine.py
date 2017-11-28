from core.Args import Args
from core.BackupFiles import BackupFiles
from core.Config import Config

if __name__ == '__main__':

    #Get the command lines arguments by initializing its class
    args = Args()

    #backup files
    bkp = BackupFiles(args.get_config_file_arg())
    #execute main program functionality - Make a backup
    bkp.execute_backup(args.get_backupdest_arg())

    #verify which argument has passed on cli to call the related method
    #a file is been added to config_file?
    if args.get_add_file_arg():
        Config().add_config(args.get_add_file_arg())

    #a file is been removed from config_file?
    if args.get_remove_file_arg():
        Config().remove_config(args.get_remove_file_arg())

    #user is listing files in config_file?
    if args.get_list_config_arg():
        Config().list_config(args.get_list_config_arg())
