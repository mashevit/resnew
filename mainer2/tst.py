
from mainer2.mainer_step_7_test import step_7_1
from mainer2.with_two_files import func_for_two_files, check
from mainer2.cut_file_from_ln import cut_lines
from mainer2.merge_combined import append_text_files
from mainer2.accuracy_ml import ml_alg

def caller_almost_fin_2(dir_out_2, file_dataset, raw):
    out_cut_1_with_dir = dir_out_2 + "out1"
    # step_7_1("../output/output.csv","../output/out5","../output/out51")
    step_7_1(dir_out_2 + file_dataset, dir_out_2 + raw, out_cut_1_with_dir)
    print(file_dataset)
    (ans1, ans2), ans3 = caller_almost_fin(dir_out_2, file_dataset, out_cut_1_with_dir)
    a, b = func_for_two_files(ans1, ans2, 2, dir_out_2)
   # print(f"ans ={a} b = {b} c = {ans3}")
    append_text_files(a, ans3)
    ml_alg(ans3)





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
'''
feature = "communication"
#second iteration
directory_output = f"../output1_{feature}/"
file_1 = "raw_out"
#save_string_to_file(step6_ans, directory_output, file_1)
file_shrink = "new_origin.csv"
#destination_file = directory_output + "origin.csv"
destination_file1 = directory_output + file_shrink

#extract_first_and_last_columns(file2,destination_file1)
        #caller_almost_fin_2(directory_output, file_shrink, file_1)
dir_out_2 = directory_output



#def caller_almost_fin_2(dir_out_2, file_dataset, raw):
out_cut_1_with_dir = directory_output + "out1"
step_7_1(directory_output + file_shrink, dir_out_2 + file_1, out_cut_1_with_dir)
a, b, c = check(file_shrink, "out1", dir_out_2, "checked", "out1_combined")

print(f"a = {a} b= {b} c = {c}")
'''
