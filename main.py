import os
import customtkinter as ctk
from src.modules.user_interface import DungeonGameGUI

def main():
    root = ctk.CTk()  # Use CTk instead of Tk
    app = DungeonGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()