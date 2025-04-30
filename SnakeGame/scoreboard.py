from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('Arial', 24, 'normal'))

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 24, 'normal'))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_high_score_to_file()
        self.write_score()

    def write_high_score_to_file(self):
        with open("score.txt", "w") as file:
            file.write(str(self.high_score))

    def read_high_score_from_file(self):
        with open("score.txt", "r") as file:
            return int(file.read())
