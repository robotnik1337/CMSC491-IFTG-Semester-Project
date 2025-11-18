from typing import List
from block.Block import Block
from npc.Npc import Npc

# Default Values

DEF_ID = -1
DEF_NAME = "Location"
DEF_DESC = "Description"
DEF_DIRECTIONS = [-1, -1, -1, -1, -1]


class Location:
    """

    """

    def __init__(self, id: int = DEF_ID, name: str = DEF_NAME,
                 desc: str = DEF_DESC, block: Block = None,
                 npcs: List[Npc] = None,
                 directions: List[int] = DEF_DIRECTIONS):
        self.id = id
        self.name = name
        self.desc = desc
        self.block = block
        self.npcs = npcs
        self.directions = directions
