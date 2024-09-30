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
    prompt1 = get_ans(prompt0)
   # print(f"ans = {prompt1}") #ans = animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, type
    prompt11 = "suggest me additional feature from external knowledge that can improve machine learning classification." #output only feature name for further processing.
    #One additional feature that could improve machine learning classification is "habitat." This feature can provide information about the natural environment or location where the animal is typically found. It can help in distinguishing between different types of animals based on their preferred habitats, such as forest, desert, grassland, or aquatic environments.

    prompt11_cont = "output only feature name as first and only phrase" #habitat
    prompt2 = f"I have dataset with the following features: {prompt1} {prompt11} {prompt11_cont}"#suggest me one additional feature from external knowledge that can improve machine learning classification. output only feature name for further processing."
    prompt3 = get_ans(prompt2)
   # print(prompt3)
    return prompt3


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