from flowchart import Flowchart
from spells import Spells
from stats import Stats
from stats import character_stats
from stats import character_race
import os

''' Rangers and Paladins are not included in caster set because they do not gain ability to cast until 2nd level, and this program creates a level 1 character'''

def main():
    flowchart = Flowchart()
    spells = Spells()
    caster = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]

    dnd_class, dnd_race = flowchart.start()

    if dnd_class in caster:
        style = spells.start(dnd_class)
        cantrip_list, first_list = spells.spell_list(style)

    if dnd_class in character_stats:
        class_stats = character_stats[dnd_class]

    if dnd_race in character_race:
        race_stats = character_race[dnd_race]
        if race_stats["darkvision"]:
            vision = "Darkvision - can see in non-magical darkness as if the darkness were dim light, in a range of 60 feet."
        else:
            vision = ""

    full_stats = class_stats + race_stats["bonus"]


    print(f"Class: {dnd_class}\nRace: {dnd_race}\nSpecial abilities: {vision} {race_stats['special']}")
    print(f"Stats:\n {full_stats}")
    print("Spell List:\nCantrips:")
    for cantrip in cantrip_list:
        print(f"Name: {cantrip['name']}\nDescription: {cantrip['description']}")
    print("First Level:")
    for first in first_list:
        print(f"Name: {first['name']}\nDescription: {first['description']}")

    """ finished with setting class, race, stats. need to add spell picker flowchart for casters, possibly add something to calculate saving throws and proficiency bonus"""






if __name__ == "__main__":
    main()
