from character.Player import Player, Warrior, Mage
from character.Npc import Npc
from location.Location import Location
from typing import Dict


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
    print("Welcome to Chosen One")
    print("Player creation: \n")
    name = input("Hero Name: ")
    print()
    print("What class would you like your hero to be?")
    choice = input("\n1. Warrior \n2. Mage \n")
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Please pick 1 or 2: \n")
    print()
    print()
    if choice == "1":
        return Warrior(name=name, location=map[1])
    else:
        return Mage(name=name, location=map[6])


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


def addItemtoLocation(item, location):
    """Adds an item to a location's items list (handles missing 'items' attribute)."""
    if not hasattr(location, 'items') or location.items is None:
        location.items = []
    location.items.append(item)
