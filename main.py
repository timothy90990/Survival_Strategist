import customtkinter as ctk
from src.modules.user_interface import DungeonGameGUI
import logging

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting the application")
    root = ctk.CTk()  # Use CTk instead of Tk
    app = DungeonGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()