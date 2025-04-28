# Create the screen (Done)
# Create and move a paddle
# Create another paddle
# Create a ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses the ball
# Keep score

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=paddle1.go_up, key="Up")
screen.onkey(fun=paddle1.go_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()