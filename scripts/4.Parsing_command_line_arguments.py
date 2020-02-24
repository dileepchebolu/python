import sys

## This will be useful to pass arguments to the script

print(f"First argument is {sys.argv[0]}")  ## First Argument is the script file name and it will print the whole path of the file.

# ============================
# OUTPUT:
#     First argument is c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/4.Parsing_command_line_arguments.py
# ============================

print(f"Positional arguments: {sys.argv[1:]}")  ## It will print out the positional arguments as a list

# =================
# OUTPUT: 
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/4.Parsing_command_line_arguments.py dileep surya
#     First argument is c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/4.Parsing_command_line_arguments.py
#     Positional arguments: ['dileep', 'surya']
# ==================