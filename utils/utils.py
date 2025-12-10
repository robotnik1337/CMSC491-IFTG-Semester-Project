from character.Player import Player, Warrior, Mage
from character.Npc import Npc
from location.Location import Location
from typing import Dict
from item.Item import Item, Weapon


def load_map() -> Dict[int, Location]:
    """Loads in all Locations into a dictionary"""
    map = {}
    with open("utils/491_map.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            chunks = [chunk.strip() for chunk in line.split('|')]
            id = int(chunks[0])
            name = chunks[1]
            desc = chunks[2]
            directions = [int(chunks[3]), int(chunks[4]),
                          int(chunks[5]), int(chunks[6])]
            loc = Location(id=id, name=name, desc=desc, directions=directions)
            map[loc.id] = loc
    return map


def load_npc(map: Dict[int, Location]) -> None:
    """Loads in all NPCs and places them in their Locations

    Parameters:
        map (Dict[int, Location]): Game map, key: id, value: location
    """
    with open("utils/491_npc.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            chunks = [chunk.strip() for chunk in line.split('|')]
            name = chunks[0]
            loc_id = int(chunks[1])
            desc = chunks[2]
            is_fightable = bool(int(chunks[3]))
            npc = Npc(name=name, desc=desc, is_fightable=is_fightable)
            map[loc_id].add_npc(npc)  # Add loaded Npc into current Location


def pick_class(map: Dict[int, Location]) -> Player:
    """Character creation

    Parameters:
        map (Dict[int, Location]): Game map, key: id, value: location
    """
    print("---------------------")
    print("Welcome to Chosen One")
    print("---------------------")
    print("\nChoose your class to begin your journey.\n")
    print("What class would you like your hero to be: 1. Warrior or 2. Mage?")
    choice = input("> ")
    while choice not in ["1", "2"]:
        print("Invalid choice. Please pick 1 or 2.")
        choice = input("> ")
    print("\nEnter your character name:")
    name = input("> ")
    if choice == "1":
        print()
        print("------------------------------------------")
        print(f"You are now a **Warrior**, {name} of Miru")
        print("Your journey begins...")
        print("------------------------------------------\n")
        weapon = Weapon(name="Knife", description="A small knife.")
        player_obj = Warrior(name=name, location=map[1])
        player_obj.add_item(weapon)
        return player_obj
    else:
        print()
        print("----------------------------------------")
        print(f"You are now a **Mage**, {name} of Ashen")
        print("Your jouney begins...")
        print("----------------------------------------\n")
        weapon = Weapon(name="Wand", description="A small, sturdy wand.")
        player_obj = Mage(name=name, location=map[6])
        player_obj.add_item(weapon)
        return player_obj


def display_cmds(menu: str = "Available Commands:") -> None:
    """Displays information about actions and other commands

    Parameters:
        menu (str): Menu Name
    """
    print("\n\n")
    print(menu)
    print(" - go <direction>\t-> travel to another location")
    print(" - fight <npc>\t-> fight an npc in the location")
    print(" - look\t\t-> look around the area")
    print(" - stats\t\t-> view your character stats")
    print(" - quit or q\t-> quit the game")
    print(" - help or h\t-> display this help menu")
    print("")


def parser(line: str) -> str:
    """Parser of user input"""
    words = [word.lower() for word in line.split()]
    return (words[0] if len(words) > 0 else None,
            words[1] if len(words) > 1 else None)
