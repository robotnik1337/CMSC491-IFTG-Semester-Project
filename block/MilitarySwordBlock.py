import block, location, character

from item import Item

class MilitarySwordBlock(block.Block):
    def __init__(self, location: location.Location, player: character.Character):
        self.location = location
        self.player = player

    def is_blocked(self) -> bool:
        return not self.player.is_trained