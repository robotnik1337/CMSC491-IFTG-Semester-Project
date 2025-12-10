from action.Action import Action, Player
from location.Location import Location
from typing import Dict
from utils.utils import display_cmds

# Constants


class Inventory(Action):
    """Action to look at your inventory

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, 
                 map: Dict[int, Location] | None = None) -> None:
        """Initializes the Action subclass Look"""

        super().__init__(player, verb)
        self.current_loc = player.location
        self.execute()

    def execute(self) -> None:
        """Prints Inventory"""
        print("Inventory:")
        for item in self.player.inventory:
            print(f"{item.name}: {item.description}")
