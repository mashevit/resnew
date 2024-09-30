from mainer.mainer_1 import step1
from mainer.get_animals import step_2
from mainer.mainer_step_3 import step3
from mainer.mainer_step_4 import step_4
from mainer.mainer_step_5 import step_5
from mainer.mainer_step_6 import step_6
from mainer.string_to_file import save_string_to_file
from mainer.create_sub_csv import extract_first_and_last_columns
from mainer2.step_7_caller import caller_almost_fin_2
import time


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.index = 0

    def elapsed_time(self):
        return time.time() - self.start_time

    def print_elapsed_time(self, message="Elapsed time"):
        self.index += 1
        print(f"{message} {self.index}: {self.elapsed_time():.2f} seconds")


timer = Timer()

timer.print_elapsed_time()
directory = "../zoo/"
file = directory + "zoo.names"
feature = "Color"\
    #step1(file)
strfeatures = "Habitat, Diet, Social behavior, Lifespan, Reproduction, Size, Conservation status, Predation, Migration patterns, Communication"
substrings_array = strfeatures.split(', ')
leng = len(substrings_array)
timer.print_elapsed_time()
#print(ans)#habitat
file2 = directory + "zoo.data"
animal_list = step_2(file2)

timer.print_elapsed_time()
#print(ans2)
"""
tmp = aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren
aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren

"""
#animal_list = "aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren"
#feature = "habitat"

step3_ans = step3(feature, animal_list)
timer.print_elapsed_time()
#print(step3_ans)

#step3_ans =
"""To improve the classification for further dataset work, you can include the habitat feature as categorical values for the animals in the given list. Here is the updated list with the corresponding habitat information:

aardvark - terrestrial
antelope - grassland
bass - freshwater
bear - forest
boar - forest
buffalo - grassland
calf - terrestrial
carp - freshwater
catfish - freshwater
cavy - grassland
cheetah - grassland
chicken - terrestrial
chub - freshwater
clam - aquatic
crab - aquatic
crayfish - freshwater
crow - terrestrial
deer - forest
dogfish - marine
dolphin - marine
dove - terrestrial
duck - aquatic
elephant - grassland
flamingo - aquatic
flea - terrestrial
frog - freshwater
fruitbat - forest
giraffe - grassland
girl - terrestrial
gnat - terrestrial
goat - grassland
gorilla - forest
gull - coastal
haddock - marine
hamster - terrestrial
hare - grassland
hawk - terrestrial
herring - marine
honeybee - terrestrial
housefly - terrestrial
kiwi - terrestrial
ladybird - terrestrial
lark - terrestrial
leopard - forest
lion - grassland
lobster - aquatic
lynx - forest
mink - aquatic
mole - underground
mongoose - grassland
moth - terrestrial
newt - freshwater
octopus - marine
opossum - forest
oryx - desert
ostrich - grassland
parakeet - forest
penguin - aquatic
pheasant - grassland
pike - freshwater
piranha - freshwater
pitviper - terrestrial
platypus - aquatic
polecat - forest
pony - grassland
porpoise - marine
puma - forest
pussycat - terrestrial
raccoon - forest
reindeer - tundra
rhea - grassland
scorpion - terrestrial
seahorse - marine
seal - marine
sealion - marine
seasnake - marine
seawasp - marine
skimmer - coastal
skua - coastal
slowworm - terrestrial
slug - terrestrial
sole - marine
sparrow - terrestrial
squirrel - forest
starfish - marine
stingray - marine
swan - aquatic
termite - terrestrial
toad - terrestrial
tortoise - terrestrial
tuatara - terrestrial
tuna - marine
vampire - terrestrial
vole - grassland
vulture - terrestrial
wallaby - grassland
wasp - terrestrial
wolf - forest
worm - terrestrial
wren - terrestrial

By including the habitat information, you can now use it as a feature for classification tasks or further analysis on the dataset.
"""

step4_ans = step_4(feature,step3_ans)
#print(step4_ans)
timer.print_elapsed_time()
#step4_ans = "terrestrial, grassland, freshwater, forest, aquatic, marine, coastal, underground, desert, tundra"

step5_ans = step_5(feature, step4_ans)
timer.print_elapsed_time()
#step5_ans =
"""To add categorical numerical numbers to the given habitat features for a machine learning classification task, you can assign unique numerical values to each category. Here's one possible mapping:

1. Terrestrial: 1
2. Grassland: 2
3. Freshwater: 3
4. Forest: 4
5. Aquatic: 5
6. Marine: 6
7. Coastal: 7
8. Underground: 8
9. Desert: 9
10. Tundra: 10

By assigning numerical values to the habitat features, you can represent them in a format that can be used by machine learning algorithms for classification tasks."""

step6_ans = step_6(feature, step3_ans, step5_ans)
#print(step6_ans)

timer.print_elapsed_time()
#step6_ans =
"""
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

You can save this information in a CSV file format for further analysis or use in machine learning algorithms.

Process finished with exit code 0

"""
directory_output = f"../output_{feature}/"
file_1 = "raw_out"
save_string_to_file(step6_ans, directory_output, file_1)
file_shrink = "new_origin.csv"
#destination_file = directory_output + "origin.csv"
destination_file1 = directory_output + file_shrink

extract_first_and_last_columns(file2,destination_file1)
caller_almost_fin_2(directory_output, file_shrink, file_1)

timer.print_elapsed_time()


