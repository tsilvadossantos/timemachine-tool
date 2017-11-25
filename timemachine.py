from core.Args import Args
from core.File import File
from core.DataModel import DataModel
from core.BackupFiles import BackupFiles

if __name__ == '__main__':
    #Get the command lines arguments
    args = Args()
    fn, bd = args.get_args()
    config_file, backupdest = fn[0], bd[0]

    #Read the file by parsing the filename
    f = File(config_file)
    data_loaded = f.read_yaml_file()

    #get a dict of files from config file
    dm = DataModel(data_loaded)
    dm.set_data_model()

    #provide the dict of files, modified_date, and description for backup
    bkp = BackupFiles(dm.get_file_name_dict(), dm.get_modified_date_dict(), dm.get_description_dict())
    bkp.execute_backup(backupdest)

    #print l.get_dict_of_modified_date()
    #print l.get_dict_of_description()
