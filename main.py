import sys
from utils.utils import pick_class, parser, load_map, load_npc, display_cmds
from action.Go import Go
from action.View import View

HELP_MENU = "HELP MENU:"

if __name__ == "__main__":
    map = load_map()
    load_npc(map)
    user = pick_class(map)
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
        elif (cmd == "help" or cmd == "h") and noun is None:
            display_cmds(HELP_MENU)
        elif (cmd == "view" or cmd == "v") and noun is None:
            View(player=user, verb=cmd, map=map)
        elif (cmd == "quit" or cmd == "q") and noun is None:
            print("\n\n")
            print("Thanks for playing!")
            sys.exit(0)
