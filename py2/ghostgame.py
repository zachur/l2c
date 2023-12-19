# Ghost Game

# Game Setup
from random import randint
print("Ghost Game")
feeling_brave = True
score = 0

# Main Loop
while feeling_brave:
    ghost_door = randint(1,3)
    print("Three doors ahead...")
    print("A ghost behind one.")
    print("Which door do you open?")
    door = input("1, 2, or 3? ")
    door_num = int(door)

    # Branching Part
    if door_num == ghost_door:
        print("GHOST!")
        feeling_brave = False
    else:
        print("No ghost!")
        print("You enter the next room.")
        score = score + 1

# Game Ending
print("Run away!")
print("Game over! You scored", score)
