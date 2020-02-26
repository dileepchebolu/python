employee_file = open("Examples/employee_file.txt", "a")

print(employee_file.writable())  ## Will check wether we able to write the file or not. and the output is like boolean value.
employee_file.write("\nhari - Systems engineer")  ## it will append this content to the last line in the file. if you want to add this content to new file, need to give \n to create a new line in the file.

employee_file.close()


employee_file = open("Examples/employee_file.txt", "r")

# Note: We can use "w" to create a new file, and when you execute that one it will delete all the content in that file.

print(employee_file.read()) 