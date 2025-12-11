from item.Item import Item
from action.Action import Action
from character.Player import Player


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
        self.execute()

    def can_execute(self, item: Item | None = None) -> bool:
        """Check's if item is gettable"""
        if isinstance(item, Item):
            return item.is_gettable
        return False

    def execute(self) -> None:
        """Attempts to get an item"""
        item_exists = False
        item_obj = None
        # Does item exist?
        for item in self.current_loc.items:
            if item.name.lower() == self.noun:
                item_exists = True
                item_obj = item

        # Is item obtainable?
        if item_exists:
            if self.can_execute(item_obj):
                self.display_result(f"Picked up {item_obj.name}.")
                self.player.add_item(item_obj)
                self.current_loc.remove_item(item_obj)
                return
            else:
                self.display_result(f"Can't seem to get the {item_obj}.")
                return

        self.display_result(f"{self.noun} does not exist in {self.current_loc.name}.")
