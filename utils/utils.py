from character.Player import Player, Warrior, Mage
from character.Npc import Npc
from location.Location import Location
from typing import Dict, List
from item.Item import Item, Weapon
from quest.Quest import Quest


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
            if id == 5:
                # Special case, bark in this location
                item = Item(name="Bark of Agbara",
                            description="The grand tree of Agbara was placed here by the hero Arun, legends say the celestial Simi bestowed the tree to Arun as her dying wish. Many who travel through here get a piece of the bark for good fortune.",
                            gettable=True)
                loc.add_item(item)
            elif id == 4:
                # Special case, sword in this location
                item = Weapon(name="Greatsword of Nerus",
                            description="Stuck in an engraved stone, there was a greatsword was used by the great Swordsman Nerus. One of the strongest warriors to have ever existed. Many have tried to pull the sword to no avail.", is_powerful = True)
                loc.add_item(item)
            map[loc.id] = loc
    return map


def load_npc(map: Dict[int, Location]) -> Dict[str, Npc]:
    """Loads in all NPCs and places them in their Locations

    Parameters:
        map (Dict[int, Location]): Game map, key: id, value: location
    """
    npcs = {}
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
            npcs[name] = npc
    return npcs


def load_items(npc_list: Dict[str, Npc]) -> None:
    """Loads in all Items and places them in their Locations or NPCs

    Parameters:
        map (Dict[int, Location]): Game map, key: id, value: location
        npc_list (Dict[str, Npc]): All NPCs in the game, key: name, value: Npc
    """
    for npc in npc_list.values():
        if npc.name == "Evil Imp":
            item = Item(name="Ovin's Stone", description="a magical stone imbued with the power of Ovin, one of the past celestials who, in folklore, was deemed responsible for the curse of the Wycan Forest.")
            npc.add_item(item)
        if npc.name == "Grand Mage Archilus":
            item = Weapon(name="Enchanted Staff", description = "A long staff with Ovin’s stone beaming at the top. One can feel an immense power radiating from the staff.", is_powerful=True)
            npc.add_item(item)
        if npc.name == "Omar":
            item = Weapon(name="Military Sword", description="A strong sword used by Miru militants.", is_powerful=True)
            npc.add_item(item)
        if npc.name == "Qayral":
            item = Item(name="Qayral's Scale", description="A shiny scale from the skin of a Qayral. There seems to be something radiating from it, making one feel very uneasy. Only those that have special abilities are able to get this scale of a Qayral.")
            npc.add_item(item)


def load_quests() -> Dict[str, List[Quest]]:
    """Loads quest objects in and creates a dictionary where
    quests["mage"] returns a list of Quest objects in order and 
    quests["warrior"] returns a list of Quest objects in order
    """
    pass


def pick_class(map: Dict[int, Location], quests: Dict[str, List[Quest]]) -> Player:
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
        weapon = Weapon(name="Knife", description="A small knife.", is_powerful=False)
        player_obj = Warrior(name=name, location=map[1], quest=quests["warrior"][0])
        player_obj.add_item(weapon)
        return player_obj
    else:
        print()
        print("----------------------------------------")
        print(f"You are now a **Mage**, {name} of Ashen")
        print("Your jouney begins...")
        print("----------------------------------------\n")
        weapon = Weapon(name="Wand", description="A small, sturdy wand.", is_powerful=False)
        player_obj = Mage(name=name, location=map[6], quest=quests["mage"][0])
        player_obj.add_item(weapon)
        return player_obj


def display_cmds(menu: str = "Available Commands:") -> None:
    """Displays information about actions and other commands

    Parameters:
        menu (str): Menu Name
    """
    print("\n\n")
    print(menu)
    commands = [
        ("go <direction>", "travel to another location"),
        ("fight <npc>", "fight an npc in the location"),
        ("look", "look around the area"),
        ("stats", "view your character stats"),
        ("quit or q", "quit the game"),
        ("help or h", "display this help menu"),
    ]

    for cmd, desc in commands:
        print(f" - {cmd:<15} -> {desc}")

    print("")


def parser(line: str) -> str:
    """Parser of user input"""
    words = [word.lower() for word in line.split()]
    return (words[0] if len(words) > 0 else None,
            words[1] if len(words) > 1 else None)
