class Stats:

    def __init__(
        self,
        strength=0,
        dexterity=0,
        constitution=0,
        intelligence=0,
        wisdom=0,
        charisma=0,
    ):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return f"Strength: {self.strength}\n Dexterity: {self.dexterity}\n Constitution: {self.constitution}\n Intelligence: {self.intelligence}\n Wisdom: {self.wisdom}\n Charisma: {self.charisma}"

    def __add__(self, other):
        strength = self.strength + other.strength
        dexterity = self.dexterity + other.dexterity
        constitution = self.constitution + other.constitution
        intelligence = self.intelligence + other.intelligence
        wisdom = self.wisdom + other.wisdom
        charisma = self.charisma + other.charisma
        return Stats(strength, dexterity, constitution, intelligence, wisdom, charisma)


character_stats = {
    "Barbarian": Stats(15, 13, 14, 8, 12, 10),
    "Bard": Stats(8, 14, 13, 10, 12, 15),
    "Cleric": Stats(14, 8, 13, 12, 15, 10),
    "Druid": Stats(8, 14, 13, 10, 15, 12),
    "Fighter": Stats(15, 14, 13, 8, 12, 10),
    "Monk": Stats(12, 15, 13, 8, 14, 10),
    "Paladin": Stats(14, 8, 13, 10, 12, 15),
    "Ranger": Stats(13, 15, 12, 10, 14, 8),
    "Rogue": Stats(8, 15, 12, 13, 10, 14),
    "Sorcerer": Stats(8, 13, 14, 10, 12, 15),
    "Warlock": Stats(8, 14, 13, 10, 12, 15),
    "Wizard": Stats(8, 14, 13, 15, 12, 10),
}


character_race = {
    "Dwarf": {
        "bonus": Stats(2, 0, 2, 0, 0, 0),
        "movement": 25,
        "darkvision": True,
        "special": "Advantage on saving throws against poison/resistance to poison damage.",
    },
    "High_elf": {
        "bonus": Stats(0, 2, 0, 1, 0, 0),
        "movement": 30,
        "darkvision": True,
        "special": "Know one cantrip from wizard spell list.",
    },
    "Halfling": {
        "bonus": Stats(0, 2, 0, 0, 0, 1),
        "movement": 25,
        "darkvision": False,
        "special": "Advantage on saving throws against being frightened, Lucky (can reroll a 1 on a saving throw, attack roll, ability check), can hide behind a creature at least medium size.",
    },
    "Human": {
        "bonus": Stats(1, 1, 1, 1, 1, 1),
        "movement": 30,
        "darkvision": False,
        "special": "None",
    },
    "Half_orc": {
        "bonus": Stats(2, 0, 1, 0, 0, 0),
        "movement": 30,
        "darkvision": True,
        "special": "Proficient in indimidation skill, relentless endurance (drop to 1 hp instead of 0 once per long rest), roll an additional damage dice on critical hit.",
    },
    "Tiefling": {
        "bonus": Stats(0, 0, 0, 1, 0, 2),
        "movement": 30,
        "darkvision": True,
        "special": "Resistant to fire damage, thaumaturgy cantrip.",
    },
}


