from action.Action import Action, Player
from location.Location import Location
from typing import Dict

# Constants

SUCCESS = "Fought and won against "
FAILURE = "Fought and lost against "
DAMAGE = "Took 10 damage!"
UNABLE = "Cannot fight "


class Fight(Action):
    """Action to move between locations

    Attributes:
        current_loc (Location): Holds the current location of the player

    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None,
                 map: Dict[int, Location] | None = None) -> None:
        """Initializes the Action subclass Fight"""
        
        super().__init__(player, verb, noun)
        self.current_loc = player.location
        self.execute()
        self.enemy_npc =None


    def can_execute(self) -> bool:
        """Checks if the character in the location is fightable"""
        for npc in self.current_loc.npcs:
            if self.noun.lower() in npc.name.lower():
                self.enemy_npc = npc
                return npc.is_fightable
        return False

        

    def execute(self) -> None:
        """Fight the targeted NPC"""
        if self.can_execute():
            #simple fight, if user has weapon, they win, very simple
            if self.player.inventory is not None:
                for item in self.player.inventory:
                    if type(item).__name__ == "Weapon":
                        
                        #remove npc from location
                        for item in self.enemy_npc.inventory:
                            self.player.inventory.append(item)
                        self.current_loc.remove_npc(self.enemy_npc)
                        self.display_result(SUCCESS + self.enemy_npc.name)
                        return
            self.display_result(FAILURE + self.enemy_npc.name)
            self.display_result(DAMAGE)
            self.player.hp -= 10
        else:
            self.display_result(UNABLE +self.enemy_npc.name)
