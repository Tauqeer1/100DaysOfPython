from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # self.teleport(350, 0)
        self.goto(position)

    def create_paddle(self, position):
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20
        print(new_y)
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        print(new_y)
        self.goto(self.xcor(), new_y)