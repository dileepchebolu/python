import argparse 

parser = argparse.ArgumentParser(description="Description about the script")
parser.add_argument("filename", help=" the file to read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.0")

args = parser.parse_args()

print(args)

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]
    
    for line in lines:
        print(line.strip()[::-1])    ## ::-1 Will print the lines in revers indexing  


# ==================================================
# OUTPUT:
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/6.Robuct_CLIs_with_argparse_2.py --limit 10 sample.txt
#     Namespace(filename='sample.txt', limit=10)
#     ramuK
#     kohsA
#     ramuK
#     ardnegaN
#     ayruS
#     peeliD
#     olleH

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/scripts (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/6.Robuct_CLIs_with_argparse_2.py --limit 2 sample.txt
#     Namespace(filename='sample.txt', limit=2)
#     ramuK
#     kohsA
# ====================================================
