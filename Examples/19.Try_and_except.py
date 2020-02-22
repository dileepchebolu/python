
# number = int(input("enter a number to print out here:" ))
# print (number)

## If enter any input other than integer, then will throw below error 

# ===================================================================================================================
# OUTPUT:
# enter a number to print out here:dileep
# Traceback (most recent call last):
#   File "c:/Users/dileep_chebolu/Desktop/Python_Learning/Examples/19.Try_and_except.py", line 1, in <module>
#     number = int(input("enter a number to print out here:" ))
# ValueError: invalid literal for int() with base 10: 'dileep'
# ===================================================================================================================

## TO overcome all the errors in output, use TRY and EXCEPT 
try:
    value = 10 / 0
    print(value)
    number = int(input("enter a number to print out here:" ))
    print (number)

except ValueError:
    print("you entered other than integer")
except ZeroDivisionError:     
    print("You gave input as dividing by zero")
except ZeroDivisionError as error:  ## this is the method we used to print the error message
    print(error)
# =====================================================================
# OUTPUT:
#     enter a number to print out here:dileep
#       you entered other than integer
# =====================================================================