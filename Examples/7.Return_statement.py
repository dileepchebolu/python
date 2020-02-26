def function_1(num):
    print("Sample function with return statement")
    print(num*num*num)   ## By default will give "none" as output, even if you print the output of the math.
print(function_1(3))
# ============================
# # Output:

# # Sample function with return statement
# # 27
# # None
# ==============================


def function_2(num):
    print("Sample function with return statement")
    print(num*num*num)   ## By default will give "none" as output, even if you print the output of the math.
    return num*num*num  ## will return this value when exit from the function. After the return function it will break the execution of function and it wont look for commands further in function 
result = function_2(10)   ## this is standard way of using functions
#Another way of printing the output of the function
print(function_2(20))
print(result)

# ==============================
# # Output:
# # $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/Examples/7.Return_statement.py
# Sample function with return statement
# 27
# None
# Sample function with return statement
# 1000
# Sample function with return statement
# 8000
# 8000
# 1000
# ==============================




