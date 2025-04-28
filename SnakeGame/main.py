# Day 1
# 1-Create Snake
# 2-Move the Snake
# 3-Control the Snake
# Day 2
# 4-Detect collision with food
# 5-Create a scoreboard
# 6-Detect collision with wall
# 7-Detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
LEFT_WALL = -285
RIGHT_WALL = 285
UP_WALL = 285
DOWN_WALL = -285
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
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

    # Detect collision with food
    distance = snake.head.distance(food)
    if distance < 15:
        food.create_random_food()
        snake.append_snake()
        score_board.increase_score()

    #  Detect collision with walls (Condition working)
    # if snake.head.xcor() > RIGHT_WALL or snake.head.xcor() < LEFT_WALL or snake.head.ycor() > UP_WALL or snake.head.ycor() < DOWN_WALL:
    #     game_is_on = False
    #     score_board.game_over()

    # Snake Wall direction
    if snake.head.xcor() > RIGHT_WALL:
        snake.set_snake_x_cor(LEFT_WALL)
    elif snake.head.xcor() < LEFT_WALL:
        snake.set_snake_x_cor(RIGHT_WALL)
    elif snake.head.ycor() > UP_WALL:
        snake.set_snake_y_cor(DOWN_WALL)
    elif snake.head.ycor() < DOWN_WALL:
        snake.set_snake_y_cor(UP_WALL)

    # Detect collision with tail
    for i in range(1, len(snake.snake_list)):
        if snake.head.distance(snake.snake_list[i]) < 10:
            game_is_on = False
            score_board.game_over()

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
