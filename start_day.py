import requests
import sys

YEAR = 2025
day = sys.argv[1]

URL = f"https://adventofcode.com/{YEAR}/day/{day}/input"
cookie = open("cookie.txt", "r").read()

r = requests.get(URL, headers={"Cookie": cookie})

with open(f"inputs/day{day}.txt", "w") as f:
    f.write(r.text)

with open(f"inputs/test{day}.txt", "w") as f:
    pass # create empty file

template = open(f"template.py", "r").read()
with open(f"day{day}.py", "w") as f:
    f.write(template)