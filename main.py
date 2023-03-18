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
    if ball.ycor() > 230 or ball.ycor() < -230 :
        ball.bounce_with_wall()
    left_y_upper_limit = left_paddle.ycor() + 50
    left_y_lower_limit = left_paddle.ycor() - 50
    right_y_upper_limit = right_paddle.ycor() + 50
    right_y_lower_limit = right_paddle.ycor() - 50
    if ball.xcor() > 330 and right_y_lower_limit < ball.ycor() < right_y_upper_limit:
        ball.bounce_with_paddle()
    if ball.xcor() < -330 and left_y_lower_limit < ball.ycor() < left_y_upper_limit:
        ball.bounce_with_paddle()
    screen.update()
screen.exitonclick()
