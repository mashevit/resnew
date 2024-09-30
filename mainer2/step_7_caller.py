from mainer2.mainer_step_7_test import step_7_1
from mainer2.with_two_files import func_for_two_files,check
from mainer2.cut_file_from_ln import cut_lines
from mainer2.merge_combined import append_text_files
from mainer2.accuracy_ml import ml_alg
#from mainer2.mainer_step_7_test import  step_7_1
import pandas as pd
#get initial cut fromchat answer
def step1_1():
    string00 = "habitat"
    num_cut = 1
    directory_path = '../output/'
    file1 = directory_path + f"output_{string00}"
    file0 = directory_path + "output.csv"
    file_out = directory_path + f"out_cut_{num_cut}"
    #print(file1)
    step_7_1(file0, file1, file_out)

#get first half of end file


def step1_2(directory_path3, new_origin, out1):
  #  num_cut = 1
    #directory_path3 = '../output/'
    file02 = directory_path3 + new_origin
    #file_out1 = directory_path3 + f"out_cut_{num_cut}"
    ans = func_for_two_files(file02, out1, 1, directory_path3)

    #print(f"ans  =  {ans}")
    return ans

#cut to meet frog demand


def step1_3(inp_file_origin, inp_file_other, line, dir):
    num_cut = 2
   # directory_path1 = '../output/'
    file1 = dir + f"out_cut_{num_cut}_0"
    file2 = dir + f"out_cut_{num_cut}_1"
    cut_lines(inp_file_origin, file1, line)
    cut_lines(inp_file_other, file2, line - 1)
   # print(f"gf1 = {file1} f2 = {file2}")
    return file1, file2

#return line num for second iteration


def caller_almost_fin(directory_path, file_output_csv, out_base):
    num_cut1 = 1
    #directory_path = '../output/'
    #file1 = directory_path + f"output_{string00}"
   # file0 = directory_path + file_output_csv
           # "output.csv"
    out_name, line_num = step1_2(directory_path, file_output_csv, out_base)
    file1 = out_base #####check how file got here ## already with directory
    print(file_output_csv)
    return step1_3(directory_path + file_output_csv, file1, line_num, directory_path), out_name


#second iteration

def caller_almost_fin_2(dir_out_2, file_dataset, raw):
    out_cut_1_with_dir = dir_out_2 + "out1"
    # step_7_1("../output/output.csv","../output/out5","../output/out51")
    step_7_1(dir_out_2 + file_dataset, dir_out_2 + raw, out_cut_1_with_dir)
    print(file_dataset)
    a, b, c = check(file_dataset, "out1", dir_out_2, "checked", "out1_combined")
    if a:
        print(f"a = {a} b = {b} c = {c}")

        df1 = pd.read_csv(dir_out_2 + file_dataset)
        df2 = pd.read_csv(c)


        # Check if the first columns are identical
        test1 = df1.iloc[:, 0].equals(df2.iloc[:, 0])

        # Check if the second and third columns in the second file are of integer type
        test2 = df2.iloc[:, 1].dtype == 'int' and df2.iloc[:, 2].dtype == 'int'

        #print("First column identical:", first_column_identical)
        #print("Second and third columns in second file are integers:", second_and_third_columns_integers)
        
        if (not test1) or (not test2):
            print("hallucination in 1")
            return False
        else:    
            ans = ml_alg(ans3)
            return ans
        #ml_alg(c)

    else:  
        (ans1, ans2), ans3 = caller_almost_fin(dir_out_2, file_dataset, out_cut_1_with_dir)
        a, b = func_for_two_files(ans1, ans2, 2, dir_out_2)
    # print(f"ans ={a} b = {b} c = {ans3}")
        append_text_files(a, ans3)
        df1 = pd.read_csv(dir_out_2 + file_dataset)
        df2 = pd.read_csv(ans3)

        # Get the number of rows in each DataFrame
        #rows_file1 = len(df1)
        #rows_file2 = len(df2)
        '''
        # Check if the number of rows are different
        if rows_file1 != rows_file2:
            print(f"_____hallucination_____The number of rows are different. file1.csv has {rows_file1} rows, and file2.csv has {rows_file2} rows.")
        else:
            print("The number of rows are the same in both files.")

        '''


        # Check if the first columns are identical
        test1 = df1.iloc[:, 0].equals(df2.iloc[:, 0])

        # Check if the second and third columns in the second file are of integer type
        test2 = df2.iloc[:, 1].dtype == 'int' and df2.iloc[:, 2].dtype == 'int'

        #print("First column identical:", first_column_identical)
        #print("Second and third columns in second file are integers:", second_and_third_columns_integers)
        
        if (not test1) or (not test2):
            print("hallucination")
            return False
        else:    
            ans = ml_alg(ans3)
            return ans

#dir_out = "../output_habitat/"
#file_dataset2 = "new_origin.csv"
#feature_file = "raw_out"
#caller_almost_fin_2(dir_out,file_dataset2, raw_feature_file)
'''
feature = "Habitat"
directory_output = f"../output_{feature}/"
file_shrink = "new_origin.csv"
file_1 = "raw_out"
#caller_almost_fin_2(directory_output, file_shrink, file_1)
'''




