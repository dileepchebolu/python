dileep = input("what you want to add here ..?")
print("Hello " + dileep )

# For taking password as input, use getpass package and use like below.

import getpass

p = getpass.getpass(prompt="What is your prod password..?")   ## It won't show the entered password on terminal.

if p.lower() == 'rose':
    print("Welcome!!")
else:
    print("The answer you provided is incorrect :( ")


print(getpass.getuser())   ## For printing the default user who currently logged into.