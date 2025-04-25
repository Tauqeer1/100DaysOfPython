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
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

class Snake:
    def __init__(self):
        pass

def create_snake():
    x = 0
    y = 0
    snake_list_segments = []
    for _ in range(3):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.teleport(x, y)
        snake_segment.penup()
        snake_segment.speed(0)
        snake_list_segments.append(snake_segment)

        x = x - 20
    return snake_list_segments

snake_list = create_snake()

def move_up():
    snake_list[0].setheading(90)

def move_down():
    snake_list[0].setheading(270)

def move_left():
    snake_list[0].setheading(90)

def move_right():
    snake_list[0].setheading(180)

screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.onkey(fun=move_left, key="Left")
screen.onkey(fun=move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Store previous position of snake list
    prev_positions = []
    for snake in snake_list:
        prev_positions.append(snake.position())

    # Move head
    snake_list[0].forward(20)

    # Move body
    for i in range(1, len(snake_list)):
        prev_position = prev_positions[i - 1]
        snake_list[i].goto(prev_position)



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
