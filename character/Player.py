from typing import List
from character.Character import Character, Item
from location.Location import Location


class Player(Character):
    """Child class of Character, represting the Player

    Attributes:
        location (Location): Current location of the player
    """

    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 0, mana: int = 0,
                 location: Location | None = None) -> None:
        super().__init__(name, inventory, hp, mana)
        self.location = location

    def set_location(self, location: Location) -> None:
        self.location = location

class Mage(Player):
    """Child class of Player, represting the Player class Mage. Sets HP and Mana for the class

    Attributes:
        classname (str): Name of the class
    """
    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 0, mana: int = 0,
                 location: Location | None = None) -> None:
        super().__init__(name, inventory, hp, mana, location)
        self.classname = "Mage"
        self.hp = 70
        self.mana = 150    


class Warrior(Player):
    """Child class of Player, represting the Player class Warrior. Sets HP and Mana for the class

    Attributes:
        classname (str): Name of the class
    """
    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 0, mana: int = 0,
                 location: Location | None = None) -> None:
        super().__init__(name, inventory, hp, mana, location)
        self.classname = "Warrior"
        self.hp = 150
        self.mana = 50