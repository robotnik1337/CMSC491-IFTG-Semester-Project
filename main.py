from utils.utils import pick_class, parser
from location.Location import Location

if __name__ == "__main__":
    loc = Location(0, "Trial", "super insane location with amazing dragon wow",
                   None, None, [-1, 1, 0, -1, -1])
    loc.display()
    class_choice = pick_class()
    print(f"You picked option {class_choice}")
