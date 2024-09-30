import csv

# Replace 'input.txt' with the path to your input text file
input_file = 'Datasets/zoo.data'

# Replace 'output.csv' with the path to your output CSV file
output_file = 'output.csv'

try:
    with open(input_file, 'r') as input_file:
        lines = input_file.read().splitlines()

    with open(output_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)

        for line in lines:
            data = line.split(',')
            csv_writer.writerow(data)

    print(f'Data from {input_file.name} has been successfully written to {output_file.name} as a CSV file.')

except FileNotFoundError:
    print(f"The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")