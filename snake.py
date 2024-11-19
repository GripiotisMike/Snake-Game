from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Snake:
    def __init__(self):
        """
        Initialize the snake with its starting segments and direction.
        """
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]  # The first segment is the snake's head

    def create_snake(self):
        """
        Create the initial snake with 3 segments.
        """
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        """
        Add a new segment to the snake at the current head's position.
        """
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        self.segment_list.append(segment)
        self.update_segments()

    def extend(self):
        """
        Add a new segment to the snake's body when it eats food.
        """
        self.add_segment()

    def move(self):
        """
        Move the snake forward. Each segment follows the one in front of it.
        """
        for i in range(len(self.segment_list) - 1, 0, -1):
            x = self.segment_list[i - 1].xcor()
            y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(x, y)
        self.head.forward(20)  # Move the head forward by 20 units

    def snake_reset(self):
        """
        Reset the snake to its initial state.
        """
        for segment in self.segment_list:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.segment_list.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        self.head = self.segment_list[0]  # Reset the head
