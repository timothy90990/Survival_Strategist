from src.config import ROOMS as rooms
from src.config import ROOM_POSITION as room_positions
from src.config import QUOTES_PATH as quotes_path

class Player:
    """
    Module: Player
    Date: 8/6/24
    Programmer: Timothy Stowe
    
    Purpose: This class represents the player in the game, managing their current room
    and inventory. It provides methods for player movement and item collection.
    
    Version: 1.0
    RTM: 001
    """
    def __init__(self, start_room):
        """
        Module: Player.__init__
        Date: 8/6/24
        Programmer: Timothy Stowe
        
        Purpose: Initializes a new Player object with a starting room and an empty inventory.
        
        Version: 1.0
        RTM: 002
        """
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        """
        Module: Player.move
        Date: 8/6/24
        Programmer: Timothy Stowe
        
        Purpose: Moves the player in the specified direction if possible, updating their
        current room and returning a message about the movement.
        
        Version: 1.2
        RTM: 003
        """
        try:
            new_room = rooms[self.current_room][direction]
            self.current_room = new_room
            return f"You travel {direction}"
        except KeyError:
            return "You can't go that way."

    def get_item(self, item, rooms):
        """
        Module: Player.get_item
        Date: 8/6/24
        Programmer: Timothy Stowe
        
        Purpose: Attempts to add an item to the player's inventory if it's present in the
        current room and not already in the inventory.
        
        Version: 1.2
        RTM: 004
        """
        try:
            if item == rooms[self.current_room]["Item"]:
                if item not in self.inventory:
                    self.inventory.append(rooms[self.current_room]["Item"])
                    return f"{item} retrieved!"
                else:
                    return f"You already have the {item}"
            else:
                return f"Can't find {item}"
        except KeyError:
            return f"Can't find {item}"

    def can_fight_boss(self):
        """
        Module: Player.can_fight_boss
        Date: 8/6/24
        Programmer: Timothy Stowe
        
        Purpose: Determines if the player has collected enough items to fight the boss.
        
        Version: 1.1
        RTM: 005
        """
        return len(self.inventory) >= 6


def process_input(user_input, player, rooms):
    """
    Module: process_input
    Date: 8/6/24
    Programmer: Timothy Stowe
    
    Purpose: Processes the user's input, executing the appropriate action (move, get item,
    fight boss, or exit) based on the input command.
    
    Version: 1.2
    RTM: 006
    """
    next_move = user_input.split(' ')
    action = next_move[0].title()
    item = "Item"
    direction = "null"

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()
        item = " ".join(item).title()

    if action == "Go":
        return player.move(direction, rooms)
    elif action == "Get":
        return player.get_item(item, rooms)
    elif action == "Fight" and player.current_room == "roomEight":
        if player.can_fight_boss():
            return "BossFight"
        else:
            return "You need at least 6 items to fight the boss!"
    elif action == "Exit":
        return "Exit"
    else:
        return "Invalid command"