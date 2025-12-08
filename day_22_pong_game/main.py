import time
from turtle import Screen , Turtle
from ball import Ball
from Paddle import Paddle
from scoreboard import Scoreboard


screen =  Screen()
screen.bgcolor("black")
screen.setup(height = 600 , width = 800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up ,"Up")
screen.onkey(r_paddle.move_down,key ="Down")
screen.onkey(l_paddle.move_up ,"w")
screen.onkey(l_paddle.move_down,key ="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        #time.sleep(ball.move_speed)

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()