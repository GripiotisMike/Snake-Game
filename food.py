from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """
        Initialize the food item as a red circle that appears at random positions
        on the screen within the boundaries.
        """
        super().__init__()
        self.shape("circle")
        self.penup()  # Don't leave a trail behind the food
        self.shapesize(0.5, 0.5)  # Smaller size for the food
        self.color("red")
        self.speed("fastest")  # Make the food appear instantly
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random location on the screen
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
