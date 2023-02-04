from turtle import Turtle
import random

CAR_SIZE = 20
BOTTOM_MARGIN = 100
TOP_MARGIN = 75
WEST = 180
SLOWEST_SPEED = 5
FASTEST_SPEED = 15


class Car(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.starting_position = (0, 0)
        self.drive_speed = random.randint(SLOWEST_SPEED, FASTEST_SPEED)
        self.finish_width = - self.screen_width / 2
        self.CAR_WIDTH = CAR_SIZE * 2.5
        self.CAR_HEIGHT = CAR_SIZE * 1.5

        self.initialize_car()

    def initialize_car(self):
        random_y = random.randint(-self.screen_height / 2 + CAR_SIZE + BOTTOM_MARGIN,
                                  self.screen_height / 2 - CAR_SIZE - TOP_MARGIN)
        random_x = random.randint(-self.screen_width / 2 + CAR_SIZE, self.screen_width / 3 - CAR_SIZE)
        self.setheading(WEST)
        self.starting_position = (random_x, random_y)
        self.shape("square")
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(random_color)
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(self.starting_position)

    def drive(self):
        # check if we have reached the west boundary and reset car position
        # this way we can reuse cars when they go out of bounds instead of spawning infinite ones
        if self.xcor() < self.finish_width:
            # we set it from the negative max to the positive max width of the screen
            self.setx(self.screen_width / 2)
        self.forward(self.drive_speed)

    def activate_turbo(self):
        self.drive_speed += 1.5

    def reset_drive_speed(self):
        self.drive_speed = random.randint(SLOWEST_SPEED, FASTEST_SPEED)
