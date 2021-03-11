from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle:
    """Creates the players"""
    def __init__(self):
        self.player = None
        self.create_paddle()
        self.move()

    def create_paddle(self):
        paleta = Turtle(shape='square')
        paleta.shapesize(stretch_len=1, stretch_wid=5)
        paleta.color('white')
        paleta.penup()
        paleta.goto(x=350, y=0)
        self.player = paleta

    def move(self):
        pass

    def up(self):
        new_y = self.player.ycor() + 20
        self.player.goto(x=self.player.xcor(), y=new_y)

    def down(self):
        new_y = self.player.ycor() - 20
        self.player.goto(x=self.player.xcor(), y=new_y)
