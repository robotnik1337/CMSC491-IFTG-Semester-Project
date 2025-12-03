from utils.utils import pick_class, parser, load_map
from action.Go import Go

if __name__ == "__main__":
    map = load_map()
    user = pick_class(map)
    user.location.display()
    choice = None
    while (choice != 'q'):
        choice = input()
        cmd, noun = parser(choice)
        print(f"cmd: {cmd}, noun: {noun}\n\n")
        if cmd == "go" and noun is not None:
            Go(user, cmd, noun, map)
            user.location.display()
