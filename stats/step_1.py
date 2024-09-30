import os
import csv
import pandas as pd
import os
import numpy as np


# Define a converter function
def safe_int(x):
    try:
        return int(x)
    except ValueError:
        return np.nan  # or any other default value you prefer
'''
# Assuming csv_files is a list of file paths
csv_files = ['file1.csv', 'file2.csv', 'file3.csv']

# Initialize an empty DataFrame to store the results
result_df = pd.DataFrame()

# Counter to generate unique column names
counter = 1

for csv_file in csv_files:
    # Read the CSV file, specifying header=None to avoid reading the first row as column names
    data = pd.read_csv(csv_file, header=None)
    
    # Assuming you want to add the second column to the result DataFrame
    column_name = f'Column_{counter}'
    result_df[column_name] = data.iloc[:, 1]
    
    counter += 1

# Display the result DataFrame
print(result_df)
'''
name_new = 'output_new2'
filenew = 'zoo16'
dirnew = 'zoo2'
#if NaN then hallucination#################################################################
# Initialize an empty DataFrame to store the results
result_df = pd.DataFrame()
# Define the features and corresponding output folders
strfeatures = "Habitat, Diet, Social behavior, Lifespan, Reproduction, Size, Conservation status, Predation, Migration patterns, Communication"
strnew = strfeatures.lower()
features = [f.strip() for f in strnew.split(",")]
output_folders = [f"/{name_new}/{f.strip()}" for f in features]
current_directory = os.getcwd()
new_directory = current_directory + "/.."
os.chdir(new_directory)    
# Create a list to store the data
all_data = []
# Counter to generate unique column names
counter = 20
current_directory = os.getcwd()
newdir1 = current_directory + f'/{dirnew}/'
destination_file = os.path.join(newdir1, 'zoo2.data')
df = pd.read_csv(destination_file, header=None)
# Iterate over each feature and read the corresponding CSV file
for feature, folder in zip(features, output_folders):

    current_directory = os.getcwd()
    print(f"{current_directory}")
    newdir = current_directory + folder
    file_path = os.path.join(newdir, "out1_combined")
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:

            #data = pd.read_csv(file, header=None, dtype={1: int})
            data = pd.read_csv(file, header=None, converters={1: safe_int})
            # Assuming you want to add the second column to the result DataFrame
            column_name = f'{counter}'
            result_df[column_name] = data.iloc[:, 1]
            df[column_name] = data.iloc[:, 1]
            counter += 1
'''
            csv_reader = csv.reader(file)
            for row in csv_reader:
                animal, middle_num, _ = row
                all_data.append((animal, middle_num, feature))
'''

# Display the result DataFrame
print(result_df)
'''

# Write the combined data to a new CSV file
with open("combined_output.csv", mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Animal', 'Middle Number', 'Feature'])
    for data in all_data:
        csv_writer.writerow(data)

'''
#newdir1 = current_directory + '/zoo1/'
destination_file = os.path.join(newdir1, f'{filenew}')

#df = df.select_dtypes(include=['int'])



df_int = df.select_dtypes(include=['int'])

# Add the first column back to the DataFrame
df_int.insert(0, df.columns[0], df[df.columns[0]])

df = df_int
# Assuming 'df' is your DataFrame
column_17 = df.iloc[:, 17]  # Extract column 17

# Drop column 17 from the DataFrame
df.drop(df.columns[17], axis=1, inplace=True)




# Add column 17 back to the DataFrame as the last column
df['column_17'] = column_17
# Assume df is your DataFrame and 'file.csv' is your CSV file
#df = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})  # Example DataFrame
file_path = 'file.csv'

# Append the DataFrame columns to the CSV file
df.to_csv(destination_file, mode='a', header=True, index=False)


'''
import shutil
newdir = current_directory + '/zoo/'
file_path = os.path.join(newdir, "zoo.data")
source_file1 = 'source.txt'
destination_file1 = 'destination.txt'
newdir1 = current_directory + '/zoo1/'
destination_file = os.path.join(newdir1, 'zoo1.data')
# Copy the contents of the source file to the destination file
shutil.copyfile(file_path, destination_file)

'''