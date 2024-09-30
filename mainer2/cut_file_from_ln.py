def cut_lines(input_file_name, output_file_name, start_line):
    print(f"in cut = outname = {output_file_name} input = {input_file_name} startln = {start_line}")

    try:
        with open(input_file_name, 'r') as infile, open(output_file_name, 'w') as outfile:
            lines = infile.readlines()
            if start_line <= len(lines):
                # Write lines starting from the specified line number to the output file
                outfile.writelines(lines[start_line - 1:])
            else:
                print(f"Start line ({start_line}) is greater than the total number of lines in the input file.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the input and output file names and the starting line number
#input_file_name = "input.txt"
#output_file_name = "output.txt"
#start_line = 5

# Call the function to cut lines
#cut_lines(input_file_name, output_file_name, start_line)