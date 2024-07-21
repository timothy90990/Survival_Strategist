# Add the path of quotes.json file
QUOTES_PATH = "src/quotes.json"

ROOM_POSITION = {
    'roomOne': (50, 200),
    'roomTwo': (50, 50),
    'roomThree': (50, 350),
    'roomFour': (200, 350),
    'roomFive': (200, 200),
    'roomSix': (200, 50),
    'roomSeven': (350, 50),
    'roomEight': (350, 200)
}

ROOMS = {
    'roomOne': {'North': 'roomTwo', 'South': 'roomThree', 'East': 'roomFive'},
    'roomTwo': {'South': 'roomOne', 'Item': 'One'},
    'roomThree': {'North': 'roomOne', 'East': 'roomFour', 'Item': 'Two'},
    'roomFive' : {'West': 'roomOne', 'North': 'roomSix', 'East': 'roomEight', 'Item': 'Four'},
    'roomSix' : {'South': 'roomFive', 'East': 'roomSeven', 'Item': 'Five'},
    'roomSeven': {'West': 'roomSix', 'Item': 'Six'},
    'roomFour': {'West': 'roomThree', 'Item': 'Three'},
    'roomEight': {'West': 'roomFive', 'Boss': 'Boss'}
}
