class Item:
    def __init__(self, name: str = "", description: str = "", gettable: bool = None) -> None:
        """
        Initializes the Base Item Class
        """
        self.name = name
        self.description = description
        self.gettable = gettable



class Weapon(Item):
    """Child class of Item, representing a Weapon

    Attributes:
        damage (int): amount of damage the weapon can deal
        mana_cost (int): amount of mana required to use the weapon
    """

    def __init__(self, name: str = "", description: str = "", gettable: bool = None,
                 damage: int = 0, mana_cost: int = 0) -> None:
        super().__init__(name, description)
        self.damage = damage
        self.mana_cost = mana_cost



class Armor(Item):
    """Child class of Item, representing Armor

    Attributes:
        defense (int): amount of defense the armor provides
    """

    def __init__(self, name: str = "", description: str = "", gettable: bool = None,
                 defense: int = 0) -> None:
        super().__init__(name, description)
        self.defense = defense