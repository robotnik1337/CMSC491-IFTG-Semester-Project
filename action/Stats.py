from action.Action import Action, Player
from location.Location import Location
from typing import Dict
from utils.utils import display_cmds

# Constants


class Stats(Action):
    """Action to look at your stats

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
        """Prints Stats"""
        print(f"Player Name: {self.player.name}")
        print(f"Player Class: {type(self.player).__name__}")
        print(f"Health Points: {self.player.hp}")
        print(f"Mana Points: {self.player.mana}")
        print("Inventory:")
        if not self.player.inventory:
            print("Your inventory is empty.\n")
        else:
            for item in self.player.inventory:
                print(f"{item.name}: {item.description}\n")