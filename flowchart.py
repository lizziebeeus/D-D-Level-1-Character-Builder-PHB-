class Flowchart:

    def __init__(self):
        self.choice = None

    def start(self):
        while True:
            self.choice = input("Do you want to do magic, melee, or both? ").lower()

            if self.choice == "magic":
                return self.caster()
            elif self.choice == "melee":
                return self.bonk()
            elif self.choice == "both":
                return self.mix()
            else:
                print("Please enter 'magic', 'melee', or 'both'.")

    """Magic classes include Cleric, Wizard, Druid, Sorcerer, and Warlock, and are parsed by "caster", "student" and "natural"
    - Caster function contains Cleric only or redirects to the appropriate secondary function"""

    def caster(self):
        while True:
            self.choice = input("Do you want to follow a god? ").lower()
            if self.choice == "yes":
                self.chosen_class = "Cleric"
                return self.pick_race()
            elif self.choice == "no":
                while True:
                    self.choice = input("Do you like to study? ").lower()
                    if self.choice == "yes":
                        return self.student()
                    elif self.choice == "no":
                        return self.natural()
                    else:
                        print("Please enter 'yes' or 'no'")
            else:
                print("Please enter 'yes' or 'no'")

    """Student function contains Druid and Wizard"""

    def student(self):
        while True:
            self.choice = input("Do you like nature? ").lower()
            if self.choice == "yes":
                self.chosen_class = "Druid"
                break
            elif self.choice == "no":
                self.chosen_class = "Wizard"
                break
            else:
                print("Please enter 'yes' or 'no'")

        return self.pick_race()

    """Natural function contains Sorcerer and Warlock"""

    def natural(self):
        while True:
            self.choice = input("Were you born with magic abilities? ").lower()
            if self.choice == "yes":
                self.chosen_class = "Sorcerer"
                break
            elif self.choice == "no":
                self.chosen_class = "Warlock"
                break
            else:
                print("Please enter 'yes' or 'no'")

        return self.pick_race()

    """ Bonk function contains Fighter, Monk and Barbarian """

    def bonk(self):
        while True:
            self.choice = input("Do you want to fight with your fists, or a weapon? ").lower()
            if self.choice == "fists":
                self.chosen_class = "Monk"
                break
            elif self.choice == "weapon":
                while True:
                    self.choice = input("Do you prefer strategy, or blind rage? ").lower()
                    if self.choice == "strategy":
                        self.chosen_class = "Fighter"
                        break
                    elif self.choice == "blind rage" or self.choice == "rage":
                        self.chosen_class = "Barbarian"
                        break
                    else:
                        print("Please enter either 'strategy' or 'blind rage'")
            else:
                print("Please enter either 'fists' or 'weapon'")

        return self.pick_race()

    """ Mix function contains Paladin, Bard, Ranger and Rogue as they can do a combination of melee/magic"""

    def mix(self):
        while True:
            self.choice = input("Are you good with people? ").lower()
            if self.choice == "yes":
                while True:
                    self.choice = input("Are you sneaky? ").lower()
                    if self.choice == "yes":
                        self.chosen_class = "Rogue"
                        break
                    elif self.choice == "no":
                        while True:
                            self.choice = input(
                                "Do you prefer words or smiting? ").lower()
                            if self.choice == "words":
                                self.chosen_class = "Bard"
                                break
                            elif self.choice == "smiting":
                                self.chosen_class = "Paladin"
                                break
                            else:
                                print("Please enter 'words' or 'smiting'")
                    else:
                        print("Please enter 'yes' or 'no'")
            elif self.choice == "no":
                self.chosen_class = "Ranger"
                break
            else:
                print("Please enter 'yes' or 'no'")

        return self.pick_race()

    """Function pick_race allows user to choose which D&D race they would like to play. Each race gets specific bonuses to certain stats.
    Returns the chosen class and race as a tuple"""

    def pick_race(self):
        race = ["dwarf", "high_elf", "halfling", "human", "half_orc", "tiefling"]
        while True:
            self.chosen_race = input("Which race would you like to play? Please choose from 'Dwarf', 'High elf', 'Halfling', 'Human', 'Half orc', or 'Tiefling': ").lower()
            if self.chosen_race == "high elf":
                self.chosen_race = "high_elf"
            elif self.chosen_race == "half orc":
                self.chosen_race = "half_orc"

            if self.chosen_race in race:
                return (self.chosen_class, self.chosen_race.capitalize())
            else:
                print("Please enter a race from the list")
