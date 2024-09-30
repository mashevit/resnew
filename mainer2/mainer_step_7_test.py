# Input file name

from mainer.string_to_file import *
from mainer2.cut_file_from_ln import cut_lines


def step_7_1(input_file_name_output_csv, input_file_name_feature1, output_cut_1):

    '''  = "habitat"
    num_csv = 1
    input_file_name_output_csv = "../output/output_wrong.csv"  # Replace with your actual file name
    input_file_name_feature1 = f"../output/output_{string00}"
    output_cut_1 = f"../output/cut_{string00}_csv_{num_csv}"
    '''
    first = 0
    # List to store attribute information lines
    attribute_info_lines = []
    i = 0
    # Read the content of the input file
    with open(input_file_name_output_csv, 'r') as file1:
        with open(input_file_name_feature1, 'r') as file2:
            i = 0  # Initialize a counter for lines
            for line in file1:
                s = line.split(",")[0]
               # print(f"ans = {s}")  # You should print the value of 's' here
                j = 1
                for line2 in file2:
                    s1 = line2.split(",")[0]
                    if s1 != s:
                        j += 1

                    else:
                        print("here")
                        cut_lines(input_file_name_feature1, output_cut_1, j)
                        break
                break
    # Open the source file for reading
    with open(input_file_name_feature1, 'r') as source_file:
        # Read the contents of the source file
        source_contents = source_file.read()

        # Open the destination file for writing
        with open(output_cut_1, 'w') as destination_file:
            # Write the contents to the destination file
            destination_file.write(source_contents)
'''
#step_7_1("../output/output.csv","../output/out5","../output/out512")
current_directory = os.getcwd()
print("Current working directory:", current_directory)
new_directory = current_directory + "/mainer"
os.chdir(new_directory)

feature = "Habitat"
dir_out_2 = f"../output_{feature}/"
file_dataset = "new_origin.csv"
raw = "raw_out"
out_cut_1_with_dir = dir_out_2 + "out1"
step_7_1(dir_out_2 + file_dataset, dir_out_2 + raw, out_cut_1_with_dir)


'''
'''           print(f"j = {j}")
            jj = 0
            with open(input_file_name_output_csv, 'r') as file11, open(input_file_name_feature1, 'r') as file22:
                for line15, line25 in zip(file1, file2):
                    if jj != j:
                        jj += 1
                    else:
                        s41 = line15.split(",")[0]
                        s22 = line25.split(",")[1].strip()
                        s33 = line15.split(",")[1].strip()
                        print(f"ans11 = {s41},{s22},{s33}")
                        final_string = final_string + f"{s41},{s22},{s33}\n"
                        # Process lines from both files simultaneously
#                        line1 = line1.strip()  # Remove leading/trailing whitespace
              #          line2 = line2.strip()  # Remove leading/trailing whitespace

                    # Do something with line1 and line2, e.g., print them
                    #print(f'File 1: {line1}')
                   # print(f'File 2: {line2}')
            break
'''
'''
            else:
                print("23")
                with open(input_file_name_output_csv, 'r') as file3:
                    for line3 in file3:
                        s4 = line3.split(",")[0]
                        s2 = line2.split(",")[1].strip()
                        s3 = line3.split(",")[1].strip()
                        print(f"ans11 = {s4},{s2},{s3}")
                        final_string = final_string + f"{s4},{s2},{s3}\n"
                        first = 1
                break

'''
#print(final_string)

