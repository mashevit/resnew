from mainer.mainer_1 import step1
from mainer.get_animals import step_2
from mainer.mainer_step_3 import *
from mainer.mainer_step_4 import step_4
from mainer.mainer_step_5 import step_5
from mainer.mainer_step_6 import step_6
from mainer.string_to_file import save_string_to_file
from mainer.create_sub_csv import extract_first_and_last_columns
from mainer2.step_7_caller import caller_almost_fin_2
import time
import os
import shutil
import os

# Function to copy a directory
def copy_directory(src, dst):
    # Remove the destination directory if it exists
    if os.path.exists(dst):
        print("jsjdfjsddsjkkjdskdj")
        #shutil.rmtree(dst)
        return
    # Copy the source directory to the destination
    shutil.copytree(src, dst)



class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.index = 0

    def elapsed_time(self):
        return time.time() - self.start_time

    def print_elapsed_time(self, message="Elapsed time"):
        self.index += 1
        print(f"{message} {self.index}: {self.elapsed_time():.2f} seconds")

def mainer_main(self,a=None):
    namenew = 'output_new3'
    current_directory = os.getcwd()
    print(f"asasasas = {current_directory}")
    #src_dir = current_directory+ '/zoo/'
    #dst_dir = current_directory + f'/{namenew}/zoo/'

    src_dir = os.path.join(current_directory, 'zoo')
    dst_dir = os.path.join(current_directory,f'{namenew}','zoo')#f'/{namenew}/zoo'


    # Copy the directory
    copy_directory(src_dir, dst_dir)
    current_directory = os.getcwd()
    print("Current working directory:11", current_directory)
    #os.chdir(a)
    timer = Timer()

    timer.print_elapsed_time()#1
    directory = "zoo/"
    file = directory + "zoo.names"
    #feature = "Color"\
        #step1(file)
    strfeatures = "Habitat, Diet, Social behavior, Lifespan, Reproduction, Size, Conservation status, Predation, Migration patterns, Communication"
    #strfeatures = "Reproduction"#todo: communication
    strfeatures.lower()
    substrings_array = strfeatures.split(', ')
    leng = len(substrings_array)
    timer.print_elapsed_time()#2
    #print(ans)#habitat
    file2 = directory + "zoo.data"
    #animal_list = step_2(file2)

    timer.print_elapsed_time()#3
    #print(ans2)
    """
    tmp = aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren
    aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren

    """
    animal_list = "aardvark, antelope, bass, bear, boar, buffalo, calf, carp, catfish, cavy, cheetah, chicken, chub, clam, crab, crayfish, crow, deer, dogfish, dolphin, dove, duck, elephant, flamingo, flea, frog, frog, fruitbat, giraffe, girl, gnat, goat, gorilla, gull, haddock, hamster, hare, hawk, herring, honeybee, housefly, kiwi, ladybird, lark, leopard, lion, lobster, lynx, mink, mole, mongoose, moth, newt, octopus, opossum, oryx, ostrich, parakeet, penguin, pheasant, pike, piranha, pitviper, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, rhea, scorpion, seahorse, seal, sealion, seasnake, seawasp, skimmer, skua, slowworm, slug, sole, sparrow, squirrel, starfish, stingray, swan, termite, toad, tortoise, tuatara, tuna, vampire, vole, vulture, wallaby, wasp, wolf, worm, wren"
    #feature = "habitat"
    for i in range(len(substrings_array)):
        j = 0
        while j <= 3:
            feature1 = substrings_array[i]
        
            ##### print statement(s) in important places between steps. with feature name.
            feature = feature1.lower()
            print(f"Processing element: {feature}")
            step3_0 = step3_1(feature,animal_list,10)
            timer.print_elapsed_time()#4
            step3_2 = step3_1_2(animal_list,step3_0)
            #step3_ans = step3(feature, animal_list)
            step3_ans = step3_2
            #### find top ten feature categories at most.
            #### match categories with animal list values.
            timer.print_elapsed_time()#5

            step4_ans = step_4(feature,step3_ans)
            #print(step4_ans)
            timer.print_elapsed_time()#6
            #step4_ans = "terrestrial, grassland, freshwater, forest, aquatic, marine, coastal, underground, desert, tundra"

            step5_ans = step_5(feature, step4_ans)
            timer.print_elapsed_time()#7
            #step5_ans =

            step6_ans = step_6(feature, step3_ans, step5_ans)
            #print(step6_ans)

            timer.print_elapsed_time()#8
            #step6_ans =
            #namenew = 'output3'
            directory_output = f"{namenew}/{feature}/"

            # Define the source and destination directories
            #src_dir = '../zoo/'
            #dst_dir = f'../{namenew}/zoo/'

            # Copy the directory
            #copy_directory(src_dir, dst_dir)
            file_1 = "raw_out"
            save_string_to_file(step6_ans, directory_output, file_1)
            file_shrink = "new_origin.csv"
            #destination_file = directory_output + "origin.csv"
            destination_file1 = directory_output + file_shrink

            extract_first_and_last_columns(file2,destination_file1)
            ans5 = caller_almost_fin_2(directory_output, file_shrink, file_1)
            if not ans5:
                print("hallucination probably accuracy")
                print("Condition met, repeating the loop on this element once more")
                j += 1
                
                timer.print_elapsed_time()#9
                continue
            
            timer.print_elapsed_time()#9
            break

            timer.print_elapsed_time()#9

