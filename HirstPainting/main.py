from turtle import Turtle, Screen
import random
import colorgram
t = Turtle()
t.speed("fastest")
t.hideturtle()

def rgb_color_tuple(num_of_colors):
    colors = colorgram.extract('image.jpg', num_of_colors)
    rgb_tuple_list = []
    for color in colors:
        rgb_tuple_list.append((color.rgb.r / 255, color.rgb.g / 255, color.rgb.b / 255))
    return rgb_tuple_list

rgb_tuple = rgb_color_tuple(30)

def draw_spot_painting(num_of_lines):
    t.pensize(25)
    t.penup()
    x = -200
    for i in range(0, 500, 50):
        y = i - 200
        t.penup()
        t.setpos(x, y)
        for _ in range(num_of_lines):
            t.pencolor(random.choice(rgb_tuple))
            t.pendown()
            t.forward(1)
            t.penup()
            t.forward(50)

draw_spot_painting(10)


screen = Screen()
screen.exitonclick()