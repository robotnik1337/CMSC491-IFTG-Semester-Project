from action.Action import Action
from character.Player import Player, Mage, Warrior
from quest.Quest import Quest
from dialogue.Dialogue import generate_dialogue

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
            if isinstance(self.player, Mage):
                if self.other.name == "Grand Mage Archilus":
                    if self.player.stage == 0:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)
                    elif self.player.stage == 1:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)
                        
                        # Mage gives materials to Archilus to craft enchanted staff
                        for item in self.player.inventory:
                            if item.name == "Ovin's Stone":
                                self.other.inventory.append(item)
                                self.player.inventory.remove(item)
                                self.display_result("You gave the Grand Mage Ovin's Stone")
                            if item.name == "Bark of Agbara":
                                self.other.inventory.append(item)
                                self.player.inventory.remove(item)
                                self.display_result("You gave the Grand Mage the Bark of Agbara")
                        
                        for item in self.other.inventory:
                            if item.name == "Enchanted Staff":
                                self.player.inventory.append(item)
                                self.other.inventory.remove(item)
                                self.display_result("You've received the Enchanted Staff!")
                        
                    elif self.player.stage == 2:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)
                    else:
                        self.display_result(self.other.name + ": " + self.other.default_dialogue)

                elif self.other.name == "Old Mage Supreme Sotek":
                    if self.player.stage == 3:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)
                    else:
                        self.display_result(self.other.name + ": " + self.other.default_dialogue)
                else:
                    self.display_result(self.other.name + ": " + self.other.default_dialogue)
            
            elif isinstance(self.player, Warrior):
                if self.other.name == "Lieutenant Omar":
                    if self.player.stage == 0:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)

                        # After training, Warrior gets military sword
                        for item in self.other.inventory:
                            if item.name == "Military Sword":
                                self.player.inventory.append(item)
                                self.other.inventory.remove(item)
                                self.display_result("Lieutenant Omar gave you a Military Sword")
                        
                    elif self.player.stage == 1:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)

                    elif self.player.stage == 2:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)

                        # Warrior gives Qayral scale to Omar
                        for item in self.player.inventory:
                            if item.name == "Qayral's Scale":
                                self.other.inventory.append(item)
                                self.player.inventory.remove(item)
                                self.display_result("You gave Lieutenant Omar the Qayral's Scale")

                        self.player.is_chosen = True

                    elif self.player.stage == 3:
                        dialogue = generate_dialogue(self.player.quest, self.player, self.other)
                        self.display_result(self.other.name + ": " + dialogue)

                    # no dialogue need for stage 4 (i.e. quest 5, the final quest)
                    else:
                      self.display_result(self.other.name + ": " + self.other.default_dialogue)
                else:
                    self.display_result(self.other.name + ": " + self.other.default_dialogue)
