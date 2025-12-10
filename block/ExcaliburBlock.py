import block, location, character

from character.Player import Warrior

class ExcaliburBlock(block.Block):
    def __init__(self, location: location.Location, player: character.Player):
        super().__init__()
        self.location = location
        self.player = player
    
    def is_blocked(self) -> bool:
        return False if isinstance(self.player, Warrior) and self.player.chosen else True