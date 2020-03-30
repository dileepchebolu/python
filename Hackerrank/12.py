"""
Dictionary update
"""

import sys
phonebook = {}
for i in range (int(input())):
    arr = [arr_temp for arr_temp in input().strip().split()]
    # key1 = arr[0]
    # value = arr[1] 
    phonebook.update({arr[0]:arr[1]})
#print(phonebook.items())
lines = sys.stdin.readlines()  # convert lines to list
for i in lines:
    name = i.strip()
    if name in phonebook:
        print(name + "=" + phonebook[name] )
    else:
        print("Not found")