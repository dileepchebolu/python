"""
Task : Print the max number of consecutive 1's in a binary format of a decimal number 
"""
if __name__ == '__main__':
    n = int(input())

result=bin(n)
#print(result)
list_result = (list(result[2:]))
for i in range(len(list_result)):
    list_result[i] = int(list_result[i])

#print(list_result)
#list_result_1 = len(list(result[2:])) - 1 
result_list = []
re = 0 
for i in range(len(list_result)):
    if list_result[i] == 1:
        re=re+1 
    else: 
        result_list.append(re)
        re = 0
result_list.append(re)
#print(result_list)
for i in range(len(result_list) - 1):
    if result_list[i] > result_list[i+1]:
        result_list[i+1] = result_list[i]
print(result_list.pop())