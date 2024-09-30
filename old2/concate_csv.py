import pandas as pd

# Replace these file paths with your CSV file paths
file1 = 'animal_habitats_nums.csv'
file2 = 'animal_habitats_nums2.csv'

# Read the CSV files into DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Concatenate the DataFrames vertically (stacking one below the other)
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Specify the output file path for the concatenated CSV file
output_file = 'concatenated.csv'

# Save the concatenated DataFrame to a new CSV file
concatenated_df.to_csv(output_file, index=False)

print(f'Concatenated data saved to {output_file}')
