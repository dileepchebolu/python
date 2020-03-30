"""
TASK: Working with 2d lists, and find the highest sum of hourglass in a matrix 

Sample Input of A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4

"""
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    arr = []

## First we have to convert the matrix into lists,
for array in range(6):
    arr_temp = [int(arr_temp) for arr_temp in input().strip().split(" ")]
    arr.append(arr_temp)
print(arr)
"""
     OUTPUT: [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
     
"""
## From here, we are start working on finding the maximum number in hourglass 

count = []
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
        arr[i+1][j+1] + \
        arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
        count.append(sum)

print(max(count))