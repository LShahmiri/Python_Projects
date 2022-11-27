# How to sort files in a appropriate folders
import glob
import os

files_List = glob.glob('*')
extension_Set = set()
# Identifying a set of file's types
for each_File in files_List:
    try:
        extension = each_File.split('.')[1]
        extension_Set.add(extension)
    except:
        continue
    

# Craete folders based on type of files
def creat_folders():
    for items in extension_Set:
        if items == 'py':
            continue
        try:
            os.makedirs(items+'_files')
        except:
            continue
# Moving files to appropriate folder
def move_files():
    for each_file in files_List:
        Extension = each_file.split('.')[1]
        try:
            os.rename(each_file, Extension+'_files/'+each_file)
        except:
            continue
        
        
creat_folders()
move_files()
        
        
    


