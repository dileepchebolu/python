"""
We can inherit some class files into the another class files

"""

from chef_1 import chef   ## will import the class chef from chef_1 file 

class ChineseChef(Chef):    ## ChineseChef(chef) means all the definitions mentioned in chef class will include into ChineseChef class file 
    def make_fried_rice(self):
        print("The chef makes fried rice")