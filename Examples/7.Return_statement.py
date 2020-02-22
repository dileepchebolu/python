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
print(result)
# ==============================
# # Output:
# # Sample function with return statement
# # 1000
# # 1000
# ==============================




