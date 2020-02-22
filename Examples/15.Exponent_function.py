result = 2 ** 8
print(result)   ## Will be equal to 2^8 

# ===============
def exponential(Base_no,Power_no):
      print(Base_no ** Power_no)

exponential(3,4)

# ==================

def exponential_2(Base_no, Power_no):
    result = 1
    for i in range(Power_no):
        print(i)   ## have print this one to avoid syntax warning only
        result = Base_no * result 
    return result

print(exponential_2(10,5))

# =============================
# TOTAL OUTPUT:
# 256
# 81
# 0
# 1
# 2
# 3
# 4
# 100000
# =============================