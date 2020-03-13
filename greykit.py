import argparse

import npc_gen
from roll import roll

# test imports - delete after reading
from npc_gen.get_rand import get_wrand

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("data", default='', nargs='?')

args = parser.parse_args()

commands = {
    'npc': npc_gen.char,
    'goal': npc_gen.directive,
    'loc': npc_gen.loc,
    'town': npc_gen.town,
    'test': get_wrand,
    'roll': lambda: roll(args.data),
}

cmd_func = commands.get(args.command, lambda: "command not recognised")

# the below assumes that all functions used here return a printable string
print(cmd_func())
