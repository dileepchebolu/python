def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = max_num(30,40,50)

print(result)

# Some other strings:

# == for strings 
# <= for lessthan or equal to
# != not-equal-to 
# and for  First it will perform first operation and then only it will look for second function.
# or  for Either one of the function should be true, then only condition would be true.