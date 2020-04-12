"""
We can inherit some class files into the another class files

from chef_1 import chef   ## will import the class chef from chef_1 file 

class ChineseChef(Chef):    ## ChineseChef(chef) means all the definitions mentioned in chef class will include into ChineseChef class file 
    def make_fried_rice(self):
        print("The chef makes fried rice")


Ex for Inheritence: https://www.w3schools.com/python/python_inheritance.asp
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
         
    
    def calculate(self):
        total = 0 
        for i in range(len(self.scores)):
            #print(self.scores[i])
            total = (total + int(scores[i]))
        #print(total)
        #print(len(self.scores))
        Average = (total / len(self.scores)) 
        #print(Average)
        if Average >= 90 and Average <= 100:
            return "O"
        elif Average >= 80 and Average < 90:
            return "E"
        elif Average >= 70 and Average < 80:
            return "A"
        elif Average >= 55 and Average < 70:
            return "P"
        elif Average >= 40 and Average < 55:
            return "D"
        elif Average < 40:
            return "T" 

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())