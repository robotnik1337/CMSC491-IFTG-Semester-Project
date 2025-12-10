# View.py

from action.Action import Action, Player
from location.Location import Location
from typing import Dict, Tuple

# Constants
SUCCESS = "You view your surroundings."

class View(Action):
    """
    Action to display the items and NPCs in the player's current location.
    
    Keywords: v, view
    """

    def __init__(self, player: Player | None = None,
                 verb: str = None, noun: str = None,
                 map: Dict[int, Location] | None = None) -> None:
        """Initializes the Action subclass View"""
        # Note: The view command doesn't typically need a 'noun', but we register the verb itself.
        # We pass 'None' as the noun since it's not a directional move.
        super().__init__(player, verb, None) 
        self.execute()

    def can_execute(self) -> bool:
        """View can always be executed if the player is in a location."""
        return True

    def execute(self) -> None:
        """Displays the items and NPCs in the player's current location."""
        
        # We access the location directly from the player object, which is set in super().__init__
        current_location = self.player.location
        output = []

        # 1. Display Items
        # Use hasattr() to safely check for the 'items' attribute 
        # because Location.py was not modified to include it.
        if hasattr(current_location, 'items') and current_location.items:
            output.append("\nItems you see here:")
            for item in current_location.items:
                # Assuming Item object has 'name' and 'description' attributes
                output.append(f"  - **{item.name}**: {item.description}")
        else:
            output.append("\nYou don't see any items here.")

        # 2. Display NPCs
        if current_location.npcs:
            output.append("\nPeople you see here:")
            for npc in current_location.npcs:
                # Assuming Npc object has a 'name' attribute
                output.append(f"  - {npc.name}")

        # 3. Print the combined output
        self.display_result(f"{SUCCESS}\n" + "\n".join(output) + "\n")
        
    def display_result(self, msg: str) -> None:
        """Prints the result message."""
        print(msg)