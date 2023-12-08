from turtle import  Screen
from paddle import *
from ball import Ball
from score import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.r_point()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x
        score.l_point()

    if ball.xcor() > 390:
        ball.reset_position()
        
    if ball.xcor() < -390:
        ball.reset_position()
        

    if score.l_score == 5 or score.r_score == 5:
        is_game_on = False

screen.bye()
