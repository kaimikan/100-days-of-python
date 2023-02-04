from turtle import Turtle
import random

NORTH = 90


class Crosser(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.CROSSER_SIZE = 20 * 2.5
        self.starting_position = (0, -screen_height / 2 + self.CROSSER_SIZE)
        self.move_speed = 10
        self.screen_height = screen_height

        self.initialize_crosser()

    def initialize_crosser(self):
        self.shape("turtle")
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(random_color)
        self.shapesize(stretch_wid=2.5, stretch_len=2.5)
        self.penup()
        self.goto(self.starting_position)
        self.setheading(NORTH)

    def cross(self):
        self.forward(self.move_speed)

    def is_crosser_at_finish_line(self):
        return self.ycor() > self.screen_height / 2 - self.CROSSER_SIZE

    def reincarnate(self):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(random_color)

    def back_to_start(self):
        self.goto(0, -self.screen_height / 2 + self.CROSSER_SIZE)
