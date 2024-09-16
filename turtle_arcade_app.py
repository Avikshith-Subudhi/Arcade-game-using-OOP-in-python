import sys
import os
import turtle
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

background_image_path = 'C:/Users/avisu/OneDrive/Documents/python project sample/images/final bg.png'


class ArcadeWindow:
    def __init__(self):
        # Initialize the screen
        self.screen = turtle.Screen()
        self.screen.title("Arcade")
        self.screen.setup(width=847, height=643)
        self.screen.bgpic(background_image_path)
        self.button_length = 200
        self.button_width = 50

        # Draw the buttons
        self.draw_buttons()

        # Define actions for the buttons
        self.screen.onclick(self.button_click)

        # Start the main loop
        turtle.done()

    def draw_buttons(self):
        self.draw_button(-100, 0, "Snake game")
        self.draw_button(-100, -100, "Ping pong")
        self.draw_button(-100, -200, "Crossing road")

    def draw_button(self, x, y, text):
        button_turtle = turtle.Turtle()
        button_turtle.hideturtle()
        button_turtle.color("grey")
        button_turtle.penup()
        button_turtle.goto(x, y)
        button_turtle.pendown()
        button_turtle.begin_fill()
        button_turtle.goto(x + self.button_length, y)
        button_turtle.goto(x + self.button_length, y + self.button_width)
        button_turtle.goto(x, y + self.button_width)
        button_turtle.goto(x, y)
        button_turtle.end_fill()
        button_turtle.penup()
        button_turtle.goto(x + 15, y + 15)
        button_turtle.pendown()
        button_turtle.pencolor("black")
        button_turtle.write(text, font=("Arial", 20, "normal"))
        button_turtle.hideturtle()

    def button_click(self, x, y):
        if -100 < x < 100 and 0 < y < 50:
            # Call the corresponding game function
            turtle.Screen().clear()
            sg_game()
        elif -100 < x < 100 and -100 < y < -50:
            # Call the corresponding game function
            turtle.Screen().clear()
            pong_game()
        elif -100 < x < 100 and -200 < y < -150:
            # Call the corresponding game function
            turtle.Screen().clear()
            cr_game()
        else:
            pass  # Click was outside of buttons

# Function stubs for the game functions (replace with actual game code)


if __name__ == "__main__":
    arcade_window = ArcadeWindow()
