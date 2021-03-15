from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
score = Scoreboard()


r_player = Paddle((350, 0))
l_player = Paddle((-350, 0))
pelota = Ball()

screen.listen()
screen.onkeypress(fun=r_player.up, key='Up')
screen.onkeypress(fun=r_player.down, key='Down')
screen.onkeypress(fun=l_player.up, key='w')
screen.onkeypress(fun=l_player.down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(pelota.move_speed)
    screen.update()
    pelota.move()

    # Detect Collision
    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.bounce_y()

    # Detect collision with r_paddle
    if pelota.distance(r_player) < 50 and pelota.xcor() > 320 or pelota.distance(
            l_player) < 50 and pelota.xcor() < -320:
        pelota.bounce_x()

    # Detect when ball misses player
    if pelota.xcor() > 400:
        pelota.refresh()
        score.l_point()

    if pelota.xcor() < -400:
        pelota.refresh()
        score.r_point()

screen.exitonclick()
