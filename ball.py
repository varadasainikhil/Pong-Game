from turtle import Turtle
import random
SPEED = 9


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.speed("slowest")

    def move(self):
        x = self.xcor() + SPEED
        y = self.ycor() + SPEED
        self.goto(x, y)

