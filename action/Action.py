from character.Player import Player


class Action:
    """Base class for all interactive fiction actions

    Attributes:
        player (Player): Holds the Player object, which has location and other
                         information about current game state
        verb (str): the verb extracted from the parser
        noun (str): the noun extracted from the parser

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None):
        """Initializes Base Action Class"""
        self.player = player
        self.verb = verb
        self.noun = noun

    def can_execute(self):
        """Checks if action is possible in current game state.
        Subclasses should override this logic
        """
        return True

    def execute(self):
        """Performs the action and updates the game state.
        Subclasses must override this method
        """
        not_implemented = "Subclasses must implement the execute method"
        raise NotImplementedError(not_implemented)

    def display_result(self, msg):
        """Displays the result of the players action"""
        print(msg)
