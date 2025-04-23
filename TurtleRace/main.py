from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
is_race_on = False
x = -230
y = -100
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=x, y=y)
    y = y + 30
    turtle_list.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle wins!")
            else:
                print(f"You've lost! The {winning_color} turtle wins!")
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()