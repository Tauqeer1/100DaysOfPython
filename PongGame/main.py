# Create the screen (Done)
# Create and move a paddle (Done)
# Create another paddle (Done)
# Create a ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses the ball
# Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move_ball()
    screen.update()

screen.exitonclick()