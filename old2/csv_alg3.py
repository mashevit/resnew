import csv
from tabulate import tabulate

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'output.csv'

try:
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]

        # Use tabulate to format and print the data
        table = tabulate(data, headers="firstrow", tablefmt="grid")
        print(table)

except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")