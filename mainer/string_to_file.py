import os


def save_string_to_file(input_string, directory_name, filename_in):
    # Specify the directory name you want to create
    # directory_name = "my_directory"

    # Check if the directory already exists, and create it if it doesn't
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")
    try:
        filename = directory_name + filename_in
        with open(filename, 'w') as file:
            file.write(input_string)
        #print(f'String has been successfully saved to {filename}')
    except Exception as e:
        print(f'Error: {e}')

"""
string = To output the updated list with the corresponding habitat information in CSV format, you can use the following format:

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

#save_string_to_file(string,f"../output/output_{string00}")