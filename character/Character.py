from typing import List
from item.Item import Item


class Character:
    """Base class for the living characters within the game

    Attributes:
        name (str): name of the characters
        inventory (List[Item]): list of items within characters inventory
        hp (int): amount of health the character has
        mana (int): amount of mana the character has
    """

    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 0, mana: int = 0) -> None:
        """Initializes the Base Character Class"""
        self.name = name
        self.inventory = inventory
        self.hp = hp
        self.mana = mana
