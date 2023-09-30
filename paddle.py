from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.pu()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)


