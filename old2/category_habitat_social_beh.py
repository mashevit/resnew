import pandas as pd

social_df = pd.read_csv('concat/social_merged.csv')  # Replace with the path to your zoo CSV

type_col = social_df.pop('Type')
Category_Code_col = social_df.pop('Category Code')
test_df = pd.read_csv('concat/concat_num_habitat_copy.csv')
test_df['Category Code'] = Category_Code_col
test_df['Type'] = type_col
combined_csv_file = "concat/combined_data_fin0.csv"
test_df.to_csv(combined_csv_file, index=False)