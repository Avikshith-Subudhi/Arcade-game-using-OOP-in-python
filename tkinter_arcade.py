import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
current_dir = os.getcwd()
snake_game_path = "C:\\Users\\avisu\\OneDrive\\Documents\\python project sample\\snake game"
pong_game_path = "C:\\Users\\avisu\\OneDrive\\Documents\\python project sample\\pong game"
crossing_road_path = "C:\\Users\\avisu\\OneDrive\\Documents\\python project sample\\crossing road"
sys.path.append(os.path.join(current_dir, snake_game_path))
sys.path.append(os.path.join(current_dir, pong_game_path))
sys.path.append(os.path.join(current_dir, crossing_road_path))
from cr_main import cr_game
from sg_main import sg_game
from pong_main import pong_game
# Replace 'path/to/your/image.png' with the actual path to your background image
background_image_path = 'C:/Users/avisu/OneDrive/Documents/python project sample/images/output.png'
arcade_image_path = 'C:/Users/avisu/OneDrive/Documents/python project sample/images/png-transparent-laser-tag-mount-blade-ii-bannerlord-arcade-game-arcade-logo.png'


class window:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Arcade")
        # Load the background image
        self.image = Image.open(background_image_path)
        # Convert image to tkinter compatible format
        self.tk_image = ImageTk.PhotoImage(self.image)
        # Create a label for the background image
        self.background_label = tk.Label(self.root, image=self.tk_image)
        # Disable resizing of the window to prevent image distortion (optional)
        # root.resizable(False, False)
        self.background_label.pack(fill=tk.BOTH, expand=True)

        # load arcade image
        self.arcade_image = Image.open(arcade_image_path)
        self.arcade_image = self.arcade_image.resize((320, 50))
        self.tk_arcade_image = ImageTk.PhotoImage(self.arcade_image)
        self.arcade_image_label = tk.Label(self.root, image=self.tk_arcade_image)
        self.arcade_image_label.place(x=80, y=50)

        # Create the buttons
        self.button1 = tk.Button(self.root, text="Snake game", command=sg_game)
        self.button1.place(x=200, y=150)
        self.button2 = tk.Button(self.root, text="Ping pong")
        self.button2.place(x=205, y=200)
        self.button3 = tk.Button(self.root, text="Crossing road", command=cr_game)
        self.button3.place(x=197, y=250)

        # Main loop
        self.root.mainloop()


if __name__ == "__main__":
    window()
