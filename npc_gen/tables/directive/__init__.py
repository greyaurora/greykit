from npc_gen.get_rand import get_rand

from .data.action import actions
from .data.theme import themes

def create():
    return f'You need to {get_rand(actions)} {get_rand(themes)}'