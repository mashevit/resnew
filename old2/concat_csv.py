import pandas as pd

# Specify the file paths for the two CSV files
#first_csv_file = "animal_habitats.csv"
#second_csv_file = "animal_habitats1.csv"

first_csv_file = 'animal_habitats_nums.csv'
second_csv_file = 'animal_habitats_nums2.csv'

# Read the first CSV file into a DataFrame
first_df = pd.read_csv(first_csv_file)

# Read the second CSV file into a DataFrame, selecting only the desired columns
columns_to_include = first_df.columns.tolist()

second_df = pd.read_csv(second_csv_file, usecols=columns_to_include)

# Concatenate the two DataFrames vertically to combine the data
combined_df = pd.concat([first_df, second_df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_csv_file = "concat_num_habitat.csv"
combined_df.to_csv(combined_csv_file, index=False)

print(f"Data from '{second_csv_file}' has been added to '{first_csv_file}' and saved to '{combined_csv_file}'.")
