from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Player class manages turtle movement
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_touch_finish_line(self):
       return self.ycor() > FINISH_LINE_Y

    def reset_player_position(self):
        self.goto(STARTING_POSITION)