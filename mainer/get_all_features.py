#from init_dataset.read_csv import *
from openai_api.connect import *


def step1(filename):
    file_path = filename
    #"../zoo/zoo.names"
    with open(file_path, 'r') as file:
        # Step 2: Read the entire file content as a single string
        file_content = file.read()

    prompt0 = f"I have the following text:{file_content} output string with attribute headers separated by ', '"
   # print(f"I have the following text:{file_content} output string with attribute headers separated by ', '")
    """
    ChatCompletionMessage(content='animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, type', role='assistant', function_call=None, tool_calls=None)
    """
    prompt1 = "animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, type"

        #get_ans(prompt0)
   # print(f"ans = {prompt1}") #ans = animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, type
    prompt11 = "suggest me additional features from external knowledge that can improve machine learning classification." #output only feature name for further processing.
    #One additional feature that could improve machine learning classification is "habitat." This feature can provide information about the natural environment or location where the animal is typically found. It can help in distinguishing between different types of animals based on their preferred habitats, such as forest, desert, grassland, or aquatic environments.

    prompt11_cont = "output only feature name as first and only phrase" #habitat
    prompt2 = f"I have dataset with the following features: {prompt1} {prompt11}"#suggest me one additional feature from external knowledge that can improve machine learning classification. output only feature name for further processing."
    prompt3 = get_ans(prompt2)
   # print(prompt3)
    return prompt3


ans = step1("../zoo/zoo.names")
loop = 1
promptans = f"rewrite {ans} output string with feature names only. without numbers. separated by ', '"
featureans = get_ans(promptans)
substrings_array = featureans.split(', ')
leng = len(substrings_array)
print(f"Substrings array: {substrings_array} len = {leng}", )

"""

1. Diet (e.g. carnivore, herbivore, omnivore)
2. Habitat (e.g. forest, desert, ocean)
3. Lifespan
4. Social behavior (e.g. solitary, group-living)
5. Reproduction method (e.g. live birth, egg-laying)
6. Activity pattern (e.g. diurnal, nocturnal)
7. Body size
8. Conservation status
9. Intelligence level
10. Communication method (e.g. vocalizations, body language)
"""
"""
1. Habitat: This feature could provide valuable information about the natural environment of the animal, which could help in classification.

2. Diet: Knowing whether an animal is a herbivore, carnivore, or omnivore could be useful in distinguishing between different types of animals.

3. Lifespan: The average lifespan of an animal could be a useful feature in classification, as it could provide insight into the animal's characteristics and behavior.

4. Social behavior: Understanding whether an animal is solitary or social could help in classification, as social behavior can vary greatly between different species.

5. Reproduction: Information about the reproductive habits of an animal, such as mating rituals or gestation periods, could be a useful feature in classification.

6. Size: The size of an animal could be an important feature in classification, as it can vary greatly between different species and can provide valuable information about the animal's characteristics.

7. Conservation status: Knowing the conservation status of an animal could be a useful feature in classification, as it could provide insight into the animal's population size and habitat.

8. Predators: Information about the predators of an animal could be a useful feature in classification, as it could provide insight into the animal's behavior and adaptations for survival.
<function step1 at 0x000001ECBAADB760>

Process finished with exit code 0
"""
"""
1. Color: This feature can provide information about the color of the animal, which can be useful in distinguishing between different types.

2. Habitat: This feature can describe the natural environment or habitat in which the animal is typically found, such as forest, desert, or ocean.

3. Diet: This feature can indicate the primary food source of the animal, such as herbivore, carnivore, or omnivore.

4. Size: This feature can provide information about the size of the animal, which can be helpful in classification.

5. Social Behavior: This feature can describe the social behavior of the animal, such as solitary, group-living, or territorial.

6. Migration: This feature can indicate whether the animal migrates or not, which can be relevant for certain types of animals.

7. Nocturnal/Diurnal: This feature can describe whether the animal is active during the day (diurnal) or night (nocturnal).

8. Endangered Status: This feature can indicate whether the animal is classified as endangered, vulnerable, or not at risk.

9. Reproduction: This feature can describe the reproductive behavior of the animal, such as live birth or egg-laying.

10. Vocalizations: This feature can indicate whether the animal produces vocalizations or sounds, which can be distinctive for certain types.

11. Adaptations: This feature can describe any unique adaptations or specialized features of the animal, such as long neck, webbed feet, or camouflage.

12. Lifespan: This feature can provide information about the average lifespan of the animal, which can vary significantly between different types.

13. Speed: This feature can describe the speed or agility of the animal, which can be relevant for certain types.

14. Intelligence: This feature can indicate the level of intelligence or cognitive abilities of the animal, which can vary across species.

15. Migration Patterns: This feature can describe the specific migration patterns or routes followed by migratory animals.

16. Ecosystem Role: This feature can indicate the role or ecological niche that the animal plays within its ecosystem, such as pollinator, predator, or prey.

17. Conservation Status: This feature can provide information about the conservation status of the animal, such as whether it is protected or facing threats.

18. Life Cycle: This feature can describe the different stages or phases in the life cycle of the animal, such as larva, pupa, or adult.

19. Parental Care: This feature can indicate whether the animal exhibits parental care towards its offspring, such as nesting or feeding behaviors.

20. Communication: This feature can describe the communication methods or signals used by the animal, such as visual displays or chemical signals.

Process finished with exit code 0
"""

"""
tmp = 1. Diet (e.g. carnivore, herbivore, omnivore)
2. Habitat (e.g. forest, desert, ocean)
3. Lifespan
4. Social behavior (e.g. solitary, group-living)
5. Reproduction method (e.g. live birth, egg-laying)
6. Activity pattern (e.g. diurnal, nocturnal)
7. Body size
8. Conservation status
9. Geographic distribution
10. Predation risk
11. Communication methods (e.g. vocalizations, visual displays)
12. Metabolic rate
13. Adaptations for specific environments (e.g. camouflage, burrowing)
tmp = Diet, Habitat, Lifespan, Social behavior, Reproduction method, Activity pattern, Body size, Conservation status, Geographic distribution, Predation risk, Communication methods, Metabolic rate, Adaptations for specific environments
Substrings array: ['Diet', 'Habitat', 'Lifespan', 'Social behavior', 'Reproduction method', 'Activity pattern', 'Body size', 'Conservation status', 'Geographic distribution', 'Predation risk', 'Communication methods', 'Metabolic rate', 'Adaptations for specific environments'] len = 13

Process finished with exit code 0

"""