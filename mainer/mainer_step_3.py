
'''from openai_api.connect import *

prompt0 = 'habitat'
prompt1 = 'aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren'
prompt2 = f'I have csv {prompt1} as first column, suggest categorical values for attribute {prompt0}'
'''

#from init_dataset.read_csv import *
from openai_api.connect import *
'''
file_path = "../output/output.csv"
with open(file_path, 'r') as file:
    # Step 2: Read the entire file content as a single string
    file_content = file.read()
'''
#max_num = 8

def step3_1(feature, animal_list, maxnum):
    prompt_01_01 = f"I need top {feature} feature categories for list {animal_list}. strictly {feature} category names or values"
    #prompt_fin = f"{prompt_01_01} output not more than top {maxnum} {feature} categories for further dataset work"
    prompt_ans = get_ans(prompt_01_01)
    return prompt_ans


def step3_1_2(animal_list, categories):
    prompt0 = f"output pairs of values in csv format from {animal_list} list called here mainList. and matching category from {categories} for all mainList values. in order of mainList. output single most matching category with single each value in mainList"
    prompt_ans = get_ans(prompt0)
    return prompt_ans

def step3(feature, animal_list):
    #prompt00 = 'habitat'
    #prompt01 = "aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren"
    prompt_01_01 = f"I have following list of animals {animal_list}"

    num = 10
    prompt_num = f"generate single answer for each value in list. with no more than {num} different {feature} categories"
    prompt0_cont = f"for further improvement of classification dataset work. include not more than top {num} most prevalent feature categories for all list values. one feature per list value."
    prompt_mid = f"Output {feature} features {prompt0_cont}. output original list value with matching feature name"

    prompt2 = f"{prompt_01_01} {prompt_mid}"
    #prompt0 = f"I have the following csv {file_content}"
    #prompt_max_num = f"with not more than {max_num} values"
    prompt_only = f"Include {feature} only for animals in list"
    prompt_tmp_fin = f"{prompt2} {prompt_only}"
    #prompt11 = f"{prompt0} first column are animals, last column classes for machine learning classification"
    #prompt12 = f"{prompt11} output {prompt00} feature categorical values to improve classification {prompt0_cont} {prompt_max_num}"

    #print(prompt_tmp_fin)

    prompt1 = get_ans(prompt_tmp_fin)

    return prompt1

   # print(prompt1)


"""
1. Terrestrial: aardvark, antelope, bear, boar, buffalo, calf, catfish, cavy, cheetah, chicken, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flea, frog, frog, fruitbat, giraffe, gnat, goat, gorilla, hare, hawk, honeybee, housefly, ladybird, leopard, lion, lynx, mink, mole, mongoose, moth, newt, opossum, oryx, pheasant, puma, pussycat, raccoon, reindeer, scorpion, seal, sealion, skua, slowworm, slug, sole, sparrow, squirrel, starfish, termite, toad, tortoise, tuatara, vampire, vole, vulture, wasp, wolf, worm, wren.

2. Aquatic: bass, carp, catfish, chub, dolphin, haddock, herring, lobster, octopus, pike, piranha, seal, sealion, seasnake, seawasp, skimmer, sole, stingray, tuna.

3. Avian: chicken, crow, dove, flamingo, gull, hawk, kiwi, ladybird, lark, ostrich, parakeet, penguin, rhea, seahorse, skua, sparrow, swan, vulture, wren.

4. Amphibious: frog, newt, toad.

5. Arboreal: monkey, squirrel.

6. Burrowers: mole.

7. Desert: oryx.

8. Grassland: buffalo, calf, giraffe, goat, hare, lion, mongoose, pheasant, pony, reindeer, vole, wallaby.

9. Forest: bear, boar, deer, fruitbat, gorilla, leopard, lynx, mink, raccoon, squirrel, vampire, wolf.

10. Marine: dolphin, seal, sealion, stingray.

11. Polar: penguin, polar bear, seal, sealion.

12. Savanna: antelope, buffalo, giraffe, lion.

13. Tropical: cheetah, frog, gorilla, leopard, lion, monkey, mongoose, parakeet, puma, vampire.

These categorical values based on habitat features can help improve the classification of animals and provide a foundation for further dataset work.

Process finished with exit code 0
"""
"""
tmp4 = The last column in your dataset represents the habitat feature of each animal. These are categorical values that can be used to improve the classification of your machine learning model. 

Here's what each number might represent:

1. Land: This could include animals that primarily live on land, such as aardvarks, antelopes, bears, etc.
2. Air: This category could include birds and other animals that spend a significant amount of time in the air, such as chickens, crows, doves, etc.
3. Poisonous Land: This category could include poisonous animals that live on land, such as the pitviper.
4. Freshwater: This category could include fish and other animals that live in freshwater habitats, such as bass, carp, catfish, etc.
5. Amphibians: This category could include animals that can live both on land and in water, such as frogs and newts.
6. Insects: This category could include insects, such as fleas, honeybees, houseflies, etc.
7. Marine: This category could include animals that live in the sea, such as clams, crabs, crayfish, etc.

These categories can help your machine learning model to make more accurate predictions by providing additional context about each animal's habitat. However, it's important to note that these are just suggestions and the actual meaning of each category may vary depending on the specifics of your dataset.
The last column in your dataset represents the habitat feature of each animal. These are categorical values that can be used to improve the classification of your machine learning model. 

Here's what each number might represent:

1. Land: This could include animals that primarily live on land, such as aardvarks, antelopes, bears, etc.
2. Air: This category could include birds and other animals that spend a significant amount of time in the air, such as chickens, crows, doves, etc.
3. Poisonous Land: This category could include poisonous animals that live on land, such as the pitviper.
4. Freshwater: This category could include fish and other animals that live in freshwater habitats, such as bass, carp, catfish, etc.
5. Amphibians: This category could include animals that can live both on land and in water, such as frogs and newts.
6. Insects: This category could include insects, such as fleas, honeybees, houseflies, etc.
7. Marine: This category could include animals that live in the sea, such as clams, crabs, crayfish, etc.

These categories can help your machine learning model to make more accurate predictions by providing additional context about each animal's habitat. However, it's important to note that these are just suggestions and the actual meaning of each category may vary depending on the specifics of your dataset.

Process finished with exit code 0

"""


