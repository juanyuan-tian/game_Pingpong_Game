from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball # class
# import math
import time # module
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)  # turn off the animation, need to update

# create paddles on both sides
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()  #ball always moving

    # detect the collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # while ball.xcor() < 390:
        # bounce后还能继续move
        #     ball.bounce()
        # ball.move()

    # collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 \
            or ball.xcor() < - 320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # detect if one misses the ball
    if ball.xcor() > 370:
        ball.goto(0,0)
        ball.bounce_x()
        ball.move_speed = 0.1
        scoreboard.r_point()

    if ball.xcor() < -370:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.move_speed = 0.1
        scoreboard.l_point()




screen.exitonclick()