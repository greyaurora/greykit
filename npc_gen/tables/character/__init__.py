from npc_gen.get_rand import get_rand
from .data.action import actions
from .data.desc import descriptors
from .data.goal import goals
from .data.name import names
from .data.pronoun import pronouns
from .data.race import race
from .data.role import roles

def create():
    return '''NPC: {fname} {lname} ({pronouns}) the {race} {role}
{fname} wants to {goal}
{fname} is {att}
{fname} prefers to solve problems with {action}'''.format(
        fname = get_rand(names),
        lname = get_rand(names),
        pronouns = get_rand(pronouns),
        race = race(),
        role = get_rand(roles),
        goal = get_rand(goals),
        att = f'{get_rand(descriptors)}, {get_rand(descriptors)}, and {get_rand(descriptors)}',
        action = get_rand(actions),
    )