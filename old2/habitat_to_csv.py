import csv

# Read data from the text file
with open('concat2/22', 'r') as file:
    lines = file.readlines()

# Process the lines to extract the data
data = []
header = lines[1].strip().split('|')[1:-1]  # Extract header and remove leading/trailing spaces
print(header)
for line in lines[3:-1]:
    #print(line)
    values = line.strip().split('|')[1:-1]  # Extract values and remove leading/trailing spaces
    print(f"values: {values} ")
    print(f"values[0]: {values[1]} ")
    animal = values[1].strip()
    habitat_features = [int(value.strip()) for value in values[2:]]
    data.append([animal] + habitat_features)
outputFilename = 'concat2/22.csv'
# Write the data to a CSV file
with open(outputFilename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)  # Write header
    writer.writerows(data)  # Write data rows

print(f"CSV file {outputFilename} has been created.")