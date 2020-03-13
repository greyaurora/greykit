from random import randint
from functools import reduce

# select a random outcome from an 'oracle' list
def get_rand(oracle):
    return oracle[randint(0, len(oracle)-1)]

# select a random outcome from a weighted 'oracle' list
# oracle = {
#   3: ['common'],
#   2: ['uncommon'],
#   1: ['rare'],
# }
def get_wrand(oracle):
    results = []
    for key in oracle:
        for item in oracle[key]:
            for _ in range(key):
                results.append(item)

    return get_rand(results)