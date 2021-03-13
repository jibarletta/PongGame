from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_player = Paddle((350, 0))
l_player = Paddle((-350, 0))
pelota = Ball()

screen.listen()
screen.onkey(fun=r_player.up, key='Up')
screen.onkey(fun=r_player.down, key='Down')
screen.onkey(fun=l_player.up, key='w')
screen.onkey(fun=l_player.down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    pelota.move()

    # Detect Collision
    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.bounce()

screen.exitonclick()