'''
        if is_attribute_info:
            print(line.strip())
            # Collect lines until an empty line is encountered (end of attribute information)
            if first >= 3:
                if not line.strip():
                    break
                attribute_info_lines.append(line.strip())
            first += 1
        elif "Attribute" in line:
            is_attribute_info = True
            first = 1
            #save_string_to_file(final_string,f"../output/output_{string00}_combined")

wrong:

String has been successfully saved to ../output/output_habitat
ans = aardvark
23
ans11 = aardvark,1,5
ans11 = antelope,1,1
ans11 = bass,1,4
ans11 = bear,1,1
ans11 = boar,1,1
ans11 = buffalo,1,1
ans11 = calf,1,1
ans11 = carp,1,4
ans11 = catfish,1,4
ans11 = cavy,1,1
ans11 = cheetah,1,1
ans11 = chicken,1,2
ans11 = chub,1,4
ans11 = clam,1,7
ans11 = crab,1,7
ans11 = crayfish,1,7
ans11 = crow,1,2
ans11 = deer,1,1
ans11 = dogfish,1,4
ans11 = dolphin,1,1
ans11 = dove,1,2
ans11 = duck,1,2
ans11 = elephant,1,1
ans11 = flamingo,1,2
ans11 = flea,1,6
ans11 = frog,1,5
ans11 = frog,1,5
ans11 = fruitbat,1,1
ans11 = giraffe,1,1
ans11 = girl,1,1
ans11 = gnat,1,6
ans11 = goat,1,1
ans11 = gorilla,1,1
ans11 = gull,1,2
ans11 = haddock,1,4
ans11 = hamster,1,1
ans11 = hare,1,1
ans11 = hawk,1,2
ans11 = herring,1,4
ans11 = honeybee,1,6
ans11 = housefly,1,6
ans11 = kiwi,1,2
ans11 = ladybird,1,6
ans11 = lark,1,2
ans11 = leopard,1,1
ans11 = lion,1,1
ans11 = lobster,1,7
ans11 = lynx,1,1
ans11 = mink,1,1
ans11 = mole,1,1
ans11 = mongoose,1,1
ans11 = moth,1,6
ans11 = newt,1,5
ans11 = octopus,1,7
ans11 = opossum,1,1
ans11 = oryx,1,1
ans11 = ostrich,1,2
ans11 = parakeet,1,2
ans11 = penguin,1,2
ans11 = pheasant,1,2
ans11 = pike,1,4
ans11 = piranha,1,4
ans11 = pitviper,1,3
ans11 = platypus,1,1
ans11 = polecat,1,1
ans11 = pony,1,1
ans11 = porpoise,1,1
ans11 = puma,1,1
ans11 = pussycat,1,1
ans11 = raccoon,1,1
ans11 = reindeer,1,1
ans11 = rhea,1,2
ans11 = scorpion,1,7
ans11 = seahorse,1,4
ans11 = seal,1,1
ans11 = sealion,1,1
ans11 = seasnake,1,3
ans11 = seawasp,1,7
ans11 = skimmer,1,2
ans11 = skua,1,2
ans11 = slowworm,1,3
ans11 = slug,1,7
ans11 = sole,1,4
ans11 = sparrow,1,2
ans11 = squirrel,1,1
ans11 = starfish,1,7
ans11 = stingray,1,4
ans11 = swan,1,2
ans11 = termite,1,6
ans11 = toad,1,5
ans11 = tortoise,1,3
ans11 = tuatara,1,3
ans11 = tuna,1,4
ans11 = vampire,1,1
ans11 = vole,1,1
ans11 = vulture,1,2
ans11 = wallaby,1,1
ans11 = wasp,1,6
ans11 = wolf,1,1
ans11 = worm,1,7
ans11 = wren,1,2
aardvark,1,5
antelope,1,1
bass,1,4
bear,1,1
boar,1,1
buffalo,1,1
calf,1,1
carp,1,4
catfish,1,4
cavy,1,1
cheetah,1,1
chicken,1,2
chub,1,4
clam,1,7
crab,1,7
crayfish,1,7
crow,1,2
deer,1,1
dogfish,1,4
dolphin,1,1
dove,1,2
duck,1,2
elephant,1,1
flamingo,1,2
flea,1,6
frog,1,5
frog,1,5
fruitbat,1,1
giraffe,1,1
girl,1,1
gnat,1,6
goat,1,1
gorilla,1,1
gull,1,2
haddock,1,4
hamster,1,1
hare,1,1
hawk,1,2
herring,1,4
honeybee,1,6
housefly,1,6
kiwi,1,2
ladybird,1,6
lark,1,2
leopard,1,1
lion,1,1
lobster,1,7
lynx,1,1
mink,1,1
mole,1,1
mongoose,1,1
moth,1,6
newt,1,5
octopus,1,7
opossum,1,1
oryx,1,1
ostrich,1,2
parakeet,1,2
penguin,1,2
pheasant,1,2
pike,1,4
piranha,1,4
pitviper,1,3
platypus,1,1
polecat,1,1
pony,1,1
porpoise,1,1
puma,1,1
pussycat,1,1
raccoon,1,1
reindeer,1,1
rhea,1,2
scorpion,1,7
seahorse,1,4
seal,1,1
sealion,1,1
seasnake,1,3
seawasp,1,7
skimmer,1,2
skua,1,2
slowworm,1,3
slug,1,7
sole,1,4
sparrow,1,2
squirrel,1,1
starfish,1,7
stingray,1,4
swan,1,2
termite,1,6
toad,1,5
tortoise,1,3
tuatara,1,3
tuna,1,4
vampire,1,1
vole,1,1
vulture,1,2
wallaby,1,1
wasp,1,6
wolf,1,1
worm,1,7
wren,1,2


Process finished with exit code 0
'''


