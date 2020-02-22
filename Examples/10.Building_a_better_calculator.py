num1 = float(input("enter first number: "))
operator = input("enter operator: ")
num2 = float(input("enter second number: "))

if operator == "+":
    print( num1 + num2 )
elif operator == "-":
    print( num1 - num2 )
elif operator == "*":
    print( num1 * num2 )
else:
    print("Invalid Operator")
# =================================
# Output:
# enter first number: 40
# enter operator: +
# enter second number: 30
# 70.0
# =================================