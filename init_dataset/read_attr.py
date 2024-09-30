# Input file name
input_file_name = "../zoo/zoo.names"  # Replace with your actual file name

# Initialize a flag to indicate when to start and stop collecting attribute information
is_attribute_info = False
first = 0
# List to store attribute information lines
attribute_info_lines = []
i = 0
# Read the content of the input file
with open(input_file_name, 'r') as file:
    for line in file:
        i = i + 1
        print(f"i={i} tf = {is_attribute_info}")
        print(line)
        if not line.strip():
            print("empty")
        if is_attribute_info:
            print(line.strip())
            # Collect lines until an empty line is encountered (end of attribute information)
            if first >= 3:
                if not line.strip():
                    break
               # if not first:
                attribute_info_lines.append(line.strip())
            first += 1
        elif "Attribute" in line:
            is_attribute_info = True
            first = 1

#else:
  #  is_attribute_info = False
            '''line.strip() == "Attribute Information:":
            # Start collecting attribute information when this line is found
            collect_attribute_info = True'''

# Extract attribute names from the collected lines
attribute_names = [line.split("\t")[0].strip() for line in attribute_info_lines]

# Join attribute names into a comma-separated string
attribute_names_string = ', '.join(attribute_names)

# Print the result
print(attribute_names_string)



# Sample line from the file
line = "7. Attribute Information: (name of attribute and type of value domain)"

# Check if the line contains "Attribute Information"
if "Attribute Information" in line:
    is_attribute_info = True
else:
    is_attribute_info = False

print(is_attribute_info)

#print("1. animal name:      Unique for each instance".strip())