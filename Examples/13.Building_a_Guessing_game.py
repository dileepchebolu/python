real_password = "dileepchebolu"
guess_password = ""
import getpass

while guess_password != real_password:
    #guess_password = input("Enter correct password: ")  ## THis is for taking normal input. and will show what we are entering in terminal.
    guess_password = getpass.getpass(prompt="Enter correct password: ")   ## This one is we should use for passwords, bcz, it won't show what we are taking from user.

print("Whola! you able to find the correct password :)")

# ====================================================
# Output:
# Enter correct password: dileep
# Enter correct password: dileep123
# Enter correct password: dileepchebolu
# Whola! you able to find the correct password :)
# ====================================================

real_password = "DileepSurya"
guess_password = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess_password != real_password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_password = input("Enter the passowrd you are expecting to be: ")
        guess_count += 1
    else:
        out_of_guesses = True

     
if out_of_guesses == True:  ## you can say like this also "if out_of_guesses:"  because it that is true only will do the particular task.
    print("You ran out of attempts :(" )
else:
    print("You able to guess the password correctly :)")

# ===========================================================
# Output:
#     Enter the passowrd you are expecting to be: Dileep
#     Enter the passowrd you are expecting to be: DileepSurya
#     You able to guess the password correctly :)
# ============================================================
    