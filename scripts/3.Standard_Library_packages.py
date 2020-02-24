import time
"""
Here no need to import whole time library, instead we can import only some functions which are using in this script. As shown below

from time import localtime, mktime, strftime
"""
start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

input("Press 'Enter' to stop timer ")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")

print(f"Total time: {difference} seconds")


# ==================================
# OUTPUT:
#     Timer started at 02:24:31
#     Press 'Enter' to stop timer
#     Timer stopped at 02:24:37
#     Total time: 6.0 seconds
# =================================