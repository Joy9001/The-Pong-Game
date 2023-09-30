from turtle import Turtle

FONT = ("Comic Sans MS", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(-100, 250)
        self.write(self.l_score, align="center", font=FONT)
        self.setpos(100, 250)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1
