import pandas as pd

social_df = pd.read_csv('social_merged.csv')  # Replace with the path to your zoo CSV

type_col = social_df.pop('Type')
test_df = pd.read_csv('combined_data.csv')

test_df['Type'] = type_col
combined_csv_file = "combined_data_fin0.csv"
test_df.to_csv(combined_csv_file, index=False)