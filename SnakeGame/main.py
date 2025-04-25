# Day 1
# 1-Create Snake
# 2-Move the Snake
# 3-Control the Snake
# Day 2
# 4-Detect collision with food
# 5-Create a scoreboard
# 6-Detect collision with wall
# 7-Detect collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



# Code Version 1
# game_is_on = True
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake_head_position = snake_list[0].position()
#     for index, snake in enumerate(snake_list):
#         if index == 0:
#             snake.forward(20)
#             # snake.left(90)
#             # time.sleep(1)
#         else:
#             position_before_move = snake.position()
#             snake.goto(snake_head_position[0], snake_head_position[1])
#             snake_head_position = position_before_move
#             # time.sleep(1)




screen.exitonclick()
