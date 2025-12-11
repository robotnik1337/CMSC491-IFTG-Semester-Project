import sys
from utils.utils import pick_class, parser, load_map, load_npc, display_cmds, load_items, load_quests
from action.Go import Go
from action.Fight import Fight
from action.Look import Look
from action.Stats import Stats
from action.Inventory import Inventory
from action.Get import Get
from action.Talk import Talk
from character.Player import Mage, Warrior


HELP_MENU = "HELP MENU:"

if __name__ == "__main__":
    map = load_map()
    quests = load_quests()
    npcs = load_npc(map)
    user = pick_class(map, quests)
    load_items(npcs)
    user.location.display()
    display_cmds()
    choice = None

    while (True):
        choice = input("> ")
        cmd, noun = parser(choice)
        if cmd == "go" and noun is not None:
            Go(user, cmd, noun, map)
            user.location.display()
        elif (cmd == "get" or cmd == "grab" or cmd == "pull") and noun is not None:
            Get(user, cmd, noun)
        elif cmd == "fight" and noun is not None:
            Fight(user, cmd, noun, map)
        elif cmd == "talk" and noun is not None:
            Talk(user, cmd, noun)
        elif (cmd == "look" or cmd == "l") and noun is None:
            Look(user, cmd, map)
        elif (cmd == "stats" or cmd == "s") and noun is None:
            Stats(user, cmd, map)
        elif (cmd == "inventory" or cmd == "i") and noun is None:
            Inventory(user, cmd, map)
        elif (cmd == "help" or cmd == "h") and noun is None:
            display_cmds(HELP_MENU)
        elif (cmd == "quit" or cmd == "q") and noun is None:
            print()
            print("Thanks for playing!")
            sys.exit(0)
        else:
            print("Invalid command: Type h or help to see all the valid commands!")

        if user.hp <= 0:
            print()
            print("Oh no! You have died.")
            sys.exit(0)
        
        if isinstance(user, Mage):
            if len(map[4].npcs) == 0:
                print()
                print("You defeated one of the greatest mages in history!")
                print(f"You are now the strongest mage in Arun, the Mage Supreme {user.name}")
                sys.exit(0)
        
        if isinstance(user, Warrior):
            for item in user.inventory:
                if item.name == "Greatsword of Nerus":
                    print()
                    print("You became chosen wield the Greatsword of Nerus, and to protect the land of Arun.")
                    print(f"You are now the strongest warrior in Arun, the Champion of the Warriors {user.name}")
                    sys.exit(0)