def pick_class():
    print("What class would you like to be?")
    choice = input("\n1. Warrior \n2. Mage \n")
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Please pick 1 or 2: \n")
    return "Warrior" if choice == "1" else "Mage"


def parser():
    pass
