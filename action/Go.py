from action.Action import Action, Player


class Go(Action):
    """Action to move between locations

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None) -> None:
        """Initializes the Action subclass Go"""
        super().__init__(player, verb, noun)
        self.current_loc = player.locations

    def can_execute(self) -> bool:
        """Checks if the chosen direction is a valid exit"""
        return self.current_loc.valid_exit(self.noun)

    def execute(self) -> None:
        """Moves the Player to the new location"""
        if self.can_execute():
            mov_id = self.current_loc.dir_to_id(self.noun)
            # TODO: Use id to change location via some location LookupError
            pass
