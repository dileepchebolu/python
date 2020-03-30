"""
Task
    You are given the year, and you have to write a function to check if the year is leap or not.
        Note that you have to complete the function and remaining code is given as template.

Input Format
    Read y, the year that needs to be checked.

Constraints

Output Format
    Output is taken care of by the template. Your function must return a boolean value (True/False)

"""

def is_leap(year):
    leap = False
    if year >= 1900 and year <= 100000:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
            else:
                leap = True
        else:
            leap = False
        return leap

year = int(input())
print(is_leap(year))