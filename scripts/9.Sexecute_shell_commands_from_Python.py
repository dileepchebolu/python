import subprocess
    ## Using subprocess package/Module we can execute shell commands from the python scripts.

proc = subprocess.run(
    ["ls", "-al"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

## By default subprocess.PIPE will print in Byte mode. If you want to decode to the notmal view use below command 

print(proc.stdout.decode())  ## For printing normal output 

print(proc)

print(proc.returncode)  ## It will show the return code of the command 

print(proc.args)  ## Will print all the arguments 

# ========================
# OUTPUT:

#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/9.Sexecute_shell_commands_from
#     _Python.py
#     total 36
#     drwxr-xr-x 1 Dileep_Chebolu 1049089    0 Feb 24 06:50 .
#     drwxr-xr-x 1 Dileep_Chebolu 1049089    0 Feb 24 01:00 ..
#     -rwxr-xr-x 1 Dileep_Chebolu 1049089  247 Feb 24 06:26 1.Reading_user_input.py
#     -rwxr-xr-x 1 Dileep_Chebolu 1049089 1819 Feb 24 06:25 2.Function_Basics.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089  762 Feb 24 02:27 3.Standard_Library_packages.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089  917 Feb 24 03:52 4.Parsing_command_line_arguments.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089 2626 Feb 24 06:21 5.Robuct_CLIs_with_argparse.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089 1453 Feb 24 06:09 6.Robuct_CLIs_with_argparse_2.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089 1800 Feb 24 06:38 7.Handling_Errors.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089  136 Feb 24 06:50 8.Exit_statuses.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089  545 Feb 24 08:44 9.Sexecute_shell_commands_from_Python.py
#     -rw-r--r-- 1 Dileep_Chebolu 1049089   52 Feb 24 06:03 sample.txt

#     CompletedProcess(args=['ls', '-al'], returncode=0, stdout=b'total 36\ndrwxr-xr-x 1 Dileep_Chebolu 1049089    0 Feb 24 06:50 .\ndrwxr-xr-x 1 Dileep_Chebolu 1049089
#     0 Feb 24 01:00 ..\n-rwxr-xr-x 1 Dileep_Chebolu 1049089  247 Feb 24 06:26 1.Reading_user_input.py\n-rwxr-xr-x 1 Dileep_Chebolu 1049089 1819 Feb 24 06:25 2.Function_Basics.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089  762 Feb 24 02:27 3.Standard_Library_packages.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089  917 Feb 24 03:52 4.Parsing_command_line_arguments.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089 2626 Feb 24 06:21 5.Robuct_CLIs_with_argparse.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089 1453 Feb 24 06:09 6.Robuct_CLIs_with_argparse_2.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089 1800 Feb 24 06:38 7.Handling_Errors.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089  136 Feb 24 06:50 8.Exit_statuses.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089  545 Feb 24 08:44 9.Sexecute_shell_commands_from_Python.py\n-rw-r--r-- 1 Dileep_Chebolu 1049089   52 Feb 24 06:03 sample.txt\n', stderr=b'')
#     0
#     ['ls', '-al']

# ==================================================