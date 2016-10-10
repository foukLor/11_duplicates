import os
import sys
import hashlib

def get_all_files_in_dir(file_path):
    all_files = []
    for (root, dirs, files) in os.walk(file_path):
        for file_in_dir in files:            
            file_name_in_dir = os.path.join(root, file_in_dir)
            all_files.append(file_name_in_dir)
    return all_files

def hash_of_file(file_path):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file_path, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def is_contains_duplicates(files):
    if files is None:
        return
    list_files = {}
    dubl_files = []
    for filename in files:
        file_info = hash_of_file(filename)
        if not file_info in list_files.keys():
            list_files[file_info] = os.path.dirname(filename)
        else:
            dubl_files.append(filename)
    return dubl_files


if __name__ == '__main__':
    dir_name = sys.argv[1]
    if not os.path.isdir(dir_name):
        exit(1)
    files = get_all_files_in_dir(dir_name)
    duplicates = is_contains_duplicates(files)
    print("These files should be delete to save the space\n {0}".format(duplicates))
