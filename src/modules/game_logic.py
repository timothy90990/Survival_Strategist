from src.config import ROOMS as rooms
from src.config import ROOM_POSITION as room_positions
from src.config import QUOTES_PATH as quotes_path

picked_up_items = []

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction, rooms):
        try:
            self.current_room = rooms[self.current_room][direction]
            item = rooms[self.current_room].get("Item")
            if item and item not in self.inventory:
                self.inventory.append(item)
                picked_up_items.append(item)
                return f"You travel {direction}", item
            return f"You travel {direction}", None
        except KeyError:
            return "You can't go that way.", None

    def get_item(self, item, rooms):
        global picked_up_items
        try:
            if item == rooms[self.current_room]["Item"]:
                if item not in self.inventory:
                    self.inventory.append(rooms[self.current_room]["Item"])
                    picked_up_items.append(item)
                    return f"{item} retrieved!"
                else:
                    return f"You already have the {item}"
            else:
                return f"Can't find {item}"
        except KeyError:
            return f"Can't find {item}"


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
    elif action == "Exit":
        return "Exit"
    else:
        return "Invalid command"