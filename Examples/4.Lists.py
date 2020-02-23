list_values = [ "kevin" , "Karen" , "Jim" , "dileep" ]

print(list_values[3]) 
print(list_values[0:2]) 

print(list_values[1:])  ## will print all the value after second value in the list 

print(list_values[:3]) ## Will print all the values before 4th value in the list

print(list_values[1])

print(list_values[-1])  ## Will print the last value of the list 

print(list_values[-2])  ## Will print the second last value in the list.

list_values[1] = "surya"

print(list_values[1])

list_values.append("nagendra")  ## using append function, we can add only one value.

print(list_values)

list_values.insert(0, "kumar")  ## we can insert values by providing the index_number and value to be replaced

print(list_values)

list_values.remove("kumar")  ## we can remove a value from the list using remove function 

print(list_values)

list_values.pop()  ## will remove the last element in the list 

print(list_values)

print(list_values.index("dileep"))  ## will print the index value of value named "dileep"

print(list_values.count("dileep"))  ## will give how many times the value dileep is repeated in list

list_values_2 = list_values.copy()  ## copy function will copy all the values in the list 

print(list_values_2)

list_values.clear()   ## will clear all the values to the list 


print(list_values)
#Some more modules to list:

#list_values.extend
#list_values.reverse



#Output:    
  
# dileep
# ['kevin', 'Karen']
# Karen
# surya
# ['kevin', 'surya', 'Jim', 'dileep', 'nagendra']
# ['kumar', 'kevin', 'surya', 'Jim', 'dileep', 'nagendra']
# ['kevin', 'surya', 'Jim', 'dileep', 'nagendra']
# ['kevin', 'surya', 'Jim', 'dileep']
# 3
# 1
# ['kevin', 'surya', 'Jim', 'dileep']
# []
