'''clerics do not have enough combat classed cantrips in phb. probably other classes have the same issue. will have to rework to figure out how to fix.
'''



import csv
import random
from flowchart import Flowchart

flowchart = Flowchart()

class Spells:

    def __init__(self):
        self.choice = None
        self.cantrip_list = []
        self.first_list = []

    def __str__(self):
        cantrips = "Cantrips:\n"
        for cantrip in self.cantrip_list:
            cantrips += f"{cantrip['name']}: {cantrip['description']}\n"
        first_levels = "1st:\n"
        for first_level in self.first_list:
            first_levels += f"{first_level['name']}: {first_level['description']}\n"

        spell_list = cantrips + first_levels

        return spell_list


    def start(self, chosen_class):
        self.chosen_class = chosen_class

        while True:
            self.choice = input("Do you want to do combat magic, support/healing magic, or both? ").lower()

            if "combat" in self.choice:
                self.type = "combat"
                break
            elif "healing" in self.choice or "support" in self.choice:
                self.type = "support"
                break
            elif self.choice == "both":
                self.type = "combination"
                break
            else:
                print("Please enter 'combat', 'healing', 'support', or 'both'.")
        return self.type

    def filter_spells(self, spell_type, chosen_class, level):

        spells = []
        with open("spell_list.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                class_list = [class_type.strip() for class_type in row["classes"].split(",")]
                if row["type"] in spell_type and chosen_class in class_list and row["level"] == level:
                    spells.append({"name": row["name"], "description": row["description"]})

        return spells

    def spell_list(self, type):

        if self.chosen_class == "Bard":
            n = 2
            m = 4
        elif self.chosen_class in ["Cleric", "Druid"]:
            n = 3
            m = 2
        elif self.chosen_class == "Sorcerer":
            n = 4
            m = 2
        elif self.chosen_class == "Warlock":
            n = 2
            m = 2
        elif self.chosen_class == "Wizard":
            n = 3
            m = 6

        support_cantrip = self.filter_spells(["support"], self.chosen_class, "0")
        support_first = self.filter_spells(["support"], self.chosen_class, "1")
        combat_cantrip = self.filter_spells(["damage"], self.chosen_class, "0")
        combat_first = self.filter_spells(["damage"], self.chosen_class, "1")
        combo_cantrip = self.filter_spells(["damage", "support"], self.chosen_class, "0")
        combo_first = self.filter_spells(["damage", "support"], self.chosen_class, "1")

#Added while loops here to account for possible lack of appropriate number of cantrips/first level spells at desired level
        if type == "combat":
            while True:
                try:
                    self.cantrip_list = random.sample(combat_cantrip, k=n)
                    break
                except ValueError:
                    n = n-1
                    print("Number of cantrips is reduced based on choices")
            while True:
                try:
                    self.first_list = random.sample(combat_first, k=m)
                    break
                except ValueError:
                    m = m-1
                    print("Number of first level spells is reduced based on choices")

        elif type == "support":
            while True:
                try:
                    self.cantrip_list = random.sample(support_cantrip, k=n)
                    break
                except ValueError:
                    n = n-1
                    print("Number of cantrips is reduced based on choices")
            while True:
                try:
                    self.first_list = random.sample(support_first, k=m)
                except ValueError:
                    m = m-1
                    print("Number of first level spells is reduced based on choices")

        elif type == "combination":
            self.cantrip_list = random.sample(combo_cantrip, k=n)
            self.first_list = random.sample(combo_first, k=m)

        return self.cantrip_list, self.first_list












