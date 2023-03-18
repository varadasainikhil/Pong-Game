from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
l_player_score_text = Score("P1", -150)
r_player_score_text = Score("P2", 150)
l_player_misses = 0
r_player_misses = 0

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
game_over_text = Score("text", 0)
game_is_on = True
while game_is_on:
    left_y_upper_limit = left_paddle.ycor() + 50
    left_y_lower_limit = left_paddle.ycor() - 50
    right_y_upper_limit = right_paddle.ycor() + 50
    right_y_lower_limit = right_paddle.ycor() - 50
    time.sleep(0.1)
    ball.move()
    if r_player_misses == 5:
        game_over_text.game_over("P1")
        game_is_on = False
    if l_player_misses == 5:
        game_over_text.game_over("P2")
        game_is_on = False
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_with_wall()
    if ball.xcor() > 330 and right_y_lower_limit < ball.ycor() < right_y_upper_limit:
        r_player_score_text.increase_score()
        ball.bounce_with_paddle()
    if ball.xcor() < -330 and left_y_lower_limit < ball.ycor() < left_y_upper_limit:
        l_player_score_text.increase_score()
        ball.bounce_with_paddle()
    if ball.xcor() > 370:
        r_player_misses += 1
        ball.reset_position()
    if ball.xcor() < -370:
        l_player_misses += 1
        ball.reset_position()
    screen.update()
    l_player_score_text.show_score()
    r_player_score_text.show_score()
screen.exitonclick()
