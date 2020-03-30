"""
Task: 
    There are lines of numeric input:

    The first line has a double, mealCost(the cost of the meal before tax and tip).
    
    The second line has an integer, tipPercent (the percentage of being added as tip).
    
    The third line has an integer, taxPercent(the percentage of being added as tax).

Output Format

    Print the total meal cost, where totalCost is the rounded integer result of the entire bill (mealCost with added tax and tip).
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    value1 = float(meal_cost)
    value2 = float(value1 * (float(tip_percent) / 100))
    value3 = float(value1 * (float(tax_percent) / 100))

    print(round(value1 + value2 + value3))
if __name__ == '__main__':
    meal_cost = (input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)