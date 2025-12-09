from typing import List
from block.Block import Block
from character.Npc import Npc

# Default Values

DEF_ID = -1
DEF_NAME = "Location"
DEF_DESC = "Description"
DEF_DIRECTIONS = [-1, -1, -1, -1, -1]

# Other Constants

DIRECTION_MAP = {
    "n": "north",
    "north": "north",
    "e": "east",
    "east": "east",
    "s": "south",
    "south": "south",
    "w": "west",
    "west": "west"
}

DIR_TO_INDEX = {
    "north": 0,
    "east": 1,
    "south": 2,
    "west": 3
}


class Location:
    """Represents a location within the IF game, or a tile on the map

    Attributes:
        id (int): Unique int for Location
        name (str): Name of Location obj
        desc (str): Description of Location
        block (Block | None): Block of Location if one exists
        npcs (List[Npc] | None): List of Npcs at Location if they exists
        directions (List[int]): [north, east, south, west, in/out] where
                                 each index is an id of a location or -1
    """

    def __init__(self, id: int = DEF_ID, name: str = DEF_NAME,
                 desc: str = DEF_DESC, block: Block | None = None,
                 npcs: List[Npc] | None = [],
                 directions: List[int] = DEF_DIRECTIONS):
        """Initializes Location"""
        self.id = id
        self.name = name
        self.desc = desc
        self.block = block
        self.npcs = npcs if npcs is not None else []
        self.directions = directions
        self.items = []  # list of items at location

    def display(self):
        """Outputs infomation of the Location for the Player"""
        island = True  # Stays False if no exits
        print(f"Location: **{self.name}**")
        print(f"Description:\n{self.desc}\n")
        print("Exits:")

        if self.directions[0] > -1:
            print("\t- North")
            island = False
        if self.directions[1] > -1:
            print("\t- East")
            island = False
        if self.directions[2] > -1:
            print("\t- South")
            island = False
        if self.directions[3] > -1:
            print("\t- West")
            island = False

        if island:
            print("None", end="")
        print()

    def valid_exit(self, noun: str) -> bool:
        """Checks if the direction passed in is a valid Exits

        Attributes:
            noun (str): could be any string the parser accepts
        """
        if noun in DIRECTION_MAP:
            dir = DIRECTION_MAP[noun]
            idx = DIR_TO_INDEX[dir]
            if self.directions[idx] > -1:
                return True

        return False

    def dir_to_id(self, noun: str) -> int:
        """Returns the location id of the direction from
        this location

        Attributes:
            noun (str): could be any string the parser accepts
        """
        if noun in DIRECTION_MAP:
            dir = DIRECTION_MAP[noun]
            idx = DIR_TO_INDEX[dir]
            return self.directions[idx]

        return -1

    def add_npc(self, npc: Npc) -> None:
        """Adds Npc to Location

        Parameters:
            npc (Npc): character
        """
        self.npcs.append(npc)
