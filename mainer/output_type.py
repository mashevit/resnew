from init_dataset.read_csv import *
from openai_api.connect import *

#res = print_3('../zoo/zoo.data')
#print(f"out = {res}")


file_path = "../zoo/zoo.data"
with open(file_path, 'r') as file:
    # Step 2: Read the entire file content as a single string
    file_content = file.read()

prompt0 = f"I have the following csv: {file_content} output string with animal names (first column) separated by ', '"

prompt1 = get_ans(prompt0)

print(f"ans = {prompt1}")
#ans = aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren
