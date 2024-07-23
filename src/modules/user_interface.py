import customtkinter as ctk
from PIL import Image, ImageTk
from src.modules.game_logic import Player, rooms, room_positions, process_input, picked_up_items
from src.modules.quotes import get_quote
import logging

class DungeonGameGUI:
    def __init__(self, root):
        logging.info("Initializing DungeonGameGUI")
        self.root = root
        self.root.title("Dungeon Game")
        self.player = Player(start_room="roomOne")
        self.msg = ""

        self.create_widgets()
        self.show_map()
        self.show_character()
        
        # Add listener for picked up items
        self.root.after(100, self.check_picked_up_items)

    def create_widgets(self):
        logging.info("Creating widgets")
        # Create a frame for the map
        self.map_frame = ctk.CTkFrame(self.root)
        self.map_frame.pack(side="top", fill="both", expand=True)

        self.map_label = ctk.CTkLabel(self.map_frame, text="")
        self.map_label.pack()

        # Create a frame for the controls
        self.controls_frame = ctk.CTkFrame(self.root)
        self.controls_frame.pack(side="bottom", fill="x")

        self.info_label = ctk.CTkLabel(self.controls_frame, text="", justify="left")
        self.info_label.pack()

        # Add directional buttons
        self.north_button = ctk.CTkButton(self.controls_frame, text="North", command=lambda: self.move("North"))
        self.north_button.pack()

        self.south_button = ctk.CTkButton(self.controls_frame, text="South", command=lambda: self.move("South"))
        self.south_button.pack()

        self.east_button = ctk.CTkButton(self.controls_frame, text="East", command=lambda: self.move("East"))
        self.east_button.pack()

        self.west_button = ctk.CTkButton(self.controls_frame, text="West", command=lambda: self.move("West"))
        self.west_button.pack()

        self.character_label = ctk.CTkLabel(self.map_frame, text="")  # Initialize without text
        self.character_label.place(x=0, y=0)  # Initial placement

        self.update_info()

    def show_map(self):
        logging.info("Showing map")
        img = Image.open('src/media/Map.jpeg')
        img = img.resize((400, 400), Image.LANCZOS)
        self.map_img = ImageTk.PhotoImage(img)
        self.map_label.configure(image=self.map_img)

    def show_character(self):
        logging.info("Showing character")
        self.character_img = Image.open('src/media/character.png')
        self.character_img = self.character_img.resize((20, 20), Image.LANCZOS)
        self.character_img = ImageTk.PhotoImage(self.character_img)
        self.character_label.configure(image=self.character_img)  # Update label with image
        self.update_character_position()

    def update_character_position(self):
        logging.debug(f"Updating character position to {self.player.current_room}")
        pos = room_positions[self.player.current_room]
        self.character_label.place(x=pos[0], y=pos[1])

    def update_info(self):
        logging.debug(f"Updating info: {self.player.current_room}, Inventory: {self.player.inventory}")
        info_text = f"You are in the {self.player.current_room}\nInventory: {self.player.inventory}\n{'-' * 27}"
        self.info_label.configure(text=info_text)
        self.update_character_position()

    def process_input(self, event):
        logging.debug(f"Processing input: {self.input_entry.get()}")
        self.msg = process_input(self.input_entry.get(), self.player, rooms)
        self.input_entry.delete(0, ctk.END)
        self.update_info()

    def move(self, direction):
        logging.debug(f"Moving {direction}")
        self.msg = self.player.move(direction, rooms)
        self.update_info()

    def show_dialog(self, title, message, mental_health_quote):
        logging.info(f"Showing dialog: {title}")
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x200")
        dialog.attributes('-topmost', True)  # Make the dialog always on top
        dialog.grab_set()  # Prevent interaction with the main window

        label = ctk.CTkLabel(dialog, text=message, wraplength=350)
        label.pack(pady=10)

        quote_label = ctk.CTkLabel(dialog, text=f"Mental Health Quote:\n{mental_health_quote}", wraplength=350)
        quote_label.pack(pady=10)

        ok_button = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)
        ok_button.pack(pady=10)

        dialog.wait_window()  # Wait for the dialog to be closed before continuing

    def check_picked_up_items(self):
        global picked_up_items
        if picked_up_items:
            item = picked_up_items.pop(0)
            quote_data = get_quote(item)
            self.show_dialog("New Item", f"You picked up: {item}\n\n{quote_data['key_message']}", quote_data['mental_health_quote'])
        self.root.after(100, self.check_picked_up_items)