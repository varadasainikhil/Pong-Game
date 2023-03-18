from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()

    def show_score(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"SCORE = {self.score}", align="center", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE = {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align="center", font=('Arial', 25, 'normal'))
