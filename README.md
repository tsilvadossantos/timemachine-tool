# TimeMachine Tool - Script to Execute Files Backups Periodically

## Application Structure:
The "fileConfig.json" contain a list of files to have a backup. This files contains:
1. File ID: Uniq and Serialized ID.
2. File description: file description provided by the user.
3. File name: file name specified by the user in the CLI.
4. Modification Date: last modified data, taken from stat.

The four attributes of a given file(ID, Name, Description, and Modification Date) are treated in this project as an independent entity, that are managed individually, but any changes in any of the entities are cascaded to each other
by respecting they relationship.

IMPORTANT: Even though it is possible to, users should not edit the configuration file manually in order to avoid errors. In order to add/edit/remove a specific file from the configuration file, user should use: -add or -remove
parameters.

##Usage:

### To execute backups by running the script:
1. `$ python timemachine.py -f resources/FileConfig.json -bd backup_dest`
2. `$ python timemachine.py`

### add a file to a configuration file (If description is not specified the value will be Null)
1. `$ python timemachine.py -add sample_files/file1 -desc 'new file using add - well done'`

### remove file from a configuration file
1. `$ python timemachine.py -remove sample_files/file1`

1. -list configuration file content
`$ python timemachine.py -list resources/FileConfig.json`

## Project Content:
```
├── README.md
├── backup_dest - "Backup destination"
├── core
│   ├── Args.py - "Class to get CLI arguments"
│   ├── BackupFiles.py - "Class to Execute Backups"
│   ├── Config.py - "Class to manage the configuration file"
│   ├── DataModel.py - "Class to create the data model"
│   ├── Encode.py - "Class to encode dictionaries to json format"
│   ├── EntityManagement.py - "Observer Class to manage the data"
│   ├── File.py - "Class to read and write to files"
│   ├── FileStat.py - "Class to obtain a give file timestamp"
│   ├── Log.py - "Class to log system events"
│   └── __init__.py
├── designdoc.txt
├── logs
│   ├── error.log - "Error log output"
│   └── main.log - "Main application log output"
├── resources
│   └── FileConfig.json - "Configuration file"
├── sample_files
│   ├── file
│   ├── file1
│   ├── file2
│   ├── file3
│   ├── file4
│   └── file5
└── timemachine.py - "Application caller"
```

## Classes and Methods:

1. Args.py
Class to manage CLI arguments
```
Methods:
def set_config_file_arg(self, args): set file config arguments
def get_config_file_arg(self): get file config arguments
def set_backupdest_arg(self, args): set backup destination arg
def get_backupdest_arg(self): get backup destination arg
def set_add_file_arg(self, args): set add file arg
def get_add_file_arg(self): get add file arg
def set_file_desc_arg(self, args): set file description arg
def get_file_desc_arg(self): get file description arg
def set_remove_file_arg(self, args): set remove file arg
def get_remove_file_arg(self): get remove file arg
def set_list_config_arg(self, args): set list config files arg
def get_list_config_arg(self): get list config files arg
```


2. BackupFiles.py
Class to backup files (Execute Backup)
```
Methods:
def execute_backup(self, backupdest): execute the backup
def update_config_file(self): update configuration file with new file modification date
def copy_new_files(self, backupdest): copy files to backup dir
def copy_changed_files(self, backupdest, entity): copy files to backup dir
def fetch_absent_files_from_backupdir(self, backupdest): check which files are in the backup dir
def commit_to_log_file(msg, log_path, entity = None): add logging
def write_changes(self, data): write to file
def check_modified_files(self, lastest_mdates): check if files have been modified
def request_entity_update(self, entity, last_modified_data): request observer to update data content
```

3. Config.py
Class to manage the configuration file (List, Add, Remove)
```
Methods:
def add_config(self, filename, description = None): add a file to a specified configuration file
def list_config(self, config_file): list the configuration file
def remove_config(self, filename): remove a specified file from configuration file
def commit_to_config_file(self, data): edit configuration file
def commit_to_log_file(self, msg, log_path): append to log file
def abort_operation(self): sys.exit
def display_config_file(self, f_id, f_name, f_mdate, f_desc): list configuration file content
```

4. DataModel.py
Class to defined the configuration file content as dictionaries and treats each line of the file
as a different entity: File ID, File Name, File Description, File Modification Date
```
Methods:
def set_id_key_serial(self): set serial key serial id for File_ID dictionary Key
def get_id_key_serial(self): get value serial key serial id for File_ID dictionary Key
def set_id_value_serial(self): set serial Value serial id for File_ID dictionary Value
def get_id_value_serial(self): get serial Value serial id for File_ID dictionary Value
def set_data_model(self): initialize the datamodel
def set_file_id(self, datamodel_i = None, filter_string = 'file_id'): set File ID
def get_file_id(self): get File ID
def set_f_name(self, data_index, file_id, filter_string = 'file'): Set File Name
def get_f_name(self): get File Name
def set_f_mdate(self, data_index, file_id, filter_string = 'modified_date'): Set File Modification Date
def get_f_mdate(self): get File Modification Dates
def set_f_desc(self, data_index, file_id, filter_string = 'description'): Set File Description
def get_f_desc(self): get File Description
```

5. Encode.py
Class to encode dictionary to json format.
```
Methods:
def set_encode(self, outer_label, inner_data): set json data structure
def get_encode(self): get json datastructure
def json_dump_model(self, f_id, f_desc, f_name, f_mdate): encode directory to json
```

6. EntityManagement.py
Class to initialize the Data Model and observe changes and updates.
```
Methods:
def get_id_key_serial(self): get value serial key serial id for File_ID dictionary Key
def get_id_value_serial(self): get serial Value serial id for File_ID dictionary Value
def is_entity_present(self): check if a entity is present in the data model
def set_data_model_entrypoint(self, filename, description): set first data model if not present
def initialize_data_model(self): generate/model the data
def update_entity(self, entity, obj_id, value): make updates to entities
def add_entity(self, filename, description): add new data to entities
def remove_entity(self, filename): remove data from entities
def list_entity(self): list an specific entity
def search_member_entity(self, member, entity): search for a particular member in a given entity
```

7. File.py
Class to call file operations (Read, Write and Append)
```
Methods:
def read_yaml_file(self): read a given json file
def write_to_file(self, stream, mode): read a given json file
def abort_operation(self): sys.exit
```

8. FileStat.py
Class to check modified date in a given file path.
```
Methods:
def set_cached_changes(self, data): method to cache changed data
def get_cached_changes(self): method to return changed data
def get_time_t(self, fname): method to get file modified date
def __str__(self): return a string
def check_file_changes(self, fname): method to get filename and return changes
```

9. Log.py
```
Class to log main application events to log/main.log and log/error.log.
If not present, folders and files will be created automatically.

Methods:
def set_cached_log_entries(self, data): set data cache for future use
def get_cached_log_entries(self): return data cached
def set_timestamp(self): set the timestamp based on current datetime
def get_timestamp(self): return timestamp
def commit_log(self, msg, entity = None): request to commit the events output to file
def get_log_path(): check if a log path is valid
def flush_data(self): flush data to be written to file
def create_log_dir(self, dirname): setup log directory
def verify_dir_exists(self, obj): check if log dir exists
def verify_file_exists(self, obj): verify if file exists
```
