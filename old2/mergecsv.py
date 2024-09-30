import pandas as pd

# Input file paths
file1_path = 'animal_habitats_nums.csv'
file2_path = 'animal_habitats_nums2.csv'

# Load the CSV files into DataFrames
df1 = pd.read_csv(file1_path, header=None)
df2 = pd.read_csv(file2_path, header=None)

# Exclude the last column from the first DataFrame
df1 = df1.iloc[:, :-1]
# Using .iloc to print the first row
first_row_iloc = df1.iloc[0]
print("Using .iloc:")
print(first_row_iloc)
print()
# Exclude the first column from the second DataFrame
df2 = df2.iloc[:, 1:]
# Using .iloc to print the first row
first_row_iloc1 = df2.iloc[0]
print("Using .iloc:")
print(first_row_iloc1)
print()
# Merge the DataFrames horizontally (along columns)
merged_df = pd.concat([df1, df2], axis=1)
# Using .iloc to print the first row
first_row_iloc2 = merged_df.iloc[0]
print("Using .iloc:")
print(first_row_iloc2)
print()
# Output file path for the merged CSV
output_path = 'merged_file_habitat_nums.csv'

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_path, header=False, index=False)

print(f'Merged CSV saved to {output_path}')