from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Your score is {self.score}", align=ALIGNMENT, font=(FONT, 24, "normal"))

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=(FONT, 20, "normal"))
