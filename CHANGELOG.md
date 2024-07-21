# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

## [0.0.1] - 2024-07-13???

### Added
- Initial project structure
- Basic dungeon game functionality
- User interface using customtkinter
- Player movement and item collection mechanics
- Map display with room positions
- Configuration file for game settings
- JSON file for storing quotes
