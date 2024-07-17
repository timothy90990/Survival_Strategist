# Text based dungeon game fighting bosses such as "anxiety, depression, etc" using
# items such as "antidepressant, relaxation, etc". Needs mockup for a map and to
# rename bosses, items, and rooms. Add more bosses between rooms in the gameplay
# loop to flesh it out. Make type text prompt for the beginning.

import os
from PIL import Image

# Opens 'Map.jpeg' on program start.
img = Image.open('Map.jpeg')
img.show()

# Display starting menu
def prompt():
    print("\t\tWelcome to 'GAME NAME'\n\n\
You must collect all six items before fighting the boss.\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'get {item}' (add nearby item to inventory)\n")

    input("Press any key to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
# Item names must start with a capital due to '.title' being used.
rooms = {
    'roomOne': {'North': 'roomTwo', 'South': 'roomThree', 'East': 'roomFive'},
    'roomTwo': {'South': 'roomOne', 'Item': 'One'},
    'roomThree': {'North': 'roomOne', 'East': 'roomFour', 'Item': 'Two'},
    'roomFive' : {'West': 'roomOne', 'North': 'roomSix', 'East': 'roomEight', 'Item': 'Four'},
    'roomSix' : {'South': 'roomFive', 'East': 'roomSeven', 'Item': 'Five'},
    'roomSeven': {'West': 'roomSix', 'Item': 'Six'},
    'roomFour': {'West': 'roomThree', 'Item': 'Three'},
    'roomEight': {'West': 'roomFive', 'Boss': 'Boss'}
    }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
currentRoom = "roomOne"

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print(f"You are in the {currentRoom}\nInventory : {inventory}\n{'-' * 27}")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in rooms[currentRoom].keys():

        nearbyItem = rooms[currentRoom]["Item"]

        if nearbyItem not in inventory:

            if nearbyItem[-1] == 's':
                print(f"You see {nearbyItem}")

            elif nearbyItem[0] in vowels:
                print(f"You see an {nearbyItem}")

            else:
                print(f"You see a {nearbyItem}")
    
    # Boss encounter
    if "Boss" in rooms[currentRoom].keys():

        # Lose
        if len(inventory) < 6:
            print(f"You lost a fight with {rooms[currentRoom]['Boss']}.")
            break

        # Win
        else:
            print(f"You beat {rooms[currentRoom]['Boss']}!")
            break

    # Accepts player's move as input
    userInput = input("Enter your move:\n")

    # Splits move into words
    nextMove = userInput.split(' ')

    # First word is action ('.title' allows for input to be in capitals or lowercase.)
    action = nextMove[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(nextMove) > 1:
        item = nextMove[1:]
        direction = nextMove[1].title()

        # Item can be two words.
        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            currentRoom = rooms[currentRoom][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."
    
    # Picking up items
    elif action == "Get":
        # Try to find item in room.
        try:
            if item == rooms[currentRoom]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[currentRoom]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        # Incase user attempts to find item that does not exist in the room.
        except:
            msg = f"Can't find {item}"
    
    # Exit program by typing in 'Exit'.
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid command."