from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        # x = 0
        # y = 0
        t = (0, 0)
        for _ in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            # snake_segment.shapesize(0.5, 0.5)
            snake_segment.teleport(t[0], t[1])
            snake_segment.penup()
            snake_segment.speed("fastest")
            self.snake_list.append(snake_segment)
            # x = x - 20
            t = (t[0] - 20, t[1])

    def append_snake(self):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_length = len(self.snake_list)
        snake_segment.teleport(self.snake_list[snake_length-1].xcor(), self.snake_list[snake_length-1].ycor() )

        snake_segment.penup()
        snake_segment.speed("fastest")
        self.snake_list.append(snake_segment)

    def move(self):
        # Store previous position of snake list
        prev_positions = []
        for snake in self.snake_list:
            prev_positions.append(snake.position())

        # Move head
        self.snake_list[0].forward(MOVE_DISTANCE)

        # Move body
        for i in range(1, len(self.snake_list)):
            prev_position = prev_positions[i - 1]
            self.snake_list[i].goto(prev_position)

    def move_up(self):
        curr_direction = self.head.heading()
        if curr_direction != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        curr_direction = self.head.heading()
        if curr_direction != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        curr_direction = self.head.heading()
        if curr_direction != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        curr_direction = self.head.heading()
        if curr_direction != LEFT:
            self.head.setheading(RIGHT)
