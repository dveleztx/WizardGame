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

        # Random Encounter
        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from a dark and foggy forest..."
              .format(active_creature.name, active_creature.level))
        print()

        # Input
        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ").lower()
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == "r":
            print("The wizard has become unsure of his power and flees!!!")
        elif cmd == "l":
            print("The wizard {} takes in the surroundings and sees: ".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        elif cmd == "x":
            print("Thanks for playing!")
            break
        else:
            print("Incorrect entry!")

        # If no creatures exist, end game
        if not creatures:
            print("You've defeated all the creatures, well done!")

        print()


# Invoke Main
if __name__ == "__main__":
    main()
