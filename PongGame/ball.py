from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(0, 0)

    def move_ball(self):
        # if self.distance((340, 340)) > 50:
        self.goto(self.xcor() + 10, self.ycor() + 10)

