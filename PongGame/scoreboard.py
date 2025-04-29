from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()



    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write_score(self.l_score)
        self.goto(100, 200)
        self.write_score(self.r_score)

    def write_score(self, p_score):
        self.write(f"{p_score}", align="center", font=('Courier', 90, 'normal'))


    def increase_l_score(self):
        self.l_score += 1
        self.update_score_board()
        print(f"Left paddle score = {self.l_score}")

    def increase_r_score(self):
        self.r_score += 1
        self.update_score_board()
        print(f"Right paddle score = {self.r_score}")