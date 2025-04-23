from turtle import Turtle, Screen
from random import random, choice, randint

my_turtle = Turtle()

# my_turtle.shape("square")
my_turtle.shapesize(1,1)

# for steps in range(5):
#     for c in ('black', 'white'):
#         my_turtle.color(c)
#         my_turtle.forward(20)


# for steps in range(10):
#     if steps % 2 == 0:
#         my_turtle.pendown()
#     else:
#         my_turtle.penup()
#     my_turtle.forward(10)

# for steps in range(10):
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)

# Triangle, Square, Pentagon, Hexagon,
# Heptagon, Octagon, Nonagon, Decagon
# Total angle / number of sides = angle -> 360 / 4 = 90, 360 / 5 = 72
def draw_shapes():
    for i in range(3, 11):
        angle = 360 / i
        my_turtle.color(random(), random(), random())
        for _ in range(i):
            my_turtle.forward(100)
            my_turtle.right(angle)

def draw_random_path():
    choice_list = [0, 90, 180, 270]
    my_turtle.pensize(10)
    my_turtle.speed("fastest")
    for i in range(200):
        my_turtle.pencolor(round(random()), round(random()), round(random()))
        my_turtle.setheading(choice(choice_list))
        my_turtle.forward(50)

for i in range(5):
    my_turtle.tilt(45)
    my_turtle.forward(10)
    my_turtle.circle(100)




my_screen = Screen()
my_screen.exitonclick()