import subprocess
    ## Using subprocess package/Module we can execute shell commands from the python scripts.

proc = subprocess.run(["ls", "-al"])

print(proc)

print(proc.returncode)  ## It will show the return code of the command 

print(proc.args)  ## Will print all the arguments 

subprocess.PIPE