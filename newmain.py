from mainer import mainer_caller
import os
current_directory = os.getcwd()
print(f"{current_directory}")
#new_directory = current_directory + "/mainer/"
#os.chdir(new_directory)

mainer_caller.mainer_main(None)