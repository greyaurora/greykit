import argparse
import re
import random
import functools

parser = argparse.ArgumentParser(description='Do a thing')
parser.add_argument('input', metavar='cmd', type=str, nargs='+')
inputArgs = parser.parse_args().input

# the first argument provided is an instruction of what to do
action = inputArgs[0]

def roll(args):
    try:
        qty, die, mod = re.match(r'(\d*)d?(\d*)\s*\+?\s*(\d*)', args[0]).group(1,2,3)
        qty, die, mod = int(qty or 1), int(die or 20), int(mod or 0)
    except:
        qty, die, mod = 1, 20, 0

    results = []
    for _ in range(qty):
        results.append(random.randint(1, die))

    if (qty > 1):
        print(results)
    
    return functools.reduce(lambda a,b : a+b, results) + mod

