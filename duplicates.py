import os
import sys


def get_duplicates(dir_path):
    files_in_dir = {}
    duplicates_files = {}
    for (file_root, dirs, all_files) in os.walk(dir_path):
        for searching_file in all_files:
            file_name = os.path.join(file_root,searching_file)
            file_key = searching_file +  str(os.path.getsize(file_name))
            path_of_file_in_dict = files_in_dir.get(file_key, False)
            if path_of_file_in_dict :
                duplicates_files.setdefault(path_of_file_in_dict,[]).append(file_name)
            else:
                files_in_dir[file_key] = file_name
    return duplicates_files


def print_duplicates(duplicates):
    print("These files should be deleted to save the space:")
    for duplicate_list in duplicates.values():
        for duplicate in duplicate_list:
            print(duplicate)


if __name__ == '__main__':
    dir_name = sys.argv[1]
    if not os.path.isdir(dir_name):
        exit(1)
    duplicates = get_duplicates(dir_name)
    print_duplicates(duplicates)