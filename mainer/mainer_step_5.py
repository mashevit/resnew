from openai_api.connect import *


def step_5(feature, step_4_out):
   # prompt2 = "terrestrial, grassland, freshwater, forest, aquatic, marine, coastal, underground, desert, tundra"
    prompt3 = f"give categorical numerical numbers to the following {feature} feature "
    prompt3_cont = "to add to machine learning classification task in dataset"
    prompt4 = f"{prompt3} {step_4_out} {prompt3_cont}"

    prompt5 = get_ans(prompt4)
    return prompt5
    #prompt00 = "habitat"


"""
tmp = To add categorical numerical numbers to the given habitat features for a machine learning classification task, you can assign unique numerical values to each category. Here's one possible mapping:

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

Process finished with exit code 0

"""