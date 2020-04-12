#!/bin/python3

import sys

def bubbleswap(array):
    n = len(array)
    swaps = 0
    
    for i in range(n):
        num_swaps = 0 
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                num_swaps += 1
            
        if num_swaps == 0:
            break 
        else:
            swaps = swaps + num_swaps 
    return swaps


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_swaps = bubbleswap(a)

print(f"Array is sorted in {total_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")


#---------------------------------------------------------
## Another method of usage:
#!/bin/python3

import sys

def bubble_sort(array):
    n = len(array)
    total_nb_swaps = 0
    for i in range(n):
        nb_swaps = 0
        
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                nb_swaps += 1
        if nb_swaps == 0:
            break
        else:
            total_nb_swaps += nb_swaps
    return total_nb_swaps

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

nb_swaps = bubble_sort(a)

print("Array is sorted in {numSwaps} swaps.".format(numSwaps=nb_swaps))
print("First Element: {firstElement}".format(firstElement=a[0]))
print("Last Element: {lastElement}".format(lastElement=a[len(a)-1]))