from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
screen.exitonclick()
