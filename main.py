from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600

# Create the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Create a paddle
paddle_r = Paddle((350, 0))
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

paddle_l = Paddle((-350, 0))
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

# Create a ball and make it move
ball = Ball()

# Create a scoreboard
scores = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # Detect Collision with the top and bottom wall
    if abs(ball.ycor()) > 280:
        time.sleep(ball.velocity)
        screen.update()
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and 350 > ball.xcor() > 320 or ball.distance(
            paddle_l) < 50 and -350 < ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the paddle misses
    if ball.xcor() > 380:
        scores.l_point()
        scores.update_scoreboard()
        ball.reset_ball()
    elif ball.xcor() < -380:
        scores.r_point()
        scores.update_scoreboard()
        ball.reset_ball()

screen.exitonclick()
