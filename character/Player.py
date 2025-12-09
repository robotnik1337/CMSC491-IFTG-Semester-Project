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
        classdesc (str): Description of the class
    """

    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 70, mana: int = 150,
                 location: Location | None = None) -> None:
        super().__init__(name, inventory, hp, mana, location)
        self.classname = "Mage"
        self.classdesc = "A young mage from Ashen who desires to become one of the greatest mages to exist, a Mage Supreme. After the death of their father due to the evil that surrounds Ashen, they seek to gain more power to protect themselves and their loved ones."


class Warrior(Player):
    """Child class of Player, represting the Player class Warrior. Sets HP and Mana for the class

    Attributes:
        classname (str): Name of the class
        classdesc (str): Description of the class
    """

    def __init__(self, name: str = "", inventory: List[Item] | None = None,
                 hp: int = 150, mana: int = 50,
                 location: Location | None = None) -> None:
        super().__init__(name, inventory, hp, mana, location)
        self.classname = "Warrior"
        self.classdesc = "A young warrior from Miru, inspired by their older brother’s military experience, who wants to become strong enough to swing their own sword and defend their family and community from the Qayral."
