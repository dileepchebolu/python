#!/bin/python3

import sys

def binary(n):
    bin=[]
    while n>1:        
        bin.append(n%2)
        n=n//2
        if n==0 or n==1:
            bin.append(n)
    return bin

n = int(input().strip())
bin=binary(n)
print(bin)
re=0
result=[]
print(result)
for i in range(len(bin)):
    if bin[i]==1:
        re=re+1
    else:
        result.append(re)
        re=0
result.append(re)
print(result)
# for i in range(len(result)-1):
#     if result[i]>result[i+1]:
#         result[i+1]=result[i]
# print(result.pop())
