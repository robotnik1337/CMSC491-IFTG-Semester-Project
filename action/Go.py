from action.Action import Action, Player

# Constants

SUCCESS = "Traveled "
LOC_MAP = {

}


class Go(Action):
    """Action to move between locations

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None) -> None:
        """Initializes the Action subclass Go"""
        super().__init__(player, verb, noun)
        self.current_loc = player.location

    def can_execute(self) -> bool:
        """Checks if the chosen direction is a valid exit"""
        return self.current_loc.valid_exit(self.noun)

    def execute(self) -> None:
        """Moves the Player to the new location"""
        if self.can_execute():
            mov_id = self.current_loc.dir_to_id(self.noun)
            if mov_id in LOC_MAP:
                location = LOC_MAP[mov_id]
                self.player.set_location(location)
                self.display_result(f"{SUCCESS} {self.noun}")
            pass
