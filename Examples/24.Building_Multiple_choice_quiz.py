## Importing class Question stored in app file
from app import Question

question_prompts = [
    "What color are apples ..?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Whar color are Bananas..?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries..?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

## Questions to be asked 
"""
FYI Question class mentioned in app file

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer 

"""


questions_list = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")

]

def run_test(questions_list):    ## We are giving input of questions_list as perameter to the function
    score = 0 
    for question in questions_list:
        #print(question.prompt) ## It will print all the avilable questions listed out in questions_list 
        answer = input(question.prompt)    ## Will prompt the questions one by one as it is in for loop and taking human input as a answer and stored in answer variable 
        if answer == question.answer:      ## If human provided answer is equal to question.answer, then score will increase 
            score += 1 
    print("You got "+ str(score) + "/" + str(len(questions_list)) + "correct")


run_test(questions_list)

