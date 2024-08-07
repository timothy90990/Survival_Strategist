import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageDraw, ImageFont
from src.modules.game_logic import Player, rooms, room_positions, process_input
from src.modules.quotes import get_quote
import logging
import random

class DungeonGameGUI:
    """
    Module: DungeonGameGUI
    Date: 7/19/24
    Programmer: Timothy Stowe
    
    Purpose: This class represents the main user interface for the Dungeon Game.
    It manages the game window, player interactions, and visual elements.
    
    Version: 1.0
    RTM: 007
    """
    def __init__(self, root):
        """
        Module: DungeonGameGUI.__init__
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Initializes the DungeonGameGUI object, setting up the game window,
        player, and initial game state.
        
        Version: 1.0
        RTM: 008
        """
        logging.info("Initializing DungeonGameGUI")
        self.root = root
        self.root.title("Dungeon Game")
        self.player = Player(start_room="roomOne")
        self.msg = ""

        # Generate the map image
        map_image = self.generate_map()
        self.map_image = CTkImage(light_image=map_image, dark_image=map_image, size=(400, 400))

        # Load the character image
        character_image = Image.open("src/media/character.png")
        
        self.character_image = CTkImage(light_image=character_image, dark_image=character_image, size=(20, 20))


        self.create_widgets()
        self.show_map()
        self.show_character()

    def generate_map(self):
        """
        Module: DungeonGameGUI.generate_map
        Date: 8/6/24
        Programmer: Timothy Stowe
        
        Purpose: Generates an aesthetic map image based on the room positions defined in config.py
        
        Version: 1.0
        RTM: 31
        """
        logging.info("Generating map")
        map_size = (400, 400)
        map_image = Image.new('RGBA', map_size, color=(255, 255, 255, 0))  # Transparent background
        draw = ImageDraw.Draw(map_image)

        # Draw connections
        for room, connections in rooms.items():
            start_x, start_y = room_positions[room]
            for direction, connected_room in connections.items():
                if direction in ['North', 'South', 'East', 'West']:
                    end_x, end_y = room_positions[connected_room]
                    draw.line([(start_x, start_y), (end_x, end_y)], fill=(200, 200, 200, 150), width=3)

        # Draw rooms
        room_size = 85
        for room, (x, y) in room_positions.items():
            # Create the center of the room to be the center of the square
            x -= room_size // 2
            y -= room_size // 2

            # Draw a rounded square room with Apple-inspired design
            corner_radius = 20
            room_color = (220, 220, 220, 230)  # Light gray, slightly transparent
            border_color = (180, 180, 180, 255)  # Darker gray for border
            
            # Draw the main rounded square
            draw.rounded_rectangle([x, y, x + room_size, y + room_size], 
                                   radius=corner_radius, 
                                   fill=room_color, 
                                   outline=border_color, 
                                   width=2)
            
            # Add a subtle inner shadow
            shadow_offset = 3
            shadow_color = (0, 0, 0, 30)  # Very light black for shadow
            draw.rounded_rectangle([x + shadow_offset, y + shadow_offset, 
                                    x + room_size - shadow_offset, y + room_size - shadow_offset],
                                   radius=corner_radius,
                                   fill=None,
                                   outline=shadow_color,
                                   width=2)
            
            # Add a subtle highlight
            highlight_offset = 1
            highlight_color = (255, 255, 255, 50)  # Very light white for highlight
            draw.rounded_rectangle([x + highlight_offset, y + highlight_offset, 
                                    x + room_size - highlight_offset, y + room_size - highlight_offset],
                                   radius=corner_radius,
                                   fill=None,
                                   outline=highlight_color,
                                   width=1)
            # Add room name
            font_size = 12
            font = ImageFont.truetype("arial.ttf", font_size)
            text_bbox = draw.textbbox((0, 0), room, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (room_size - text_width) // 2
            text_y = y + (room_size - text_height) // 2

            # Split and capitalize room name
            room_words = room.split('room')
            if len(room_words) > 1:
                capitalized_room = 'Room ' + room_words[1].capitalize()
            else:
                capitalized_room = room.capitalize()


            # Recalculate text position with new room name
            text_bbox = draw.textbbox((0, 0), capitalized_room, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = x + (room_size - text_width) // 2
            text_y = y + (room_size - text_height) // 2

            draw.text((text_x, text_y), capitalized_room, fill=(0, 0, 0, 255), font=font)

        return map_image

    def create_widgets(self):
        """
        Module: DungeonGameGUI.create_widgets
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Creates and sets up all the widgets for the game interface,
        including the map frame, controls frame, and navigation buttons.
        
        Version: 1.0
        RTM: 009
        """
        logging.info("Creating widgets")
        # Create a frame for the map
        self.map_frame = ctk.CTkFrame(self.root)
        self.map_frame.pack(side="top", fill="both", expand=True)
        self.map_frame.configure(fg_color="transparent")  # Set transparent background

        self.map_label = ctk.CTkLabel(self.map_frame, text="")
        self.map_label.pack()

        # Create a frame for the controls
        self.controls_frame = ctk.CTkFrame(self.root)
        self.controls_frame.pack(side="bottom", fill="x")

        self.info_label = ctk.CTkLabel(self.controls_frame, text="", justify="left")
        self.info_label.pack()

        # Add arrow buttons
        button_size = 40
        arrow_frame = ctk.CTkFrame(self.controls_frame)
        arrow_frame.pack(pady=10)
        # Remove the background color from the arrow frame
        arrow_frame.configure(fg_color="transparent")

        self.north_button = ctk.CTkButton(arrow_frame, text="↑", width=button_size, height=button_size, command=lambda: self.move("North"))
        self.north_button.grid(row=0, column=1)

        self.west_button = ctk.CTkButton(arrow_frame, text="←", width=button_size, height=button_size, command=lambda: self.move("West"))
        self.west_button.grid(row=1, column=0)

        self.east_button = ctk.CTkButton(arrow_frame, text="→", width=button_size, height=button_size, command=lambda: self.move("East"))
        self.east_button.grid(row=1, column=2)

        self.south_button = ctk.CTkButton(arrow_frame, text="↓", width=button_size, height=button_size, command=lambda: self.move("South"))
        self.south_button.grid(row=2, column=1)

        self.character_label = ctk.CTkLabel(self.map_frame, text="")  # Initialize without text
        self.character_label.place(x=0, y=0)  # Initial placement

        self.update_info()

    def show_map(self):
        """
        Module: DungeonGameGUI.show_map
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Displays the game map on the user interface.
        
        Version: 1.0
        RTM: 010
        """
        logging.info("Showing map")
        self.map_label.configure(image=self.map_image)
        self.map_label.configure(fg_color="transparent")  # Set transparent background

    def show_character(self):
        """
        Module: DungeonGameGUI.show_character
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Displays the character on the map and updates its position.
        
        Version: 1.0
        RTM: 011
        """
        logging.info("Showing character")
        self.character_label.configure(image=self.character_image)
        self.update_character_position()

    def update_character_position(self):
        """
        Module: DungeonGameGUI.update_character_position
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Updates the character's position on the map based on the current room.
        
        Version: 1.0
        RTM: 012
        """
        logging.debug(f"Updating character position to {self.player.current_room}")
        x, y = room_positions[self.player.current_room]
        self.character_label.place(x=x, y=y)

    def update_info(self):
        """
        Module: DungeonGameGUI.update_info
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Updates the information display with the current room and inventory.
        Also checks if the player is in the boss room.
        
        Version: 1.0
        RTM: 013
        """
        logging.debug(f"Updating info: {self.player.current_room}, Inventory: {self.player.inventory}")
        info_text = f"You are in the {self.player.current_room}\nInventory: {self.player.inventory}\n"
        self.info_label.configure(text=info_text, anchor="center")
        self.update_character_position()
        if self.player.current_room == "roomEight":
            self.show_boss_dialog()
        else:
            pass

    def process_input(self, event):
        """
        Module: DungeonGameGUI.process_input
        Date: 7/19/24
        Programmer: Timothy Stowe
        
        Purpose: Processes user input from the input entry field and updates the game state.
        
        Version: 1.0
        RTM: 014
        """
        logging.debug(f"Processing input: {self.input_entry.get()}")
        self.msg = process_input(self.input_entry.get(), self.player, rooms)
        self.input_entry.delete(0, ctk.END)
        self.update_info()

    def move(self, direction):
        """
        Module: DungeonGameGUI.move
        Date: 7/26/24
        Programmer: Timothy Stowe
        
        Purpose: Moves the player in the specified direction and updates the game state.
        
        Version: 1.1
        RTM: 015
        """
        logging.debug(f"Moving {direction}")
        self.msg = self.player.move(direction, rooms)
        self.update_info()
        self.check_room_item()

    def check_room_item(self):
        """
        Module: DungeonGameGUI.check_room_item
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Checks if there's an item in the current room and shows the item dialog if necessary.
        
        Version: 1.2
        RTM: 016
        """
        current_room = self.player.current_room
        room_item = rooms[current_room].get("Item")
        if room_item and room_item not in self.player.inventory:
            self.show_item_dialog(room_item)

    def show_item_dialog(self, item):
        """
        Module: DungeonGameGUI.show_item_dialog
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Displays a dialog with information about a newly found item,
        including a quote and a question.
        
        Version: 1.2
        RTM: 017
        """
        quote_data = get_quote(item)
        self.show_dialog(
            "New Item",
            f"You found: {item}\n\n{quote_data['key_message']}",
            quote_data['question'],
            quote_data['answers'],
            quote_data['correct_answer'],
            item
        )

    def show_dialog(self, title, message, question, answers, correct_answer, item):
        """
        Module: DungeonGameGUI.show_dialog
        Date: 7/26/24
        Programmer: Timothy Stowe
        
        Purpose: Displays a dialog box with a question and multiple-choice answers.
        Handles the logic for answering the question and collecting the item.
        
        Version: 1.1
        RTM: 018
        """
        logging.info(f"Showing dialog: {title}")
        dialog = ctk.CTkToplevel(self.root)
        dialog.title(title)
        dialog.attributes('-topmost', True)
        # Prevent user from using the x button to close the dialog
        dialog.protocol("WM_DELETE_WINDOW", lambda: None)
        # Remove the x button from the dialog
        dialog.wm_overrideredirect(True)
        dialog.grab_set()

        content_frame = ctk.CTkFrame(dialog)
        content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        label = ctk.CTkLabel(content_frame, text=message, wraplength=350)
        label.pack(pady=10)

        question_label = ctk.CTkLabel(content_frame, text=question, wraplength=350)
        question_label.pack(pady=10)

        result_label = ctk.CTkLabel(content_frame, text="")
        result_label.pack(pady=10)

        ok_button = ctk.CTkButton(content_frame, text="Collect Item", state="disabled")
        ok_button.pack(side="left", padx=(0, 10), pady=10)

        def on_try_later():
            dialog.destroy()

        try_later_button = ctk.CTkButton(content_frame, text="Try Again Later", command=on_try_later)
        try_later_button.pack(side="right", padx=(10, 0), pady=10)
        # Change the color to red for the try later button
        try_later_button.configure(fg_color="red")

        def check_answer(selected_answer):
            nonlocal correct_answer_given
            if selected_answer == correct_answer:
                result = "Correct!"
                correct_answer_given = True
                ok_button.configure(state="normal")
                for btn in answer_buttons:
                    btn.configure(state="disabled")
            else:
                result = "Incorrect. Try again!"
            result_label.configure(text=result)

        answer_buttons = []
        for answer in answers:
            answer_button = ctk.CTkButton(content_frame, text=answer, command=lambda a=answer: check_answer(a))
            answer_button.pack(pady=5)
            answer_buttons.append(answer_button)

        correct_answer_given = False

        def on_ok():
            """
            Module: DungeonGameGUI.show_dialog.on_ok
            Date: 8/2/24
            Programmer: Timothy Stowe
            
            Purpose: Handles the action when the player correctly answers the question
            and collects the item.
            
            Version: 1.2
            RTM: 024
            """
            if correct_answer_given:
                self.player.inventory.append(item)
                self.update_info()
            dialog.destroy()

        ok_button.configure(command=on_ok)

        dialog.update_idletasks()
        dialog_width = content_frame.winfo_reqwidth() + 40
        dialog_height = content_frame.winfo_reqheight() + 40
        dialog.geometry(f"{dialog_width}x{dialog_height}")
        dialog.resizable(False, False)

        dialog.wait_window()

    def show_boss_dialog(self):
        """
        Module: DungeonGameGUI.show_boss_dialog
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Displays the boss dialog when the player enters the boss room.
        Provides options to fight the boss or exit the room.
        
        Version: 1.2
        RTM: 019
        """
        boss_data = get_quote("Boss")
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Final Boss Room")
        dialog.attributes('-topmost', True)
        dialog.protocol("WM_DELETE_WINDOW", lambda: self.close_boss_dialog(dialog))
        dialog.grab_set()

        content_frame = ctk.CTkFrame(dialog)
        content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        message_label = ctk.CTkLabel(content_frame, text=boss_data["key_message"], wraplength=350)
        message_label.pack(pady=10)

        fight_button = ctk.CTkButton(content_frame, text="Fight Boss", command=lambda: self.fight_boss(dialog))
        fight_button.pack(pady=10)

        if not self.player.can_fight_boss():
            fight_button.configure(state="disabled")
            items_needed = 6 - len(self.player.inventory)
            instruction_label = ctk.CTkLabel(content_frame, text=f"Collect {items_needed} more item(s) to fight the boss.", wraplength=350)
            instruction_label.pack(pady=10)

        exit_button = ctk.CTkButton(content_frame, text="Exit Room", command=lambda: self.close_boss_dialog(dialog))
        exit_button.pack(pady=10)

        dialog.update_idletasks()
        dialog_width = content_frame.winfo_reqwidth() + 40
        dialog_height = content_frame.winfo_reqheight() + 40
        dialog.geometry(f"{dialog_width}x{dialog_height}")
        dialog.resizable(False, False)

    def close_boss_dialog(self, dialog):
        """
        Module: DungeonGameGUI.close_boss_dialog
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Closes the boss dialog and releases the grab on the window.
        
        Version: 1.2
        RTM: 020
        """
        dialog.grab_release()
        dialog.destroy()

    def fight_boss(self, dialog):
        """
        Module: DungeonGameGUI.fight_boss
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Initiates the boss fight sequence, closing the dialog
        and showing the explosion animation.
        
        Version: 1.2
        RTM: 021
        """
        dialog.destroy()
        self.show_explosion(callback=self.show_credits)

    def show_explosion(self, callback=None):
        """
        Module: DungeonGameGUI.show_explosion
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Displays an explosion animation after defeating the boss.
        
        Version: 1.2
        RTM: 022
        """
        explosion = ctk.CTkToplevel(self.root)
        explosion.title("Explosion")
        explosion.attributes('-topmost', True)
        explosion.geometry("400x400")

        canvas = ctk.CTkCanvas(explosion, width=400, height=400, bg="black")
        canvas.pack()

        particles = []
        for _ in range(100):
            x = 200
            y = 200
            dx = random.uniform(-5, 5)
            dy = random.uniform(-5, 5)
            radius = random.uniform(2, 5)
            color = random.choice(["red", "orange", "yellow"])
            particles.append([x, y, dx, dy, radius, color])

        def animate_explosion(step=0):
            """
            Module: DungeonGameGUI.show_explosion.animate_explosion
            Date: 8/2/24
            Programmer: Timothy Stowe
            
            Purpose: Animates the explosion particles frame by frame.
            
            Version: 1.2
            RTM: 025
            """
            canvas.delete("all")
            still_moving = False
            for particle in particles:
                x, y, dx, dy, radius, color = particle
                if abs(dx) > 0.1 or abs(dy) > 0.1:
                    still_moving = True
                    particle[0] += dx
                    particle[1] += dy
                    particle[3] += 0.1  # Add gravity effect
                    particle[2] *= 0.98  # Add air resistance
                    particle[3] *= 0.98  # Add air resistance
                    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline=color)
            
            if still_moving and step < 100:
                explosion.after(20, animate_explosion, step+1)
            else:
                explosion.after(500, lambda: end_explosion(explosion, callback))

        def end_explosion(explosion_window, callback_func):
            """
            Module: DungeonGameGUI.show_explosion.end_explosion
            Date: 8/2/24
            Programmer: Timothy Stowe
            
            Purpose: Ends the explosion animation and calls the callback function.
            
            Version: 1.2
            RTM: 026
            """
            explosion_window.destroy()
            if callback_func:
                self.root.after(100, callback_func)

        animate_explosion()

    def show_credits(self):
        """
        Module: DungeonGameGUI.show_credits
        Date: 8/2/24
        Programmer: Timothy Stowe
        
        Purpose: Displays the game credits after defeating the boss.
        
        Version: 1.2
        RTM: 023
        """
        credits_data = get_quote("Credits")
        credits = ctk.CTkToplevel(self.root)
        credits.title("Credits")
        credits.attributes('-topmost', True)
        credits.geometry("400x400")

        credits_label = ctk.CTkLabel(credits, text=credits_data["key_message"], wraplength=350)
        credits_label.pack(pady=20)

        close_button = ctk.CTkButton(credits, text="Close", command=credits.destroy)
        close_button.pack(pady=10)