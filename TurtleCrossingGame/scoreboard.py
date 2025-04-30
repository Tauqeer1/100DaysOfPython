from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Write the level on the screen, also handles game over

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write_level()


    def increase_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

