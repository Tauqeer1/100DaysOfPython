from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

# def move_forwards():
#     t.forward(10)
# def move_up():
#     t.setheading(90)
#     t.forward(10)
# def move_down():
#     t.setheading(270)
#     t.forward(10)
# def move_left():
#     t.setheading(180)
#     t.forward(10)
# def move_right():
#     t.setheading(0)
#     t.forward(10)
# screen.listen()
# # screen.onkey(move_forwards, "space")
# screen.onkey(move_up, "Up")
# screen.onkey(move_down, "Down")
# screen.onkey(move_left, "Left")
# screen.onkey(move_right, "Right")
# screen.onkey(key="space", fun=move_forwards)

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def move_clockwise():
    t.right(10)
def move_counterclockwise():
    t.left(10)
def clear_screen():
    t.reset()
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_counterclockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()