"""

1. Land: This could include animals that primarily live on land, such as aardvarks, antelopes, bears, etc.
2. Air: This category could include birds and other animals that spend a significant amount of time in the air, such as chickens, crows, doves, etc.
3. Poisonous Land: This category could include poisonous animals that live on land, such as the pitviper.
4. Freshwater: This category could include fish and other animals that live in freshwater habitats, such as bass, carp, catfish, etc.
5. Amphibians: This category could include animals that can live both on land and in water, such as frogs and newts.
6. Insects: This category could include insects, such as fleas, honeybees, houseflies, etc.
7. Marine: This category could include animals that live in the sea, such as clams, crabs, crayfish, etc.

These categories can help your machine learning model to make more accurate predictions by providing additional context about each animal's habitat. However, it's important to note that these are just suggestions and the actual meaning of each category may vary depending on the specifics of your dataset.
The last column in your dataset represents the habitat feature of each animal. These are categorical values that can be used to improve the classification of your machine learning model. 

Here's what each number might represent:

1. Land: This could include animals that primarily live on land, such as aardvarks, antelopes, bears, etc.
2. Air: This category could include birds and other animals that spend a significant amount of time in the air, such as chickens, crows, doves, etc.
3. Poisonous Land: This category could include poisonous animals that live on land, such as the pitviper.
4. Freshwater: This category could include fish and other animals that live in freshwater habitats, such as bass, carp, catfish, etc.
5. Amphibians: This category could include animals that can live both on land and in water, such as frogs and newts.
6. Insects: This category could include insects, such as fleas, honeybees, houseflies, etc.
7. Marine: This category could include animals that live in the sea, such as clams, crabs, crayfish, etc.

These categories can help your machine learning model to make more accurate predictions by providing additional context about each animal's habitat. However, it's important to note that these are just suggestions and the actual meaning of each category may vary depending on the specifics of your dataset.

Process finished with exit code 0
"""

"""
I have following list of animals aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren output habitat feature categorical values to improve classification for further dataset work Include habitat only for animals in list
tmp = To improve the classification for further dataset work, you can include the habitat feature as categorical values for the animals in the given list. Here is the updated list with the corresponding habitat information:

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
To improve the classification for further dataset work, you can include the habitat feature as categorical values for the animals in the given list. Here is the updated list with the corresponding habitat information:

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

Process finished with exit code 0


"""