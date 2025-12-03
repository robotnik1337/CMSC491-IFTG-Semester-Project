from action.Action import Action, Player
from location.Location import Location, DIRECTION_MAP
from typing import Dict

# Constants

SUCCESS = "Traveled"


class Go(Action):
    """Action to move between locations

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None,
                 map: Dict[int, Location] | None = None) -> None:
        """Initializes the Action subclass Go"""
        if noun in DIRECTION_MAP:
            direction = DIRECTION_MAP[noun]
        super().__init__(player, verb, direction)
        self.current_loc = player.location
        self.execute(map)

    def can_execute(self) -> bool:
        """Checks if the chosen direction is a valid exit"""
        return self.current_loc.valid_exit(self.noun)

    def execute(self, map: Dict[int, Location]) -> None:
        """Moves the Player to the new location"""
        if self.can_execute():
            #  if noun is a proper direction
            mov_id = self.current_loc.dir_to_id(self.noun)
            if map[mov_id].block is not None:
                #  if there is a block on the Location
                print("Location can't be reached\n")
                #  add functionality here based on block class once implemented
                return
            if mov_id in map:
                location = map[mov_id]
                self.player.set_location(location)
                self.display_result(f"{SUCCESS} {self.noun}...\n")
