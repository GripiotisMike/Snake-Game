from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initialize the scoreboard to track the score and high score.
        Reads the high score from a file.
        """
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highscore = int(f.read())  # Read high score from file
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.shapesize(3, 3)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the displayed scoreboard with the current score and high score.
        """
        self.clear()  # Clear previous scoreboard before writing a new one
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGN, font=FONT)

    def score_increase(self):
        """
        Increase the score and update the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        """
        Reset the score. If the score is higher than the high score, update the high score.
        """
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.highscore}")  # Save the new high score to file
        self.score = 0
        self.update_scoreboard()
