import block, location, character

from item import Item

OVINS_STONE_ITEM = Item(name="Ovin's Stone", description="a magical stone imbued with the power of Ovin, one of the past celestials who, in folklore, was deemed responsible for the curse of the Wycan Forest.")
AGBARA_BARK_ITEM = "bark placeholder :)"

class EnchantedStaffBlock(block.Block):
    def __init__(self, location: location.Location, player: character.Character):
        self.location = location
        self.player = player

    def is_blocked(self) -> bool:
        return False if OVINS_STONE_ITEM in self.player.inventory and AGBARA_BARK_ITEM in self.player.inventory else True