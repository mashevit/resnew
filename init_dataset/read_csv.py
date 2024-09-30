import pandas as pd

def process_csv(file_path):

    # Path to the file
    #file_path = '../zoo/zoo.data'

    # Read the CSV file
    df = pd.read_csv(file_path, header=None)  # Assuming the file doesn't have a header row

    # Print the DataFrame
    print(df)

    first_three = df.iloc[0:101, 0]

    # Convert to string separated by ', '
    result_string = ', '.join(first_three)
    print(result_string)


def print_3(file_path):


    # Read the CSV file
    df = pd.read_csv(file_path, header=None)  # Assuming the file doesn't have a header row

    first_three = df.iloc[0:3, 0]

    # Convert to string separated by ', '
    result_string = ', '.join(first_three)
    return result_string
   # print(result_string)


process_csv('../zoo/zoo.data')