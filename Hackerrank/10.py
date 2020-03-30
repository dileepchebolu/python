"""
Task: For printing an array in reverse order 
# # if __name__ == "__manin__":
# n = int(input())
# #arr = list(input())
# arr = list(map(int, input().strip().split()))
# #arr1 = list(input())

# # print(arr)

# # # print(arr[::-1])
# # # print(arr)

# # print(list(reversed(arr)))

correct method:
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(n):
    print(-i-1)
    print(str(arr[-i-1]))
