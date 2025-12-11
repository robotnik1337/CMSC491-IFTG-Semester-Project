from action.Action import Action, Player
from location.Location import Location
from typing import Dict

# Constants

SUCCESS = "Fought and won against "
FAILURE = "Fought and lost against "
HINT = ". Maybe a more powerful weapon could be of use!"
DAMAGE = "Took 10 damage!"
POWERFUL_DAMAGE = "Took 20 damage!"
UNABLE = " is not a foe. "


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
        self.enemy_npc = None
        self.execute()
        

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
            weapon = False
            powerful_weapon = False
            for item in self.player.inventory:
                if type(item).__name__ == "Weapon":
                    weapon = True
                    if item.is_powerful:
                        powerful_weapon = True
            if self.enemy_npc.name == "Qayral":
                if powerful_weapon:
                    #remove npc from location
                    self.display_result(SUCCESS + self.enemy_npc.name)
                    for item in self.enemy_npc.inventory:
                        self.player.inventory.append(item)
                        self.display_result(f"Recieved {item.name}.")
                    self.current_loc.remove_npc(self.enemy_npc)
                else:
                    self.display_result(FAILURE + self.enemy_npc.name + HINT)
                    self.display_result(POWERFUL_DAMAGE)
                    self.player.hp -= 20
            elif self.enemy_npc.name == "Old Mage Supreme Sotek":
                if powerful_weapon:
                    #remove npc from location
                    self.display_result(SUCCESS + self.enemy_npc.name)
                    for item in self.enemy_npc.inventory:
                        self.player.inventory.append(item)
                        self.display_result(f"Recieved {item.name}.")
                    self.current_loc.remove_npc(self.enemy_npc)
                else:
                    self.display_result(FAILURE + self.enemy_npc.name + HINT)
                    self.display_result(POWERFUL_DAMAGE)
                    self.player.hp -= 20
            else:
                if weapon:
                    #remove npc from location
                    self.display_result(SUCCESS + self.enemy_npc.name)
                    for item in self.enemy_npc.inventory:
                        self.player.inventory.append(item)
                        self.display_result(f"Recieved {item.name}.")
                    self.current_loc.remove_npc(self.enemy_npc)
                else:
                    self.display_result(FAILURE + self.enemy_npc.name)
                    self.display_result(DAMAGE)
                    self.player.hp -= 10
        else:
            if self.enemy_npc == None:
                self.display_result(f"{self.noun} is not a npc in this location.")
                return
            self.display_result(self.enemy_npc.name + UNABLE)