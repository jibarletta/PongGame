from turtle import Turtle
MOVE_DISTANCE = 20

# En esta sección había creado un self.player para poner a los jugadores en un lugar
# creándolos con una función aparte. Y luego refiriendome a ese objeto para modificarlos.
# Luego revisé el código con la autora del curso y pude ver como simplificar el mio
# quedando así:


class Paddle(Turtle):
    """Creates the players"""
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
