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
        t = (0, 0)
        for _ in range(3):
            self.add_segment(t)
            t = (t[0] - 20, t[1])

    def append_snake(self):
        snake_length = len(self.snake_list)
        position = self.snake_list[snake_length - 1].position()
        # position = (self.snake_list[snake_length - 1].xcor(), self.snake_list[snake_length - 1].ycor())
        self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.teleport(position[0], position[1])
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

    def set_snake_x_cor(self, x_coordinate):
        self.head.setx(x_coordinate)

    def set_snake_y_cor(self, y_coordinate):
        self.head.sety(y_coordinate)

    def reset_snake(self):
        for segment in self.snake_list:
            segment.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]