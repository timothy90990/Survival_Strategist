import customtkinter as ctk
from PIL import Image, ImageTk
from src.modules.game_logic import Player, rooms, room_positions, process_input

class DungeonGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dungeon Game")
        self.player = Player(start_room="roomOne")
        self.msg = ""

        self.create_widgets()
        self.show_map()
        self.show_character()

    def create_widgets(self):
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
        img = Image.open('Map.jpeg')
        img = img.resize((400, 400), Image.LANCZOS)
        self.map_img = ImageTk.PhotoImage(img)
        self.map_label.configure(image=self.map_img)

    def show_character(self):
        self.character_img = Image.open('character.png')
        self.character_img = self.character_img.resize((20, 20), Image.LANCZOS)
        self.character_img = ImageTk.PhotoImage(self.character_img)
        self.character_label.configure(image=self.character_img)  # Update label with image
        self.update_character_position()

    def update_character_position(self):
        pos = room_positions[self.player.current_room]
        self.character_label.place(x=pos[0], y=pos[1])

    def update_info(self):
        info_text = f"You are in the {self.player.current_room}\nInventory: {self.player.inventory}\n{'-' * 27}"
        self.info_label.configure(text=info_text)
        self.update_character_position()

    def process_input(self, event):
        self.msg = process_input(self.input_entry.get(), self.player, rooms)
        self.input_entry.delete(0, ctk.END)
        self.update_info()

    def move(self, direction):
        self.msg = self.player.move(direction, rooms)
        self.update_info()

    def get_item(self, item):
        self.msg = self.player.get_item(item, rooms)
        self.update_info()