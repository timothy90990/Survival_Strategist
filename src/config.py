import os
import tempfile

# Add debug level option
DEBUG_LEVEL = "DEBUG"  # Can be "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL"
#### CHANGE ME FOR RELEASE ####

# Add log file path in temporary folder
LOG_FILE = os.path.join(tempfile.gettempdir(), "dungeon_game.log")
# Log files will be at C:\Users\<username>\AppData\Local\Temp\dungeon_game.log

# Show where the log file is in the terminal
print(f"Log file is located at: {LOG_FILE}")

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