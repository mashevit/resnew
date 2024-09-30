import pandas as pd

# Define the list of animals
animals = [
    "aardvark", "antelope", "bass", "bear", "boar", "buffalo", "calf", "carp", "catfish", "cavy",
    "cheetah", "chicken", "chub", "clam", "crab", "crayfish", "crow", "deer", "dogfish", "dolphin",
    "dove", "duck", "elephant", "flamingo", "flea", "frog", "frog", "fruitbat", "giraffe", "girl",
    "gnat", "goat", "gorilla", "gull", "haddock", "hamster", "hare", "hawk", "herring", "honeybee",
    "housefly", "kiwi", "ladybird", "lark", "leopard", "lion", "lobster", "lynx", "mink", "mole"
]

# Define the corresponding habitat feature for each animal (categorical column with numerical values)
habitat_features = [
    4, 4, 2, 1, 1, 4, 4, 3, 3, 4,
    4, 7, 3, 2, 2, 3, 7, 1, 3, 3,
    7, 7, 1, 4, 6, 3, 3, 4, 4, 4,
    7, 4, 7, 7, 1, 7, 1, 4, 1, 2,
    6, 6, 5, 5, 4, 7, 7, 7, 1, 1,
    2, 7, 7, 1, 1, 3, 1, 1
]

# Define the mapping of numerical values to categories
habitat_categories = {
    1: "Forest",
    2: "Desert",
    3: "Ocean",
    4: "Freshwater",
    5: "Grassland",
    6: "Tundra",
    7: "Urban",
    8: "Mountain"
}

# Map numerical values to habitat category names
habitat_feature_names = [habitat_categories[value] for value in habitat_features]

# Create a DataFrame
df = pd.DataFrame({'Animal': animals, 'Habitat': habitat_feature_names})

# Display the DataFrame
print(df)
