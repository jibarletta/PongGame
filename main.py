from turtle import Turtle, Screen
from paddle import Paddle



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# ai_player = Paddle()
h_player = Paddle()

screen.listen()
screen.onkey(fun=h_player.up, key='Up')
screen.onkey(fun=h_player.down, key='Down')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()