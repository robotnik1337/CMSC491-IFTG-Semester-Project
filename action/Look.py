from action.Action import Action, Player
from location.Location import Location
from typing import Dict

# Constants


class Look(Action):
    """Action to look at whats in a location

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, 
                 map: Dict[int, Location] | None = None) -> None:
        """Initializes the Action subclass Look"""

        super().__init__(player, verb)
        self.current_loc = player.location
        self.execute(map)

    def execute(self, map: Dict[int, Location]) -> None:
        """Print description, npcs, items"""
        self.current_loc.display()
        #  if noun is a proper direction
        print("NPC's:")
        for npc in self.current_loc.npcs:
            print(f"You see {npc.name}: {npc.desc}\n")
        print("Items:")
        if not self.current_loc.items:
            print("There are no items here.\n")
        else:
            for item in self.current_loc.items:
                print(f"You see {item.name}: {item.desc}\n")

        self.display_result("Looked around the area...")