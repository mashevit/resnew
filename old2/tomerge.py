import pandas as pd

zoo_df = pd.read_csv('Datasets/zoo_df_col.csv')
'''
zoo_df = pd.read_csv('Datasets/zoo.csv', header=None)  # Replace with the path to your zoo CSV
social_behavior_df = pd.read_csv('Datasets/221.csv', header=None)  # Replace with the path to your social behavior CSV


#zoo_df.columns = ['Animal Name', 'Feature1', 'Feature2', ...]  # Replace with actual feature names
social_behavior_df.columns = ['Animal Name', 'Social Behavior']

zoo_df.columns = [
    'Animal Name',  # Unique name for each animal
    'Hair',         # Boolean indicating presence of hair
    'Feathers',     # Boolean indicating presence of feathers
    'Eggs',         # Boolean indicating whether the animal lays eggs
    'Milk',         # Boolean indicating whether the animal produces milk
    'Airborne',     # Boolean indicating if the animal can fly
    'Aquatic',      # Boolean indicating if the animal is aquatic
    'Predator',     # Boolean indicating if the animal is a predator
    'Toothed',      # Boolean indicating presence of teeth
    'Backbone',     # Boolean indicating presence of a backbone
    'Breathes',     # Boolean indicating if the animal breathes air
    'Venomous',     # Boolean indicating if the animal is venomous
    'Fins',         # Boolean indicating presence of fins
    'Legs',         # Numeric indicating the number of legs (0, 2, 4, 5, 6, 8)
    'Tail',         # Boolean indicating presence of a tail
    'Domestic',     # Boolean indicating if the animal is typically domesticated
    'Catsize',      # Boolean indicating if the animal is the size of a cat or larger
    'Type'          # Numeric type classification (integer values in range [1,7])
]

zoo_df.to_csv('Datasets/zoo_df_col.csv', index=False)
social_behavior_df.to_csv('Datasets/social_behavior_df_col.csv', index=False)
# Assuming 'Animal Name' is the common column in both CSV files
'''
'''
zoo_df = pd.read_csv('Datasets/zoo_df_col.csv')  # Replace with the path to your zoo CSV
type_col = zoo_df.pop('Type')
social_behavior_df = pd.read_csv('Datasets/behace_num.csv')  # Replace with the path to your social behavior CSV
'''
'''
zoo_df = pd.read_csv('Datasets/zoo_df_col.csv')
print("11")
# Converting the lists in 'column_name' to space-separated strings
zoo_df['Animal Name'] = zoo_df['Animal Name'].apply(' '.join)

# Output the column
print(zoo_df['Animal Name'])

print("22")

combined_string = ""

# Loop through each row in the DataFrame
for item in zoo_df['Animal Name']:
    combined_string += item + " "

# Remove the trailing space
combined_string = combined_string.strip()

print(combined_string)
'''
print("33")
str_com1 = ' '.join(zoo_df['Animal Name'].tolist())

print(str_com1)
'''
#zoo_df['Animal Name'] = zoo_df['Animal Name'].apply(' '.join)


print("qw")
combined_string = zoo_df['Animal Name'].str.cat(sep=' ')

print(combined_string)
'''

'''
# Output the column
print("44")
print(zoo_df['Animal Name'])
#beh_col=social_behavior_df.pop('Category Code')
#zoo_df['Category Code'] = beh_col
social_behavior_df.pop('No')
social_behavior_df['Type'] = type_col

#merged_df = pd.merge(zoo_df, social_behavior_df, on='Animal Name', how='left')

#social_behavior_df.to_csv('social_merged.csv', index=False)

'''