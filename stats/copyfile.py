import shutil
import os

current_directory = os.getcwd()
new_directory = current_directory + "/.."
os.chdir(new_directory)    
current_directory = os.getcwd()
newdir = current_directory + '/zoo/'
file_path = os.path.join(newdir, "zoo.data")
source_file1 = 'source.txt'
destination_file1 = 'destination.txt'
newdir1 = current_directory + '/zoo1/'
destination_file = os.path.join(newdir1, 'zoo2.data')
# Copy the contents of the source file to the destination file

# Ensure the destination directory exists
destination_directory = newdir1
os.makedirs(destination_directory, exist_ok=True)

shutil.copyfile(file_path, destination_file)