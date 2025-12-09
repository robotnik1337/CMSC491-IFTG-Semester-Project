from typing import List
from character.Character import Character
from item.Item import Item


class Npc(Character):
    """Child class of Character, representing living characters within the world
    that are not the player themself
    """

    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 100, mana: int = 20,
                 desc: str = ""):
        super().__init__(name, inventory, hp, mana)
        self.desc = desc
