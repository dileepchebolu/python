employee_file = open("Examples/employee_file.txt", "r")

## In above command, open function is useful to open any file. And you have to give full path of the file you want to open.
# then  "r" for open file with read permissions 
#       "w" for write permissions, when we use "w" it will create new file and wipe out anything already existed in that file.
#       "a" for append permissions, means it can not read or write the existing content in the file.
#       "r+" for read and write permissions 
print(employee_file.readable())  # will print wether the file opened is readable or not and will print boolean value 
print(employee_file.read())    ## will print all the contents of the file 
#print(employee_file.readline())  ## will print only first line of the file 
print(employee_file.readlines()[1]) ## will print all the lines in the file (as like read function) Will give out output as like a "list". 
# ========================================================================
# OUTPUT:
#       True
#       Dileep - Systems engineer

#       ['Bala - UI Developer\n', 'Jegan - Infra engineer\n', 'Abdul - systems engineer']
# ============================================================================

employee_file.close()   ## will close the open file to process.



"""
Some sample for loop to print all the lines 

employee_file = open("Examples/employee_file.txt", "r")

for employee in employee_file.readlines():
    print(employee)

"""
