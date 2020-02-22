def sayhi():  ## def is equal to function in bash scripting 
    print("hello World !!")

print("Top")
sayhi()  ## calling the function 
print("Bottom")

# Output:
#     Top
#     hello World !!
#     Bottom

# In bash scripting:  

# xyz23 ()
# {
# echo "$FUNCNAME now executing." # xyz23 now executing.
# }

# xyz23 ## for calling above function in bash scripting


## Passing variables to function 

def say_hi( name ):
    print("entering value of " + name + " in function")

say_hi("dileep")

def say_hi_2( name , age ):
    print("am adding a person name here from the function " + name + " and the age of the person is " + age )

say_hi_2("Surya", "30")  ## calling the function with variable names included in the function


