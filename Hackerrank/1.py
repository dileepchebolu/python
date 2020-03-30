##If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

if __name__ == '__main__':
    n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >= 20:
        print("Not Weird")