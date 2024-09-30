import csv
from tabulate import tabulate

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'Datasets\covtype.csv'

try:
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        first_row = next(csv_reader)  # Read the first row (header)

        # Create a list of lists for tabulate
        table_data = [
            [str(i + 1) for i in range(len(first_row))],  # First row with indexes
            first_row,  # Second row with data from the first line
        ]

        # Use tabulate to format and print the table
        table = tabulate(table_data, headers='keys', tablefmt='grid')
        print(table)

except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")