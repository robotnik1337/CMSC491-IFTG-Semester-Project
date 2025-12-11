from action.Action import Action
from character.Player import Player, Mage, Warrior
from quest.Quest import Quest

class Talk(Action):
    """

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None):
        """Initializes Base Action Class"""
        super().__init__(player, verb, noun)
        self.current_loc = player.location
        self.other = None  # This is the other npc
        self.execute()

    def can_execute(self):
        """Checks if the character in the location is able to be talked to"""
        for npc in self.current_loc.npcs:
            if self.noun.lower() in npc.name.lower():
                self.other = npc
                return npc.is_talkable
        return False
       
    def execute(self):
        """"""
        if self.can_execute():
            if self.other.name == "Grand Mage Archilus" and isinstance(self.player, Mage):
                if self.player.stage == 0:
                    self.display_result("Archilus talks")