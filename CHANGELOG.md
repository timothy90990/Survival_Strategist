# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.4] - 2024-08-06
### Added
- Comprehensive preambles to all functions and methods across the project
  - Added to `game_logic.py`, `user_interface.py`, and `quotes.py`
  - Each preamble includes module/function name, date, programmer name, purpose, version, and RTM number
- RTM (Requirements Traceability Matrix) numbers for each function and method

### Changed
- Updated documentation style to meet project requirements
- Improved code readability and maintainability with detailed function descriptions
- Map is generated rather than using a sketch image

## [0.0.3]
### Added
- Final boss placeholder logic
- Added explosion animation to the credits screen

## [0.0.2]

### Added
- Implimented multiple choice questions for items picked up as well as a "Try Later" option if the user is not ready to answer the question.
- Added a log file to the project located in the temporary folder. C:\Users\<username>\AppData\Local\Temp\dungeon_game.log

### Changed
- Modified `check_picked_up_items` and `show_dialog` methods in `DungeonGameGUI` class to allow users to postpone answering questions for picked up items
- Changed the North, East, West, and South to arrow buttons instead.

### Fixes
- Fixed issue with "Try Later" functionality not working correctly
- Fixed issue with items being automatically added to inventory when entering a room

### Added
- New file `src/modules/quotes.py` to handle quote processing
  - Implemented `get_quote()` function to retrieve quotes for items
- Dialog box functionality to display quotes when new items are picked up
  - Added `show_dialog()` method in `DungeonGameGUI` class
- Logging system for better debugging and issue diagnosis
  - Added logging to `main.py`, `user_interface.py`, and `quotes.py`
  - Log messages for key events such as initialization, user actions, and error handling

### Changed
- Modified `get_item()` method in `DungeonGameGUI` class to display quote dialog
- Updated `main.py` to initialize logging configuration
- Enhanced error handling in `quotes.py` with try-except block and logging
- Modified `show_dialog()` method in `DungeonGameGUI` class to make quote dialogs always on top
- Prevented interaction with the main game window while a quote dialog is open

### Improved
- Enhanced user experience by forcing focus on quote dialogs when new items are picked up
### Fixed
- Improved error handling for quote retrieval in case of file read issues

## [0.0.1] - 2024-07-13

### Added
- Initial project structure
- Basic dungeon game functionality
- User interface using customtkinter
- Player movement and item collection mechanics
- Map display with room positions
- Configuration file for game settings
- JSON file for storing quotes