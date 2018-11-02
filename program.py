# Program    : Wizard Game
# Author     : David Velez
# Date       :
# Description: Wizard Game based on Harry Potter lore

# Imports
import random
import time
from actors import Creature, Wizard, Dragon, SmallCreature


# Main Function
def main():
    print_header()
    game_loop()


# Print the Header
def print_header():
    print("----------------------------")
    print("      Wizard Game App")
    print("----------------------------")
    print()


# Game Logic
def game_loop():

    # Create Creature Objects
    creatures = [
        SmallCreature("Goblin", 3),
        Dragon("Ridgeback", 10, 20, True),
        Wizard("DeathEater", 12),
        Wizard("Voldemort", 19),
        Creature("Troll", 8)
    ]

    # Create Hero Object
    hero = Wizard("David", 10)

    # Play the Game
    while True:



        print()


# Invoke Main
if __name__ == "__main__":
    main()
