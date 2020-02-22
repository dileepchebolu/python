is_male = False  ## Its a boolean value

if is_male:
    print("your are a male")
else:
    print("You are not a male")

# ===================
# Output:    
# # You are not a male 
# ====================

is_male = True  ## Its a boolean value
is_tall = False 
if is_male:
    #print("your are a male")
    if is_tall:
        print("You are male and tall")
    else:
        print("You are male but not tall")
else:
    print("You are not a male and not tall")

# ===============
# output:
# You are male but not tall
# ===============

if_male = True 
if_tall = False

if if_male and if_tall:
    print("You are male and Tall")
else:
    print("You are either not male or tall or both")
# ===============
# output:
# You are either not male or tall or both
# ===============

if_male = True 
if_tall = False 

if if_male and if_tall:
    print("You are male and tall")
elif if_male and not(if_tall):
    print("You are a short male")
elif not(if_male) and if_tall:
    print("you are not a male but tall")
else:
    print("You are either not male or not tall or both")
# ====================
# output:
# You are a short male
# ====================







