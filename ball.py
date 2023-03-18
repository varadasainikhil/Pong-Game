from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.speed("slowest")
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    def bounce_with_wall(self):
        self.ymove *= -1

    def bounce_with_paddle(self):
        self.xmove *= -1

    def increase_speed(self):
        self.xmove += 3

    def reset_position(self):
        self.xmove *= -1
        self.goto(0, self.ycor())
