from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highscore = int(f.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.shapesize(3, 3)
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGN, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGN, font=FONT)
