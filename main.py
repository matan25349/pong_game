from turtle import Screen, Turtle
import paddle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("pong")
screen.setup(800, 600)
screen.bgcolor("black")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()
    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        scoreboard.l_point()
        ball.penup()
        ball.goto(0, 0)
        ball.bounce_x()
screen.exitonclick()
