#!/usr/bin/env python3.6

import os    ## for getting environement variables 
import argparse ## For managing with cli arguments
import sys    ## For getting exit status 
import requests ## To deal with URLs 

parser = argparse.ArgumentParser(description="Get the current weather information using zip zode")
parser.add_argument("zip", help="zip/Postal code to get weather for")
parser.add_argument("--country", "-c", default="us")

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Error: No 'OWM_API_KEY' provided")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

print(res.json())
 

# ======================================

# OUTPUT:
#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ export OWM_API_KEY="218481d3b4a5ef600a808d7630aa00d952"   ## modified this key  :P

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py 534312
#     <Response [404]>

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py 45891
#     <Response [200]>

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py 534312 --country IN
#     <Response [200]>

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py
#     usage: 11.Using_3rd_party_packages_in_scripts.py [-h] [--country COUNTRY] zip
#     11.Using_3rd_party_packages_in_scripts.py: error: the following arguments are required: zip

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py 534312 --country IN
#     <Response [200]>
#     <bound method Response.json of <Response [200]>>

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py
#     usage: 11.Using_3rd_party_packages_in_scripts.py [-h] [--country COUNTRY] zip
#     11.Using_3rd_party_packages_in_scripts.py: error: the following arguments are required: zip

#     Dileep_Chebolu@W2797020X3ARU MINGW64 ~/Desktop/Python_Learning (master)
#     $ C:/Users/dileep_chebolu/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/dileep_chebolu/Desktop/Python_Learning/scripts/11.Using_3rd_party_packages_in_scripts.py 534312 --country IN
#     <Response [200]>
#     {'coord': {'lon': 81.43, 'lat': 17.09}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 293.51, 'feels_like': 295.63, 'temp_min': 293.51, 'temp_max': 293.51, 'pressure': 1012, 'humidity': 90, 'sea_level': 1012, 'grnd_level': 1006}, 'wind': {'speed': 1.38, 'deg': 26}, 'clouds': {'all': 0}, 'dt': 1582674975, 'sys': {'country': 'IN', 'sunrise': 1582678509, 'sunset': 1582720791}, 'timezone': 19800, 'id': 0, 'name': 'Ponguturu', 'cod': 200}

# ======================================    