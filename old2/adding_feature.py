import pandas as pd

social_df = pd.read_csv('social_merged.csv')  # Replace with the path to your zoo CSV
categ_col = social_df.pop('Category Code')
type_col = social_df.pop('Type')
test_df = pd.read_csv('concat2/33')
test_df['Category Code'] = categ_col
test_df['Type'] = type_col
combined_csv_file = "concat2/combined_data_fin11.csv"
test_df.to_csv(combined_csv_file, index=False)
