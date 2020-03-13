from npc_gen.get_rand import get_rand
from .data.type import types
from .data.desc import descriptors

def create():
    loc = get_rand(types)
    return '''You encounter a {loc}
The {loc} is {att}'''.format(
        loc=get_rand(types),
        att=f'{get_rand(descriptors)} and {get_rand(descriptors)}'
    )