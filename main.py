import customtkinter as ctk
from src.modules.user_interface import DungeonGameGUI
import logging
from src.config import DEBUG_LEVEL, LOG_FILE

def setup_logging(): # Last week
    """
    Module: setup_logging
    Date: 8/2/24
    Programmer: Timothy Stowe
    
    Purpose: Sets up the logging configuration for the application.
    
    Version: 1.0
    RTM: 027
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, DEBUG_LEVEL))
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def main():
    """
    Module: main
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: The main function for the application.
    
    Version: 1.0
    RTM: 028
    """
    setup_logging()
    logging.info("Starting the application")
    root = ctk.CTk()
    app = DungeonGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    """
    Module: main
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: The main function for the application.
    
    Version: 1.0
    RTM: 029
    """
    main()
