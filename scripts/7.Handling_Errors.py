import argparse 

parser = argparse.ArgumentParser(description="Description about the script")
parser.add_argument("filename", help=" the file to read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.0")

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit 
except FileNotFoundError as err:
    print(f"Error: {err}")

else:

    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]  
        
        for line in lines:
            print(line.strip()[::-1])    ## ::-1 Will print the lines in revers indexing  

# ============================================
# OUTPUT:
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/7.Handling_Errors.py
#     usage: 7.Handling_Errors.py [-h] [--limit LIMIT] [--version] filename
#     7.Handling_Errors.py: error: the following arguments are required: filename

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/scripts (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/7.Handling_Errors.py sample.txt
#     ramuK
#     kohsA
#     ramuK
#     ardnegaN
#     ayruS
#     peeliD
#     olleH
#      $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/7.Handling_Errors.py sample1.txt
#       Error: [Errno 2] No such file or directory: 'sample1.txt'
# ========================================