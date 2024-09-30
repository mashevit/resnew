
"""
#prompt0 = """
"""To output the updated list with the corresponding habitat information in CSV format, you can use the following format:

Animal,Habitat
aardvark,1
antelope,2
bass,3
bear,4
boar,4
buffalo,2
calf,1
carp,3
catfish,3
cavy,2
cheetah,2
chicken,1
chub,3
clam,5
crab,5
crayfish,3
crow,1
deer,4
dogfish,6
dolphin,6
dove,1
duck,5
elephant,2
flamingo,5
flea,1
frog,3
fruitbat,4
giraffe,2
girl,1
gnat,1
goat,2
gorilla,4
gull,7
haddock,6
hamster,1
hare,2
hawk,1
herring,6
honeybee,1
housefly,1
kiwi,1
ladybird,1
lark,1
leopard,4
lion,2
lobster,5
lynx,4
mink,5
mole,8
mongoose,2
moth,1
newt,3
octopus,6
opossum,4
oryx,9
ostrich,2
parakeet,4
penguin,5
pheasant,2
pike,3
piranha,3
pitviper,1
platypus,5
polecat,4
pony,2
porpoise,6
puma,4
pussycat,1
raccoon,4
reindeer,10
rhea,2
scorpion,1
seahorse,6
seal,6
sealion,6
seasnake,6
seawasp,6
skimmer,7
skua,7
slowworm,1
slug,1
sole,6
sparrow,1
squirrel,4
starfish,6
stingray,6
swan,5
termite,1
toad,1
tortoise,1
tuatara,1
tuna,6
vampire,1
vole,2
vulture,1
wallaby,2
wasp,1
wolf,4
worm,1
wren,1

You can save this information in a CSV file, where the first row represents the column headers "Animal" and "Habitat", and each subsequent row represents the corresponding animal and its assigned numerical habitat value.
"""
#second header is/contains habitat. last breaking line.





# Input file name
input_file_name_output_csv = "../output/output.csv"  # Replace with your actual file name
input_file_name_feature1 = "../output/output_habitat"
input_file_name = ""
# Initialize a flag to indicate when to start and stop collecting attribute information
is_attribute_info = False
first = 0
# List to store attribute information lines
attribute_info_lines = []
i = 0
# Read the content of the input file
with open(input_file_name_output_csv, 'r') as file1:
    with open(input_file_name_feature1, 'r') as file2:
        for line in file1:
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

#open origin output csv and combine