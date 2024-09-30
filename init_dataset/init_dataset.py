file_path = '../zoo/zoo.data'

# Path to the file
#file_path = '/mnt/data/zoo.data'

# Open and read the file
with open(file_path, 'r') as file:
    contents = file.read()

# Print the contents
print(contents)
