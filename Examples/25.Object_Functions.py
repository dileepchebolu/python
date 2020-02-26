"""
Main Types of data we can manage in python is Strings, Intergers, and Booleans. 
and we can sort the data using lists and dictionaries.

And by using only those 3 data types we can not create all the things. So we have to create our own data types. 

Solution:
By using classes and objects, we can create out own data types

By using class we can create a data type and we can use that data type by calling that class. Using class we can essentially define your own data types.


"""
from app import Student

"""
FYI, Am pasting the Student class here ..
    class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa 
        self.is_on_probation = is_on_probation
    
    def on_honor_roll(self):   ## Have added new definition to the same class student in app file 
        if self.gpa >= 3.5:
            return True
        else:
            return False

"""

student1 = Student("Dileep", "Business", 3.1, False)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print(student1.on_honor_roll())
# ==========================
# OUTPUT:
#     Dileep
#     Business
#     3.1
#     False
# ==========================
