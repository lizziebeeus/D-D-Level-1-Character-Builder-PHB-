import csv
import os


import csv

def filter_spells(spell_type, chosen_class, level, file_path="spell_list.csv"):
    spells = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Debugging each condition
            class_list = [cls.strip() for cls in row["classes"].split(",")]
            type_match = row["type"] in spell_type
            class_match = chosen_class in class_list
            level_match = row["level"] == level

            # Print debug info
            print(f"Checking Row: {row['name']}")
            print(f"Type Match: {type_match} ({row['type']} vs {spell_type})")
            print(f"Class Match: {class_match} ({chosen_class} in {class_list})")
            print(f"Level Match: {level_match} ({row['level']} vs {level})")

            # If all conditions are true, append the spell
            if type_match and class_match and level_match:
                spells.append({"name": row["name"], "description": row["description"]})
                print(f"Matched: {row['name']}")

    if not spells:
        print("No matches found.")
    return spells


def main():
    spells = filter_spells(["damage"], "Cleric", "0")
    print("Filtered Spells:", spells)

if __name__ == "__main__":
    main()
