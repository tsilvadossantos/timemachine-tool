from core.Args import Args
from core.BackupFiles import BackupFiles
from core.Config import Config

if __name__ == '__main__':

    #Get the command lines arguments by initializing its class
    args = Args()
    config_file = args.get_config_file_arg()
    backup_path = args.get_backupdest_arg()
    file_name_add = args.get_add_file_arg()
    file_desc = args.get_file_desc_arg()
    file_name_rm = args.get_remove_file_arg()
    config_file_name = args.get_list_config_arg()

    #backup files
    bkp = BackupFiles(config_file)

    #execute main program functionality - Make a backup
    bkp.execute_backup(backup_path)

    #verify which argument has passed on cli to call the related method
    #a file is been added to config_file?
    if file_name_add:
        Config(config_file).add_config(file_name_add, file_desc)

    #a file is been removed from config_file?
    if file_name_rm:
        Config(config_file).remove_config(file_name_rm)

    #user is listing files in config_file?
    if config_file_name:
        Config(config_file).list_config(config_file_name)
