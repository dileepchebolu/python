import argparse 

parser = argparse.ArgumentParser(description="Description about the script")
parser.add_argument("filename", help=" the file to read")
parser.add_argument("--limit", "-l", type=int, help="The number of lines to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.0")

args = parser.parse_args()

print(args)

print(parser.parse_args().filename)   ## Will print the argument "filename" value 



"""
=============================================
OUTPUT:
    $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/5.Robuct_CLIs_with_argparse.py -h
    usage: 5.Robuct_CLIs_with_argparse.py [-h] [--limit LIMIT] [--version] filename

    Description about the script

    positional arguments:
    filename              the file to read

    optional arguments:
    -h, --help            show this help message and exit
    --limit LIMIT, -l LIMIT
                            The number of lines to read
    --version, -v         show program's version number and exit

    Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/Examples (master)
    $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/5.Robuct_CLIs_with_argparse.py -v 1.0 sample.txt
    5.Robuct_CLIs_with_argparse.py 1.0

    Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/Examples (master)
    $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/5.Robuct_CLIs_with_argparse.py --version
    5.Robuct_CLIs_with_argparse.py 1.0

    Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/Examples (master)
    $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/5.Robuct_CLIs_with_argparse.py --limit 10
    usage: 5.Robuct_CLIs_with_argparse.py [-h] [--limit LIMIT] [--version] filename
    5.Robuct_CLIs_with_argparse.py: error: the following arguments are required: filename

    Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning/Examples (master)
    $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/5.Robuct_CLIs_with_argparse.py --limit 10 sample.txt
    Namespace(filename='sample.txt', limit=10)
=================================================
"""