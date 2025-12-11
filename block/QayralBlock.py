import block, location, character

from item import Item

class QayralBlock(block.Block):
    def __init__(self, location: location.Location, qayral: character.Npc):
        self.location = location
        self.qayral = qayral

    def is_blocked(self) -> bool:
        return self.qayral.is_alive