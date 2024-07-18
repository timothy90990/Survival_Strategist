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
                return f"You travel {direction} and collect {item}."
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

rooms = {
    'roomOne': {'North': 'roomTwo', 'South': 'roomThree', 'East': 'roomFive', 'Item': 'One'},
    'roomTwo': {'South': 'roomOne', 'Item': 'Two'},
    'roomThree': {'North': 'roomOne', 'East': 'roomFour', 'Item': 'Three'},
    'roomFive' : {'West': 'roomOne', 'North': 'roomSix', 'East': 'roomEight', 'Item': 'Four'},
    'roomSix' : {'South': 'roomFive', 'East': 'roomSeven', 'Item': 'Five'},
    'roomSeven': {'West': 'roomSix', 'Item': 'Six'},
    'roomFour': {'West': 'roomThree', 'Item': 'Three'},
    'roomEight': {'West': 'roomFive', 'Boss': 'Boss'}
}

room_positions = {
    'roomOne': (50, 200),
    'roomTwo': (50, 50),
    'roomThree': (50, 350),
    'roomFour': (200, 350),
    'roomFive': (200, 200),
    'roomSix': (200, 50),
    'roomSeven': (350, 50),
    'roomEight': (350, 200)
}

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