import sys

class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []
            
    def pushCharacter(self,obj):
        self.stack.append(obj)
    def enqueueCharacter(self,obj):
        self.queue.append(obj)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)
        


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True

print(obj)

'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        ### comparision of last value and first value in a list, for each time in a loop will remove the values from first and last.
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    