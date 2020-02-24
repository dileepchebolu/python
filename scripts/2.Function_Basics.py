#!/usr/bin/env pyhton3.8
# BMI = (Weight in Kg / height in meters squared)
# Imperial version: BMI * 703

def gather_info():
    height = float(input(f"What is your height? (inches or pounds) "))
    weight = float(input("What is you weight? (Punds or Kilograms) "))
    system = input("Are you measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)
 
def calculate_bmi(weight, height, system="metric"):    ## If you no provide value for system, will take input as metric
    """
    Return the Body Mass Index (BMI) for the given weight, height, and measurement system
    """
    if system == "metric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2 ))
    return bmi 

while True:
    height, weight , system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, height, system = system)
        print(f"Your BMI is {bmi}")
        break
    if system.startswith("m"):
        bmi = calculate_bmi(weight,height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric")

# ==============================================================================
# OUTPUT:
#     What is your height? (inches or pounds) 165
#     What is you weight? (Punds or Kilograms) 65
#     Are you measurements in metric or imperial units?
#     Error: Unknown measurement system. Please use imperial or metric
#     What is your height? (inches or pounds) 165
#     What is you weight? (Punds or Kilograms) 85
#     Are you measurements in metric or imperial units? metric
#     Your BMI is 0.0031221303948576677
# ===============================================================================