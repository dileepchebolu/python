list_values = [ "kevin" , "Karen" , "Jim" , "dileep" ]
print(len(list_values))
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

# ==========================================================
# Some more examples: 

#     >>> my_list[5]
# 		Traceback (most recent call last):
# 		  File "", line 1, in 
# 		IndexError: list index out of range

# 		To make sure that we’re not trying to get an index that is out of range, we can test the length using the len function (and then subtract 1):

# 		>>> len(my_list)
# 		5

# 		Additionally, we can access subsections of a list by “slicing” it. We provide the starting index and the ending index (the object at that index won’t be included).

# 		>>> my_list[0:2]
# 		[1, 2]
# 		>>> my_list[1:0]
# 		[2, 3, 4, 5]
# 		>>> my_list[:3]
# 		[1, 2, 3]
# 		>>> my_list[0::1]
# 		[1, 2, 3, 4, 5]
# 		>>> my_list[0::2]
# 		[1, 3, 5]

# 		Modifying a List

# 		Unlike strings which can’t be modified (you can’t change a character in a string), you can change a value in a list using the subscript equals operation:

# 		>>> my_list[0] = "a"
# 		>>> my_list
# 		['a', 2, 3, 4, 5]

# 		If we want to add to a list we can use the .append method. This is an example of a method that modifies the object that is calling the method:

# 		>>> my_list.append(6)
# 		>>> my_list.append(7)
# 		>>> my_list
# 		['a', 2, 3, 4, 5, 6, 7]

# 		Lists can be added together (concatenated):

# 		>>> my_list + [8, 9, 10]
# 		['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 		>>> my_list += [8, 9, 10]
# 		>>> my_list
# 		['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 		Items in lists can be set using slices also:

# 		>>> my_list[1:3] = ['b', 'c']
# 		>>> my_list
# 		['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]
# 		# Replacing 2 sized slice with length 3 list inserts new element
# 		my_list[3:5] = ['d', 'e', 'f']
# 		print(my_list)

# 		We can remove a section of a list by assigning an empty list to the slice:

# 		>>> my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
# 		>>> my_list[4:] = []
# 		>>> my_list
# 		['a', 'b', 'c', 'd']

# 		Removing items from a list based on value can be done using the .remove method:

# 		>>> my_list.remove('b')
# 		>>> my_list
# 		['a', 'c', 'd']

# 		Attempting to remove and item that isn’t in the list will result in an error:

# 		>>> my_list.remove('f')
# 		Traceback (most recent call last):
# 		  File "", line 1, in 
# 		ValueError: list.remove(x): x not in list

# 		Items can also be removed from the end of a list using the pop method:

# 		>>> my_list = ['a', 'c', 'd']
# 		>>> my_list.pop()
# 		'd'
# 		>>> my_list
# 		['a', 'c']

# 		We can also use the pop method to remove items at a specific index:

# 		>>> my_list.pop(0)
# 		'a'
# 		>>> my_list
# 		['c']
# 		>>> my_list.pop(1)
# 		Traceback (most recent call last):
# 		  File "", line 1, in 
# 		IndexError: pop index out of range
# 		>>> [].pop()
# 		Traceback (most recent call last):
# 		  File "", line 1, in 
# 		IndexError: pop from empty list

# ========================================================