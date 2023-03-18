from turtle import Turtle


class Score(Turtle):
    def __init__(self, name, x_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.x_position = x_position
        self.name = name

    def show_score(self):
        self.goto(self.x_position, 260)
        self.clear()
        self.write(f"{self.name} SCORE = {self.score}", align="center", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.name} SCORE = {self.score}", align="center")

    def game_over(self, text):
        self.goto(0, 0)
        self.clear()
        self.write(f"{text} WINS !!", align="center", font=('Arial', 25, 'normal'))
