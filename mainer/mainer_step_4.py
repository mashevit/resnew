from openai_api.connect import *


def step_4(feature, step_3_ans):
    #feature = "habitat"

    prompt1 = f"extract and output only {feature} names from following text : extract {feature} categories from following text"
    prompt2 = f"{prompt1} {step_3_ans}"

    prompt3 = get_ans(prompt2)
    return prompt3
  #  print(prompt3)

#tmp = terrestrial, grassland, freshwater, forest, aquatic, marine, coastal, underground, desert, tundra
#terrestrial, grassland, freshwater, forest, aquatic, marine, coastal, underground, desert, tundra

'''  prompt0 = """To improve the classification for further dataset work, you can include the habitat feature as categorical values for the animals in the given list. Here is the updated list with the corresponding habitat information:

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
  #prompt_del = "delimiter"'''

