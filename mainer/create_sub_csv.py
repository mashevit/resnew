import csv
import os
# Input CSV file path
input_csv_file = '../zoo/zoo.data'

# Output CSV file path
output_csv_file = '../output/output.csv'


# Function to read the input CSV and write the first and last columns to the output CSV
def extract_first_and_last_columns(input_file, output_file):
    current_directory = os.getcwd()
    print(f"sddssdsd = {current_directory}")
    with open(input_file, 'r') as csvfile, open(output_file, 'w', newline='') as output_csvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(output_csvfile)

        for row in reader:
            first_column = row[0]  # Get the first column
            last_column = row[-1]  # Get the last column
            writer.writerow([first_column, last_column])


# Call the function
#extract_first_and_last_columns(input_csv_file, output_csv_file)

#print(f"First and last columns extracted and saved to {output_csv_file}.")
