from core.Args import Args
from core.File import File
from core.List import List

if __name__ == '__main__':
    #Get the command lines arguments
    args = Args()
    file_name = args.get_args()

    #Read the file by parsing the filename
    f = File(file_name[0])
    #read_file method returns the loaded data
    data_loaded = f.read_file()

    #get a list of files
    l = List()
    file_name_list = l.get_list_of_files()
