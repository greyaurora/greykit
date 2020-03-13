from npc_gen.get_rand import get_wrand

def race():
    return f'{get_wrand(modifiers)}{get_wrand(races)}'

races = {
    30: ['Human'],
    20: [
        'Dwarf', 'Elf','Half-Elf','Halfling',
    ],
    10: [
        'Dragonborn', 'Gnome', 'Half-Orc', 'Kenku', 'Tabaxi',
    ],
    5: [
        'Aarakocra', 'Goblin', 'Goliath', 'Lizardfolk', 'Genasi', 
        'Triton', 
    ],
    1: [
        'Centaur', 'Changeling', 'Firbolg', 'Aquatic Hybrid', 'Kobold',
        'Loxodon', 'Minotaur', 'Orc', 'Shifter', 'Tortle',
        'Warforged/Construct', 'Yuan-Ti', 'Vedalken',
    ],
}

modifiers = {
    80: [''],
    5: ['Aasimar ', 'Kalashtar/Twin-Spirit ', 'Tiefling '],
    1: ['Changeling ']
}