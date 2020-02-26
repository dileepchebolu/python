import argparse

parser = argparse.ArgumentParser(description="Searching for words including partial word")
parser.add_argument("snippet", help = "Partial ot complete string to search for in words")

args = parser.parse_args()

snippet = args.snippet.lower()

with open("scripts/sample.txt") as f:
    words = f.readlines()

# matches = []

# for word in words:
#     if snippet in word.lower():
#         matches.append(word)

##Other alternative way to above commented one:

matches = [word.strip() for word in words if snippet in word.lower()]   ## strip is usefull to remove spaces or new lines.

print(matches)
# ========================================
# OUTPUT:
#     With-out strip:
#         $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/10.Advanced_Iteration_with_Lis
#         t_Comprehensions.py dileep
#         ['Dileep\n']

#     With strip:
#         $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/10.Advanced_Iteration_with_Lis
#         t_Comprehensions.py dileep
#         ['Dileep']
# ========================================
