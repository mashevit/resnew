from mainer.string_to_file import save_string_to_file


def func_for_two_files(file1_inp, file2, ind, directory_path1):
   # directory_path1 = '../output/'
    final_string = ""
    line_num = 1
    file_name_in = f"out{ind}_combined"
    file_path = directory_path1 + file_name_in
    with open(file1_inp, 'r') as file11, open(file2, 'r') as file22:
        unique_lines = set()
        for line15, line25 in zip(file11, file22):
            s41 = line15.split(",")[0]
            prev_main_attr = s41
            if line25.strip() == "":
                save_string_to_file(final_string, directory_path1, file_name_in)
                #print(f"{final_string} \n line = {line_num}")
                return file_path, -1
            if line15.strip() == "":
               # file_path = directory_path1+f"out{ind}_two"
                save_string_to_file(final_string, directory_path1, file_name_in)
                #print(f"{final_string} \n line = {line_num}")
                return file_path, -2
            if s41 in unique_lines:
                #duplicate_lines.append(stripped_line)
              #  file_path = directory_path1+f"out{ind}_two"
                save_string_to_file(final_string, directory_path1, file_name_in)
                #print(f"{final_string} \n line = {line_num}")
                return file_path, line_num
            else:
                unique_lines.add(s41)
                line_num += 1
            s22 = line25.split(",")[1].strip()
            s33 = line15.split(",")[1].strip()
            #print(f"ans11 = {s41},{s22},{s33}")
            #     existing = final_string
            #  new = f"{s41},{s22},{s33}"
            # final_string = f"{existing}\n{new}"
            strnew = f"{s41},{s22},{s33}\n"
            final_string += strnew
     #   file_path = directory_path1 + f"out{ind}_two"
        save_string_to_file(final_string, directory_path1, file_name_in)
        # print(f"{final_string} \n line = {line_num}")
        return file_path, -3
   # print(final_string)

#goes wrong in double frog entry, return saved file name until first, from habitat also cut, until frog, leave frog.
'''

string00 = "habitat"
num_cut = 1
directory_path = '../output/'
file1 = directory_path + f"output_{string00}"
file0 = directory_path + "output.csv"
file_out = directory_path + f"out_cut_{num_cut}"
func_for_two_files(file0, file_out)
#line = 27
'''
import pandas as pd
from io import StringIO 
def check(file1, file2, dir, filenameout, finalout): #out should be out1
    # Load the first CSV file into a DataFrame
    file1f = dir + file1
    file2f = dir + file2
    df1 = pd.read_csv(file1f, header=None)

    # Read the second file and split into lines
    with open(file2f, 'r') as file:
        lines = file.readlines()

    # Identify the CSV part in the second file
    csv_lines = []
    non_csv_lines = []
    csv_part = True
    #num = 0
    for num, line in enumerate(lines):
        #s41 = line.split(",")[0]
   # Check if we are still within the CSV rows from the first file
        if num >= len(df1):
            break
        first_value = line.split(",")[0].strip()
    #    if num < len(df1):
        # Compare the first value with the corresponding value in the first column of the CSV
        st = str(df1.iloc[num, 0])
        if first_value != st:
            print(f"fir = {first_value} df = {st},num= {num}")
            return False, None, None
            print(f"Mismatch at line {num + 1}: {first_value} != {df1.iloc[num, 0]}")
            break             
        if csv_part and line.strip():  # If it is part of the CSV section
            csv_lines.append(line)
        else:  # Once the non-CSV part is detected
            csv_part = False
            non_csv_lines.append(line)
        #num += 1

    # Convert the CSV lines to a DataFrame

    csv_content = ''.join(csv_lines)
    df2 = pd.read_csv(StringIO(csv_content))
    '''
    # Ensure both DataFrames have the same first column values
    if (df1.iloc[:, 0] == df2.iloc[:, 0]).all():
        # Copy the first column from the first file to the second DataFrame
        df2.iloc[:, 0] = df1.iloc[:, 0]
    else:
        print("The first columns of the two files do not match.")
    '''
    # Save the modified CSV part back to a string
    modified_csv_content = df2.to_csv(index=False, sep=',')

    # Combine the modified CSV part with the non-CSV part
    #modified_content = modified_csv_content + ''.join(non_csv_lines)
    file_path = dir + filenameout
    # Write the modified content to a new file
    with open(file_path, 'w') as file:
        file.write(modified_csv_content)



        # Extract the second column from df1
    second_column_df1 = df1.iloc[:, 1]

    # Rename the second column to avoid column name conflicts
    #second_column_df1 = second_column_df1.rename('New_Column')

    # Add the second column from df1 to the last column of df2
    df2 = pd.concat([df2, second_column_df1], axis=1, ignore_index=True)

    #print(df2)

    modified_csv_content1 = df2.to_csv(index=False,  header=False, sep=',')

    # Combine the modified CSV part with the non-CSV part
    #modified_content = modified_csv_content + ''.join(non_csv_lines)
    file_path1 = dir + finalout
    # Write the modified content to a new file
    with open(file_path1, 'w') as file:
        file.write(modified_csv_content1)

    return True, file_path, file_path1

    print("The second file has been modified and saved as 'modified_file2.txt'.")