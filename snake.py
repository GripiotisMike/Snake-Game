from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[i - 1].xcor()
            new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def snake_reset(self):
        for seg in self.segment_list:
            seg.goto(1000, 1000)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]
