from src.config import ROOMS as rooms
from src.config import ROOM_POSITION as room_positions
from src.config import QUOTES_PATH as quotes_path

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        try:
            new_room = rooms[self.current_room][direction]
            self.current_room = new_room
            return f"You travel {direction}"
        except KeyError:
            return "You can't go that way."

    def get_item(self, item, rooms):
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
        return len(self.inventory) >= 6


def process_input(user_input, player, rooms):
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