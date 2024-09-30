from openai_api.connect import *


def step_6(feature,step3_ans, step5_ans):
    prompt00 = "answer"
    prompt0 = f"and output first column in {prompt00} and number in csv format"

    prompt2 = f"Change {feature} feature name in {prompt00}  = {step3_ans} to number from {step5_ans} {prompt0}"
    prompt3 = get_ans(prompt2)
    return prompt3


"""
To add categorical numerical numbers to the given habitat features for a machine learning classification task, you can assign unique numerical values to each category. Here's one possible mapping:

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

By assigning numerical values to the habitat features, you can represent them in a format that can be used by machine learning algorithms for classification tasks.


"""


#prompt1 =
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

By including the habitat information, you can now use it as a feature for classification tasks or further analysis on the dataset."""
"""
prompt2 = f"change {prompt00} name in {prompt1} to number from {prompt0} and output in csv format"

prompt3 = get_ans(prompt2)
print(prompt3)
"""

"""tmp = To output the updated list with the corresponding habitat information in CSV format, you can use the following format:

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
To output the updated list with the corresponding habitat information in CSV format, you can use the following format:

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

Process finished with exit code 0

"""