import sys
from utils.utils import pick_class, parser, load_map, load_npc, display_cmds, load_items
from action.Go import Go
from action.Fight import Fight
from action.Look import Look
from action.Stats import Stats
from action.Inventory import Inventory


HELP_MENU = "HELP MENU:"

if __name__ == "__main__":
    map = load_map()
    npcs = load_npc(map)
    user = pick_class(map)
    load_items(npcs)
    user.location.display()
    display_cmds()
    choice = None

    while (True):
        choice = input()
        cmd, noun = parser(choice)
        print(f"cmd: {cmd}, noun: {noun}\n\n")
        if cmd == "go" and noun is not None:
            Go(user, cmd, noun, map)
            user.location.display()
        elif cmd == "fight" and noun is not None:
            Fight(user, cmd, noun, map)
        elif (cmd == "look" or cmd == "l") and noun is None:
            Look(user, cmd, map)
        elif (cmd == "stats" or cmd == "s") and noun is None:
            Stats(user, cmd, map)
        elif (cmd == "inventory" or cmd == "i") and noun is None:
            Inventory(user, cmd, map)
        elif (cmd == "help" or cmd == "h") and noun is None:
            display_cmds(HELP_MENU)
        elif (cmd == "quit" or cmd == "q") and noun is None:
            print("\n\n")
            print("Thanks for playing!")
            sys.exit(0)
