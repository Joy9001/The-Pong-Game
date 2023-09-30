from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color("white")
        self.setpos(0, 0)
        print(self.position())
        self.x_diff = 10
        self.y_diff = 10
        self.velocity = 0.1

    def move(self):
        self.setposition(self.xcor() + self.x_diff, self.ycor() + self.y_diff)

    def bounce_y(self):
        self.y_diff *= -1
        self.velocity *= 0.9

    def bounce_x(self):
        self.x_diff *= -1
        self.velocity *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.bounce_x()
