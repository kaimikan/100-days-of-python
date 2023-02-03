from turtle import Turtle
import random

SPAWN_AREA_WIDTH = 500
SPAWN_AREA_HEIGHT = 500


# inherit from Turtle so we can use its functionalities
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

        self.respawn()

    def respawn(self):
        # random spawn position
        random_x = random.randint(-int(SPAWN_AREA_WIDTH / 2), int(SPAWN_AREA_WIDTH / 2))
        random_y = random.randint(-int(SPAWN_AREA_HEIGHT / 2), int(SPAWN_AREA_HEIGHT / 2))
        self.goto(random_x, random_y)
