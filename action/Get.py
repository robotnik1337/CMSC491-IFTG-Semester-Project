from item.Item import Item
from action.Action import Action
from character.Player import Player, Warrior


class Get(Action):
    """Get action, player attempts to get an item from environment

    Attributes:
        current_loc (Location): Holds the current location of the player
    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None) -> None:
        """Initializes Get Class"""
        super().__init__(player, verb, noun)
        self.current_loc = player.location
        self.item = None  # item in question
        self.execute()

    def can_execute(self) -> bool:
        """Check's if item is gettable"""
        for item in self.current_loc.items:
            if self.noun.lower() in item.name.lower():
                is_gettable = item.is_gettable
                self.item = item
                return is_gettable
        return False

    def execute(self) -> None:
        """Attempts to get an item"""
        if self.can_execute():
            self.get_item()
            return
        else:
            if self.item is None:
                self.display_result(f"{self.noun} can't be found in {self.current_loc.name} right now.")
                return
            elif self.item.name == "Greatsword of Nerus":
                if isinstance(self.player, Warrior):
                    if self.player.is_chosen:
                        self.get_item()
                    else:
                        self.display_result(f"One must be chosen to pull and wield the Greatsword of Nerus")
                else:
                    self.display_result(f"A mage could never become chosen to weild the Greatsword of Nerus!")
            else:
                self.display_result(f"{self.item.description}")
            

    def get_item(self) -> None:
        """Puts item in Player's inventory and removes it from Location"""
        self.player.add_item(self.item)
        self.current_loc.remove_item(self.item)
        if self.item.name == "Greatsword of Nerus":
            # The stone remains
            self.current_loc.add_item(Item(name="Engraved Stone",
                                           description="An empty but engraved stone rests here. No sword in sight.",
                                           gettable=False))
        elif self.item.name == "Bark of Agbara":
            # The tree remains
            self.current_loc.add_item(Item(name="Tree of Agbara",
                                           description="The grand tree of Agbara stands here: Seems rather bare.",
                                           gettable=False))
        self.display_result(f"Picked up {self.item.name}.")